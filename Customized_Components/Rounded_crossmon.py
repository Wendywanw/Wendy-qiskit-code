# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import numpy as np
from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary.core import BaseQubit



class TransmonCross(BaseQubit):  # pylint: disable=invalid-name
    """The base `TransmonCross` class.

    Inherits `BaseQubit` class.

    Simple Metal Transmon Cross object. Creates the X cross-shaped island,
    the "junction" on the south end, and up to 3 connectors on the remaining arms
    (claw or gap).

    'claw_width' and 'claw_gap' define the width/gap of the CPW line that
    makes up the connector. Note, DC SQUID currently represented by single
    inductance sheet

    Add connectors to it using the `connection_pads` dictionary. See BaseQubit for more
    information.

    Sketch:
        Below is a sketch of the qubit
        ::

                                        claw_length
            Claw:       _________                    Gap:
                        |   ________________             _________    ____________
                  ______|  |                             _________|  |____________
                        |  |________________
                        |_________


    .. image::
        transmon_cross.png

    .. meta::
        Transmon Cross

    BaseQubit Default Options:
        * connection_pads: Empty Dict -- The dictionary which contains all active connection lines for the qubit.
        * _default_connection_pads: empty Dict -- The default values for the (if any) connection lines of the qubit.

    Default Options:
        * cross_width: '20um' -- Width of the CPW center trace making up the Crossmon
        * cross_length: '200um' -- Length of one Crossmon arm (from center)
        * cross_gap: '20um' -- Width of the CPW gap making up the Crossmon
        * cross_radius: '8um' -- Radius of the corners of the Crossmon
        * _default_connection_pads: Dict
            * connector_type: '0' -- 0 = Claw type, 1 = gap type
            * claw_length: '30um' -- Length of the claw 'arms', measured from the connector center trace
            * ground_spacing: '5um' -- Amount of ground plane between the connector and Crossmon arm (minimum should be based on fabrication capabilities)
            * claw_width: '10um' -- The width of the CPW center trace making up the claw/gap connector
            * claw_gap: '6um' -- The gap of the CPW center trace making up the claw/gap connector
            * connector_location: '0' -- 0 => 'west' arm, 90 => 'north' arm, 180 => 'east' arm
    """

    default_options = Dict(
        cross_width='20um',
        cross_length='200um',
        cross_gap='20um',
        chip='main',
        cross_radius='8um',
        resolution = '10',
        junction = 'False',
        inductor_width = '10um',
        jj_pocket_extent = '20um',
        _default_connection_pads=Dict(
            connector_type='0',  # 0 = Claw type, 1 = gap type
            claw_length='30um',
            ground_spacing='5um',
            claw_width='10um',
            claw_gap='6um',
            claw_radius='2um',
            connector_location='0'  # 0 => 'west' arm, 90 => 'north' arm, 180 => 'east' arm
        ))
    """Default options."""

    component_metadata = Dict(short_name='Cross',
                              _qgeometry_table_poly='True',
                              _qgeometry_table_junction='True')
    """Component metadata"""

    TOOLTIP = """Simple Metal Transmon Cross."""

    ##############################################MAKE######################################################

    def make(self):
        """This is executed by the GUI/user to generate the qgeometry for the
        component."""
        self.make_pocket()
        self.make_connection_pads()

###################################TRANSMON#############################################################

    def make_pocket(self):
        """Makes a basic Crossmon, 4 arm cross."""

        # self.p allows us to directly access parsed values (string -> numbers) form the user option
        p = self.p

        width = p.cross_width
        cross_width = width
        cross_length = p.cross_length
        cross_gap = p.cross_gap
        resolution = p.resolution
        radius = p.cross_radius
        cross_radius = radius

        #parameters for the central cross
        max_len = cross_length*2
        height = cross_length-cross_width/2

        #parameters for the etched pocket
        max_len_etch = cross_length*2 + cross_gap*2
        radius_etch = radius + cross_gap
        height_etch = cross_length-cross_width/2 + cross_gap

        # access to chip name
        chip = p.chip

        # Creates the cross and the etch equivalent.
        # cross_line = draw.shapely.ops.unary_union([
        #     draw.LineString([(0, cross_length), (0, -cross_length)]),
        #     draw.LineString([(cross_length, 0), (-cross_length, 0)])
        # ])

        # cross = cross_line.buffer(cross_width / 2, cap_style=2)
        # cross_etch = cross.buffer(cross_gap, cap_style=3, join_style=2)

        center_metal = rec(max_len, width, same_radius = True, r = radius, resolution = resolution)
        center_metal_side = rec(width, height, same_radius = True, r = radius,  resolution = resolution, d3 = [-1,1], d4 = [1,1])
        center_metal_bot = draw.translate(center_metal_side, 0, -width/2-height/2,overwrite= True)
        center_metal_top = draw.rotate(center_metal_side, 180, overwrite = True)
        center_metal_top = draw.translate(center_metal_top, 0, width/2+height/2,overwrite= True)
        
        center_metal = draw.shapely.ops.unary_union([center_metal, center_metal_bot, center_metal_top])



        center_metal_etch = rec(max_len_etch, width+2*cross_gap,same_radius = True, r = radius_etch, resolution = resolution)
        center_metal_side_etch = rec(width+2*cross_gap, height+2*cross_gap, same_radius = True, r = radius_etch, resolution = resolution, d3 = [-1,1], d4 = [1,1])
        center_metal_bot_etch = draw.translate(center_metal_side_etch, 0, -width/2-height/2, overwrite= True)
        center_metal_top_etch = draw.rotate(center_metal_side_etch, 180, overwrite = True)
        center_metal_top_etch = draw.translate(center_metal_top_etch, 0, width/2+height/2,overwrite= True)
        center_metal_etch = draw.shapely.ops.unary_union([center_metal_etch, center_metal_bot_etch, center_metal_top_etch])
        # The junction/SQUID
        #rect_jj = draw.rectangle(cross_width, cross_gap)
        #rect_jj = draw.translate(rect_jj, 0, -cross_length-cross_gap/2)
        rect_jj = draw.LineString([(0, -cross_length),
                                   (0, -cross_length - cross_gap)])
        

        if p.junction == 'True':
            cut_out = draw.rectangle(p.inductor_width/4, p.jj_pocket_extent/4)
            cut_out_big = draw.rectangle(p.inductor_width/2, p.jj_pocket_extent/4)
            cut_out_big = draw.translate(cut_out_big, 0, p.jj_pocket_extent/4)
            cutout = draw.shapely.ops.unary_union([cut_out, cut_out_big])
            
            cutout_top = draw.translate(cutout,0,-p.cross_length)
            cutout_bot = draw.rotate(cutout, 180, origin=(0,0))
            cutout_bot = draw.translate(cutout_bot,0,-p.cross_length-p.cross_gap)

            center_metal = center_metal.difference(cutout_top)
            center_metal_etch = draw.shapely.ops.unary_union([center_metal_etch, cutout_bot])

        #rotate and translate
        polys = [center_metal, center_metal_top, center_metal_bot, center_metal_etch, center_metal_top_etch, center_metal_bot_etch, rect_jj]
        polys = draw.rotate(polys, p.orientation, origin=(0, 0))
        polys = draw.translate(polys, p.pos_x, p.pos_y)

        [center_metal, center_metal_top, center_metal_bot, center_metal_etch, center_metal_top_etch, center_metal_bot_etch, rect_jj] = polys

        # generate qgeometry
        self.add_qgeometry('poly', dict(cross=center_metal), chip=chip)
        self.add_qgeometry('poly', dict(center_metal_etch=center_metal_etch), chip=chip, subtract=True)
        
        # self.add_qgeometry('poly',
        #                    dict(cross_etch=cross_etch),
        #                    subtract=True,
        #                    chip=chip)
        if p.junction == 'False':
            self.add_qgeometry('junction',
                           dict(rect_jj=rect_jj),
                           width=cross_width,
                           chip=chip)


############################CONNECTORS##################################################################################################

    def make_connection_pads(self):
        """Goes through connector pads and makes each one."""
        for name in self.options.connection_pads:
            self.make_connection_pad(name)

    def make_connection_pad(self, name: str):
        """Makes individual connector pad.

        Args:
            name (str) : Name of the connector pad
        """

        # self.p allows us to directly access parsed values (string -> numbers) form the user option
        p = self.p
        cross_width = p.cross_width
        cross_length = p.cross_length
        cross_gap = p.cross_gap
        resolution = p.resolution

        # access to chip name
        chip = p.chip

        pc = self.p.connection_pads[name]  # parser on connector options
        c_g = pc.claw_gap
        c_l = pc.claw_length
        c_w = pc.claw_width
        g_s = pc.ground_spacing
        con_loc = pc.connector_location
        c_r = pc.claw_radius

        

        if pc.connector_type == 0:  # Claw connector
            cr = min(c_r, c_w / 2)
            claw_cpw = rec(c_w*3, c_w, resolution = resolution, d3 = [1,-1], d2 = [1,1], r3 = c_r, r2 = c_r)
            claw_cpw = draw.translate(claw_cpw, -c_w*3/2, 0, overwrite = True)
            claw_cpw_etch = rec(c_w*3 , c_w+2*c_g, resolution = resolution, d3 = [1,-1], d2 = [1,1], r3 = c_r, r2 = c_r)
            claw_cpw_etch = draw.translate(claw_cpw_etch, -c_w*3/2-c_g, 0, overwrite = True)

            t_claw_height = 2*c_g + 2 * c_w + 2*g_s + 2*cross_gap + cross_width

            r0 = p.cross_radius
            r1 = r0 + cross_gap
            r2 = r1 + g_s +c_g
            r3 = r2 + c_w 

            # r1 = min(r1, cross_width/2+cross_gap)
            r2 = min(r2, t_claw_height/2 - c_w*2, c_l -c_w)
            r3 = min(r3, t_claw_height/2 - c_w , c_l)


            claw_base = rec(c_l + c_w, t_claw_height, resolution = resolution, 
                            r1 = r3, r2 = c_r, r3 = c_r, r4 = r3)
            # claw_base = draw.translate(claw_base, (c_l + c_w)/2, 0, overwrite = True)
            claw_subtract = rec(c_l, t_claw_height-2*c_w, resolution = resolution,
                                r1 = r2, r2 = c_r, r3 = c_r, r4 = r2, d2 = [1,1], d3 = [1,-1])
            claw_subtract = draw.translate(claw_subtract, c_w/2, 0, overwrite = True)
            claw_base = claw_base.difference(claw_subtract)
            claw_base = draw.translate(claw_base, c_l/2+c_w/2, 0, overwrite = True)
            
            r2 -= c_g
            r3 += c_g
            c_r += c_g

            r2 = min(r2, t_claw_height/2 - c_w*2, c_l -c_w)
            r3 = min(r3, t_claw_height/2 - c_w , c_l)

            l = c_l + c_w +2*c_g
            lp = l - c_w - 2*c_g
            claw_base_etch = rec(l, t_claw_height+2*c_g, resolution = resolution, 
                            r1 = r3, r2 = c_r, r3 = c_r, r4 = r3)
            claw_base_etch = draw.translate(claw_base_etch, -l/2, 0, overwrite = True)

            claw_subtract_etch = rec(lp, t_claw_height-2*c_w-2*c_g, resolution = resolution,
                                r1 = r2, r2 = c_r, r3 = c_r, r4 = r2, d2 = [1,1], d3 = [1,-1])
            claw_subtract_etch = draw.translate(claw_subtract_etch, -lp/2, 0, overwrite = True)
            claw_base_etch = claw_base_etch.difference(claw_subtract_etch)
            # draw.box(-c_w, -(t_claw_height) / 2, c_l,
            #                      t_claw_height / 2)
            
            claw_base_etch = draw.translate(claw_base_etch, l-c_g, 0, overwrite = True)

            connector_arm = draw.shapely.ops.unary_union([claw_base, claw_cpw])
            connector_etcher = draw.shapely.ops.unary_union([claw_base_etch, claw_cpw_etch])
            components = [connector_arm, connector_etcher]
            connector_arm, connector_etcher = draw.translate(components, -c_g - g_s,0, overwrite = True)
            port_line = draw.LineString([(-4 * c_w +(c_w-0.01), -c_w / 2), (-4 * c_w+(c_w-0.01), c_w / 2)])
        else:
            claw_cpw = draw.box(0, -c_w / 2, -4 * c_w, c_w / 2)
            connector_arm = claw_cpw
            connector_etcher = draw.buffer(connector_arm, c_g)
            port_line = draw.LineString([(-4 * c_w, -c_w / 2), (-4 * c_w, c_w / 2)])

        # Making the pin for  tracking (for easy connect functions).
        # Done here so as to have the same translations and rotations as the connector. Could
        # extract from the connector later, but since allowing different connector types,
        # this seems more straightforward.
        # port_line = draw.LineString([(-4 * c_w, -c_w / 2), (-4 * c_w, c_w / 2)])

        claw_rotate = 0
        if con_loc > 135:
            claw_rotate = 180
        elif con_loc > 45:
            claw_rotate = -90

        # Rotates and translates the connector polygons (and temporary port_line)
        polys = [connector_arm, connector_etcher, port_line]
        polys = draw.translate(polys, -(cross_length + cross_gap + g_s + c_g),
                               0)
        polys = draw.rotate(polys, claw_rotate, origin=(0, 0))
        polys = draw.rotate(polys, p.orientation, origin=(0, 0))
        polys = draw.translate(polys, p.pos_x, p.pos_y)
        [connector_arm, connector_etcher, port_line] = polys

        # Generates qgeometry for the connector pads
        self.add_qgeometry('poly', {f'{name}_connector_arm': connector_arm},
                           chip=chip)
        self.add_qgeometry('poly',
                           {f'{name}_connector_etcher': connector_etcher},
                           subtract=True,
                           chip=chip)
        self.add_pin(name, port_line.coords, c_w)



def rec(width, height, r1=0,r2 = 0,r3 = 0,r4 = 0, resolution = 5,d1 = [-1,-1],d2 = [1,-1],d3 = [1,1],d4 = [-1,1], same_radius = False, r = 5):
    directions = np.array([[-1,-1],[1,-1],[1,1],[-1,1]])
    if same_radius:
        radius = np.array([r,r,r,r])
    else:
        radius = np.array([r1,r2,r3,r4])
    d = np.array([d1,d2,d3,d4])
    x = np.array([-width/2, width/2, width/2, -width/2])
    y = np.array([-height/2, -height/2, height/2, height/2])
    radius = np.array(radius)
    coords = []
    for i in range(len(x)):
        if radius[i] == 0:
            coord = np.array([[x[i],y[i]]])
        else:
            xx = x[i]-directions[i][0]*radius[i]
            yy = y[i]-directions[i][1]*radius[i]
            diff = directions[i]-d[i]
            xx = xx + diff[0]*radius[i]
            yy = yy + diff[1]*radius[i]
            
            coord = ((round_corners(xx,yy,direction = d[i], radius = radius[i], n_points = resolution)))
            inds = np.argsort(-coord[:,0]*directions[i][1]*directions[i][0]*d[i][0])
            coord = coord[inds]
        if i == 0:
            coords = coord
        else:
            coords = np.concatenate((coords, coord))

    rounded_rec = draw.Polygon(coords)
    return rounded_rec

def round_corners(x,y,direction, radius, n_points = 5):
    xi, yi = direction
    pts = [(xi*radius * np.cos(np.pi/2 * x / n_points),
                                yi*radius * np.sin(np.pi/2 * x / n_points)) for x in range(int(n_points+1))]
    # if (xi*yi<0) or flip:
    #     pts = pts[::-1]
    x_corner = x#-radius*xi
    y_corner = y#-radius*yi
    pts = np.array(pts)
    coords = pts +np.array([x_corner,y_corner])
    
    return coords