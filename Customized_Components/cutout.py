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


class Cutout(QComponent):
    """A rrectangle with rounded corners.

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
        * subtract: 'True'
    """

    default_options = dict(
        pos_x = '0um',
        pos_y = '0um',
        width = '300um',
        height = '100um',
        subtract='True',
        heler = 'False')
    """Default drawing options"""

    TOOLTIP = """A single rectangle with rounded corners"""

    def make(self):
        """The make function implements the logic that creates the geoemtry
        (poly, path, etc.) from the qcomponent.options dictionary of
        parameters, and the adds them to the design, using
        qcomponent.add_qgeometry(...), adding in extra needed information, such
        as layer, subtract, etc."""
        p = self.p

        x = p.pos_x
        y = p.pos_y
        w = p.width
        h = p.height
        rect = draw.Polygon([(x-w/2, y-h/2),(x+w/2, y-h/2), (x+w/2, y+h/2), (x-w/2, y+h/2)])


        
        # add qgeometry
        self.add_qgeometry('poly', {'Rounded_Rec': rect},
                           subtract=p.subtract,
                           helper=p.helper,
                           layer=p.layer,
                           chip=p.chip)
        
