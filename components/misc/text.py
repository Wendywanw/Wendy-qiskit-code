

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
"""Dolan Junction."""

import numpy as np
import gdspy
import astropy.units as u
from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary.core import QComponent

from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union



class Text_object(QComponent):
    """A dose array coponent 

    Inherits QComponent class.

    # .. meta::
    #     Circle Raster

    Default Options:
        * chip = 'main'
        * pos_x: '0um' -- x position of the center
        * pos_y: '0um' -- y position of the center
        * pad_width: '20 um' -- width of the big pads that connect to the transmon
        * pad_height: '30 um' -- height of the big pads that connect to the transmon
        * total_length: '80 um' -- total length of the junction, including the pads
        * Lj: '10 nH' -- inductance of the junction
        * resolution: '5' -- number of points used to draw the rounded rectangle
        * Fillet: '5 um' -- radius of the fillet/rounded corners
        * fat_finger_width: '6 um' -- width of the fat finger, i.e. the part that tapers down to the junction finger
        * Jc: '0.1' -- critical current density of the junction
        * rotation: '0' -- rotation of the junction
        * layer: '0' -- layer of the junction
        * area_layer: '1' -- layer of the area that defines the junction
        * area: 'False' -- whether to draw the area that defines the junction
    """
    default_options = Dict(
        pos_x = '0um', 
        pos_y = '0um',
        text = 'haha',
        text_height = '200 um',
        orientation = '0',
        layer = '0',
        subtract = False,
        )
    """Default drawing options"""

    component_metadata = Dict(short_name='Text',
                              _qgeometry_table_path='True',
                              _qgeometry_table_poly='True',
                              _qgeometry_table_junction='False')
    """Component metadata"""

    TOOLTIP = """A text object"""

    def make(self):
        """Define the way the options are turned into QGeometry.

        The make function implements the logic that creates the geoemtry
        (poly, path, etc.) from the qcomponent.options dictionary of
        parameters, and the adds them to the design, using
        qcomponent.add_qgeometry(...), adding in extra needed
        information, such as layer, subtract, etc.
        """
        """Making the dolan junction."""
        p = self.p

        # extract chip name
        chip = p.chip

        # since we will reuse these options, parse them once and define them as varaibles
        text = self.options['text']
        position = (p.pos_x, p.pos_y)
        text_height = p.text_height
        dummy_layer = 0
        
        text_element = gdspy.Text(text, text_height, position, layer=dummy_layer)
        text_polygons = text_element.polygons
        
        poly = [Polygon(polygon) for polygon in text_polygons]
        
        
        # w_pocket = p.w_pocket
        # h_pocket = p.h_pocket
        # w_pad = p.w_pad
        # h_pad = p.h_pad
        # pad_gap = p.pad_gap

        # pocket = rec2(w_pocket, h_pocket)
        # pad = rec2(w_pad, h_pad)

        # pad_left = draw.translate(pad, -w_pad/2-pad_gap/2, 0)
        # pad_right = draw.translate(pad, w_pad/2 + pad_gap/2, 0)

        # all = draw.union(pad_left, pad_right)
        # cut = pocket

        poly = draw.rotate(poly, p.orientation, origin=position)
        # all, cut = draw.translate(components, p.pos_x, p.pos_y)
        poly_final = unary_union(poly)
        
        
        # Use the geometry to create Metal qgeometry
        self.add_qgeometry('poly',
                           dict(poly_final=poly_final),
                           chip=chip, layer = p.layer, subtract = p.subtract)

        # self.add_qgeometry('poly', dict(cut = cut), 
        #                    subtract=True, layer=p.layer,
        #                    chip=chip)

