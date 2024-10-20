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
"""This is the CircleCaterpillar module."""

from qiskit_metal import draw, Dict  # , QComponent
from qiskit_metal.qlibrary.core import QComponent
#from qiskit_metal import is_true
from shapely.geometry import CAP_STYLE, JOIN_STYLE
import numpy as np


class RoundedRectangle(QComponent):
    """A rectangle with rounded corners.

    Inherits QComponent class.

    # .. image::
    #     CircleRaster.png

    # .. meta::
    #     Circle Raster

    Default Options:
        * pos_x: '0um'
        * pos_y: '0um' 
        * width: '200 um'
        * height: '200 um' 
        * radius: '50 um'
        * resolution: '5'
        * connection: 'False' -- if this rectangle is for making connection with others, the radius will point another way
        * connection_radius: '10um'
        * connection_direction: '180' -- clockwise direction w.r.t. vertical upwards
        * cap_style: 'round' -- Valid options are 'round', 'flat', 'square'
        * subtract: 'False'
        * helper: 'False'
    """

    default_options = dict(
        pos_x = '0um',
        pos_y = '0um',
        width = '200um',
        height = '200um',
        radius ='50um',
        resolution ='5',
        cap_style='round',
        connection = False,
        connection_radius = '10um',
        connection_direction = -180,    
        # round, flat, square
        # join_style = 'round', # round, mitre, bevel
        # General
        subtract='False',
        helper='False')
    """Default drawing options"""

    TOOLTIP = """A single rectangle with rounded corners"""

    def make(self):
        """The make function implements the logic that creates the geoemtry
        (poly, path, etc.) from the qcomponent.options dictionary of
        parameters, and the adds them to the design, using
        qcomponent.add_qgeometry(...), adding in extra needed information, such
        as layer, subtract, etc."""
        p = self.p  # p for parsed parameters. Access to the parsed options.
        n = p.resolution
        radius = min(p.radius,p.height/2,p.width/2)
        if p.radius>max(p.height/2,p.width/2):
            print('Error: radius is too big. Will show up as circle')

        # create the geometry
        if p.connection:
            for i, (xi,yi) in enumerate([(-1,1),(1,1)]):
                pts = [(-xi*radius * np.cos(np.pi/2 * x / n),
                                yi*radius * np.sin(np.pi/2 * x / n)) for x in range(int(n+1))]
                if xi*yi>0:
                    pts = pts[::-1]
                x_corner = p.width/2*xi+radius*xi
                y_corner = p.height/2*yi-radius*yi
                pts = np.array(pts)
                coords = pts +np.array([x_corner,y_corner])
                index = None
                index = coords if i == 0 else np.concatenate((index,coords))
            index = np.concatenate((index,np.array([[p.width/2,-p.height/2],[-p.width/2,-p.height/2]])))

        else:
            for i,(xi,yi) in enumerate([(1,1),(-1,1),(-1,-1),(1,-1)]):
                pts = [(xi*radius * np.cos(np.pi/2 * x / n),
                                yi*radius * np.sin(np.pi/2 * x / n)) for x in range(int(n+1))]
                if xi*yi<0:
                    pts = pts[::-1]
                # pts += [(0,0)]
                x_corner = p.width/2*xi-radius*xi
                y_corner = p.height/2*yi-radius*yi
                pts = np.array(pts)
                coords = pts +np.array([x_corner,y_corner])
                # coords = list(coords)
                index = coords if i == 0 else np.concatenate((index,coords))
                        # print(index)

        rounded_rec = draw.Polygon(index)

        if p.connection:
            rounded_rec = draw.rotate(rounded_rec,p.connection_direction,overwrite= True, origin=(0,0))
        rounded_rec = draw.translate(rounded_rec,p.pos_x,p.pos_y,overwrite= True)
        # add qgeometry
        self.add_qgeometry('poly', {'Rounded_Rec': rounded_rec},
                           subtract=p.subtract,
                           helper=p.helper,
                           layer=p.layer,
                           chip=p.chip)
        
def rounded_rec_only(width, height, radius, resolution = 5, connection = False,connection_direction = 180):
    """_summary_

    Args:
        width (_type_): the size of the rectangle in x direction
        height (_type_): the size of the rectangle in y direction
        radius (_type_): the radius of the rounded corner
        resolution (int, optional): number of points making up the rounded corner. Defaults to 5.
        connection (bool, optional): if the rectangle connects to a different rectangle, check this. Defaults to False.
        connection_direction (int, optional): which direction the connection is to. Rotation counter clockwise starting from pos x axis. Defaults to 180.

    Returns:
        _type_: Polygon object
    """
    
    radius = min(radius,height/2,width/2)
    if radius>max(height/2,width/2):
        print('Error: radius is too big. Will show up as circle')
    n = resolution
    # create the geometry
    if connection:
        for i, (xi,yi) in enumerate([(-1,1),(1,1)]):
            pts = [(-xi*radius * np.cos(np.pi/2 * x / n),
                            yi*radius * np.sin(np.pi/2 * x / n)) for x in range(int(n+1))]
            if xi*yi>0:
                pts = pts[::-1]
            x_corner = width/2*xi+radius*xi
            y_corner = height/2*yi-radius*yi
            pts = np.array(pts)
            coords = pts +np.array([x_corner,y_corner])
            index = None
            index = coords if i == 0 else np.concatenate((index,coords))
        index = np.concatenate((index,np.array([[width/2,-height/2],[-width/2,-height/2]])))

    else:
        for i,(xi,yi) in enumerate([(1,1),(-1,1),(-1,-1),(1,-1)]):
            pts = [(xi*radius * np.cos(np.pi/2 * x / n),
                            yi*radius * np.sin(np.pi/2 * x / n)) for x in range(int(n+1))]
            if xi*yi<0:
                pts = pts[::-1]
            # pts += [(0,0)]
            x_corner = width/2*xi-radius*xi
            y_corner = height/2*yi-radius*yi
            pts = np.array(pts)
            coords = pts +np.array([x_corner,y_corner])
            # coords = list(coords)
            index = coords if i == 0 else np.concatenate((index,coords))
                    # print(index)

    rounded_rec = draw.Polygon(index)

    if connection:
        rounded_rec = draw.rotate(rounded_rec,connection_direction,overwrite= True, origin=(0,0))
    return rounded_rec
    # rounded_rec = draw.translate(rounded_rec,p.pos_x,p.pos_y,overwrite= True)
def rounded_rec(width, height, r1=0,r2 = 0,r3 = 0,r4 = 0, resolution = 5,d1 = [-1,-1],d2 = [1,-1],d3 = [1,1],d4 = [-1,1], same_radius = False, r = 5):
    """Generate customized rounded rectangle with different radius and rounded corners to face different directions. 
    the order of corners is from the same naming as quadrants in a cartesian plane.
    Args:
        width (_type_): the size of the rectangle in y direction
        height (_type_): the size of the rectangle in x direction
        r1 (int, optional): radius of the first rounded corner. Defaults to 0.
        r2 (int, optional): radius of the second rounded corner. Defaults to 0.
        r3 (int, optional): radius of the third rounded corner.. Defaults to 0.
        r4 (int, optional): radius of the fourth rounded corner.. Defaults to 0.
        resolution (int, optional): the number of points that makes up the rounded corner. Defaults to 5.
        d1,d2,d3,d4: the direction of the corner, the direction is where the center of circle is facing w.r.t. the line. [x direction, y direction] +1 means positive axis direction, -1 means negative axis direction.
        d1 (list, optional): direction of corner 1. Defaults to [-1,-1].
        d2 (list, optional): direction of corner 2. Defaults to [1,-1].
        d3 (list, optional): direction of corner 3. Defaults to [1,1].
        d4 (list, optional): direction of corner 4. Defaults to [-1,1].
        same_radius (bool, optional): True of the corners have the same radius. Defaults to False.
        r (int, optional): if the corners have same radius, then this sets the radius. Defaults to 5.

    Returns:
        _type_: Polygon object
    """
    
    directions = np.array([[-1,-1],[1,-1],[1,1],[-1,1]])
    radius = np.array([r,r,r,r]) if same_radius else np.array([r1,r2,r3,r4])
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
        coords = coord if i == 0 else np.concatenate((coords, coord))
    return draw.Polygon(coords)

def round_corners(x,y,direction, radius, n_points = 5):
    xi, yi = direction
    pts = [(xi*radius * np.cos(np.pi/2 * x / n_points),
                                yi*radius * np.sin(np.pi/2 * x / n_points)) for x in range(int(n_points+1))]
    # if (xi*yi<0) or flip:
    #     pts = pts[::-1]
    x_corner = x#-radius*xi
    y_corner = y#-radius*yi
    pts = np.array(pts)
    return pts +np.array([x_corner,y_corner])