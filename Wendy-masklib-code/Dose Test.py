# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 09:54:15 2021

@author: ziqian
"""
path = '/Users/wendy/_Lib'

import sys
sys.path.append(path)

from slab.circuits import *
from slab.mp_components import *

import os, time, sys
import subprocess
from time import sleep
import numpy as np
from matplotlib import pyplot as plt
import csv
import matplotlib as mpl
import datetime as dt

plt.close('all')

# CHIPNAME = "UC"  # dt.datetime.today().strftime("%Y%m%d") #+ "ParaAmp"
today = time.strftime('%Y%m%d')
author = ''

# Only change these two variables!!
pad_layer = 0
junction_layer = 1

# I don't know why it works...
if pad_layer == 1 and junction_layer == 0:
    draw_layer1 = 1
    draw_layer2 = 0
    draw_layer3 = 1

if junction_layer == 1 and pad_layer == 0:
    draw_layer1 = 0
    draw_layer2 = 1
    draw_layer3 = 1

if pad_layer == 1 and junction_layer == 1:
    draw_layer1 = 1
    draw_layer2 = 1
    draw_layer3 = 1

show_structure = 0
show_wafer = 1
two_layer = 1
perf = False
solid = 0
square = 0
etching = True  # False if a bare wafer is used
open_dwgviewer = False
open_klayout = True

if draw_layer1 == 1:
    MaskName = ""
else:
    MaskName = " "  # MaskName not needed for junction mask

if draw_layer1 == 1 and draw_layer2 == 0:
    two_layer = 0
elif draw_layer1 == 0 and draw_layer3 == 1:
    two_layer = 0
else:
    two_layer = 1

if junction_layer == 1:
    two_layer = 1
# Don't change anything above!

### CPW Parameters
cpw_length = 10
cpw_pinw = 10.0
cpw_rad = 50
taperl = 50
eps_eff = (1. + 10.4) / 2.
cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)
flux_pinw = 3.5
flux_gapw = calculate_gap_width(eps_eff, 50, flux_pinw) + 0.21

### JPA capacitor parameters
cap_botm_y = 40
cap_botm_x = 140
cap_top_y = 120
cap_top_x = 80
cap_sep = 11
con_pin_l = 50.

junc_pad_y = 6.5

print(cpw_gapw)

chip_names = list()
chanstarts = list()

### Close DWG Viewer & KLayout
if open_dwgviewer:
    subprocess.Popen(r'taskkill /F /im "dwgviewr.exe"')
if open_klayout:
    subprocess.Popen(r'taskkill /F /im "klayout_app.exe"')


def TransPads2(structure, center_pt=(0, 0), padw=500.0, padh=200.0, taperw=40.0, leadw=437.5, leadh=20.0, qugap=45.0):
    s = structure
    #    s/.two_layer = 0
    s.last = center_pt
    s.last_direction = 90.0

    start_pt = (center_pt[0] - qugap / 2. - leadw - taperw - padw, center_pt[1])
    s.last = start_pt
    CPWStraight(s, padw, pinw=0., gapw=padh / 2.)
    CPWLinearTaper(s, taperw, start_pinw=0.0, stop_pinw=0.0, start_gapw=padh / 2., stop_gapw=leadh / 2.)
    CPWStraight(s, leadw, pinw=0.0, gapw=leadh / 2.)

    return_pt = s.last
    return_dir = s.last_direction

    s.last_direction += 180
    CPWLinearTaper(s, 3.0, start_pinw=0.0, stop_pinw=0.0, start_gapw=leadh / 2. * 0.15, stop_gapw=leadh / 2. * 0.35)

    s.last = (return_pt[0], return_pt[1] + qugap)
    s.last_direction = return_dir

    return_pt = s.last
    # s.last_direction+=180
    CPWLinearTaper(s, 3.0, start_pinw=0.0, stop_pinw=0.0, start_gapw=leadh / 2. * 0.15, stop_gapw=leadh / 2. * 0.35)

    s.last = return_pt
    # s.last_direction+=180
    CPWStraight(s, leadw, pinw=0.0, gapw=leadh / 2.)
    CPWLinearTaper(s, taperw, start_pinw=0.0, stop_pinw=0.0, start_gapw=leadh / 2., stop_gapw=padh / 2.)
    CPWStraight(s, padw, pinw=0., gapw=padh / 2.)


def struct_startings_10mm(chip):
    struct_starting = list()

    struct_starting.append((800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 1))
    struct_starting.append((800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 2))
    struct_starting.append((800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 3))

    struct_starting.append((chip.size[0] / 2, chip.size[1] - 800))

    struct_starting.append((chip.size[0] - 800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 3))
    struct_starting.append((chip.size[0] - 800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 2))
    struct_starting.append((chip.size[0] - 800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 1))
    struct_starting.append((chip.size[0] - 800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 0))

    struct_starting.append((chip.size[0] / 2, 800))

    struct_starting.append((800, 1200 + (chip.size[1] - 1200 * 2) / 3 * 0))

    return struct_starting


def chipInit_10mm(chip, defaults):
    """
    This makes the launch pads on the chip. Input is an object c, which is the chip.
    From the launch pads, we can make connections on the chip.
    """
    # The following creates 8 launch pads on the chip. There are 3 pads per side, two
    # in each of the corners and then one in the middle of each side.

    struct_starting = struct_startings_10mm(chip)

    setattr(chip, 's0', Structure(chip, start=struct_starting[0], direction=0, defaults=defaults, layer='0'))
    setattr(chip, 's1', Structure(chip, start=struct_starting[1], direction=0, defaults=defaults, layer='0'))
    setattr(chip, 's2', Structure(chip, start=struct_starting[2], direction=0, defaults=defaults, layer='0'))
    setattr(chip, 's3', Structure(chip, start=struct_starting[3], direction=270, defaults=defaults, layer='0'))
    setattr(chip, 's4', Structure(chip, start=struct_starting[4], direction=180, defaults=defaults, layer='0'))
    setattr(chip, 's5', Structure(chip, start=struct_starting[5], direction=180, defaults=defaults, layer='0'))
    setattr(chip, 's6', Structure(chip, start=struct_starting[6], direction=180, defaults=defaults, layer='0'))
    setattr(chip, 's7', Structure(chip, start=struct_starting[7], direction=180, defaults=defaults, layer='0'))
    setattr(chip, 's8', Structure(chip, start=struct_starting[8], direction=90, defaults=defaults, layer='0'))
    setattr(chip, 's9', Structure(chip, start=struct_starting[9], direction=0, defaults=defaults, layer='0'))


def draw_launchers_10mm(chip, chip_defaults, pinw, gapw, exclude=[]):
    chipInit_10mm(chip, defaults=chip_defaults)

    for k in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:

        if k in exclude:
            pass
        else:
            Launcher(vars(vars()['chip'])['s%d' % k], pinw=pinw, gapw=gapw, flipped=False, pad_length=250 + 50,
                     taper_length=150, pad_to_length=350, )


def set_mask_init():
    ### Setting defaults
    d = ChipDefaults()
    d.Q = 1000
    d.radius = 50
    d.segments = 6
    d.pinw_rsn = 2.  # this is the resonator pinwitdth that we are goign to use.
    d.gapw_rsn = 8.5

    d.pinw = 1.5  # d.pinw
    d.gapw = 1.
    d.center_gapw = 1
    ### Now calculate impedance
    d.imp_rsn = 80.  # calculate_impedance(d.pinw_rsn,d.gapw_rsn,d.eps_eff)
    d.solid = True
    return d


def chipInit(c, defaults):
    """
    This makes the launch pads on the chip. Input is an object c, which is the chip.
    From the launch pads, we can make connections on the chip.
    """
    # The following creates 8 launch pads on the chip. There are 3 pads per side, two
    # in each of the corners and then one in the middle of each side.

    setattr(c, 's0',
            Structure(c, start=(c.size[0] / 2 - 1900 - 800-100+100+100, c.size[1] / 2 - 800 - 5.), direction=-90, defaults=defaults,
                      layer='0'))
    setattr(c, 's1',
            Structure(c, start=(c.size[0] / 2 - 1900 - 800-100+100+100, c.size[1] / 2 + 1000 + 450), direction=-90, defaults=defaults,
                      layer='0'))
    setattr(c, 's2',
            Structure(c, start=(c.size[0] / 2 - 1900, c.size[1] - 600+100-100), direction=270, defaults=defaults, layer='0'))
    setattr(c, 's3',
            Structure(c, start=(c.size[0] / 2 - 9, c.size[1] - 600+100-100), direction=270, defaults=defaults, layer='0'))
    setattr(c, 's4',
            Structure(c, start=(c.size[0] / 2 + 1900+200, c.size[1] - 600+100-100), direction=180, defaults=defaults, layer='0'))
    setattr(c, 's5',
            Structure(c, start=(c.size[0] / 2 + 1900 + 800+100-100-100, c.size[1] / 2 + 1000 + 450), direction=-90, defaults=defaults,
                      layer='0'))
    setattr(c, 's6',
            Structure(c, start=(c.size[0] / 2 + 1900 + 800+100-100-100, c.size[1] / 2 - 800), direction=-90, defaults=defaults,
                      layer='0'))
    setattr(c, 's7', Structure(c, start=(c.size[0] / 2 + 1900+200, 800-100+100), direction=180, defaults=defaults, layer='0'))
    setattr(c, 's8', Structure(c, start=(c.size[0] / 2, 800-100+100), direction=90, defaults=defaults, layer='0'))
    setattr(c, 's9', Structure(c, start=(c.size[0] / 2 - 1900-200, 800-100+100), direction=0, defaults=defaults, layer='0'))


def draw_launchers(c, d, exclude=[]):
    chipInit(c, defaults=d)

    for k in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:

        if k in exclude:
            pass
        else:
            if k==k:
                Launcher(vars(vars()['c'])['s%d' % k], pinw=cpw_pinw, gapw=cpw_gapw, launcher_pinw=150, launcher_gapw=75)
            else:
                Launcher(vars(vars()['c'])['s%d' % k], pinw=cpw_pinw, gapw=cpw_gapw, launcher_pinw=300,
                         launcher_gapw=150)


def cover_launchers(c, d, exclude=[], h=500, w=400):
    """
    Cover the launchers with a square so that we can wirebond to the pads on the chip.
    """

    # taper_length = 250
    # taper_to_width = 2 * 50 + 20
    #
    # s = Structure(c, start=c.top_midpt, direction=270, defaults=d)
    #
    # if not (1 in exclude):  # middle, top
    #     lo_left = (c.top_midpt[0] - w / 2., c.top_midpt[1] - (h - taper_length))
    #     lo_right = (c.top_midpt[0] + w / 2., c.top_midpt[1] - (h - taper_length))
    #     tp_left = (c.top_midpt[0] - w / 2., c.top_midpt[1])
    #     tp_right = (c.top_midpt[0] + w / 2., c.top_midpt[1])
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    #     tp_left = lo_left
    #     tp_right = lo_right
    #     midx = (lo_left[0] + lo_right[0]) / 2.
    #     midy = tp_left[1] - taper_length
    #     lo_left = (midx - taper_to_width / 2., midy)
    #     lo_right = (midx + taper_to_width / 2., midy)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    # if not (2 in exclude):  # middle, bottom
    #     lo_left = (c.bottom_midpt[0] - w / 2., c.bottom_midpt[1])
    #     lo_right = (c.bottom_midpt[0] + w / 2., c.bottom_midpt[1])
    #     tp_left = (c.bottom_midpt[0] - w / 2., c.bottom_midpt[1] + (h - taper_length))
    #     tp_right = (c.bottom_midpt[0] + w / 2., c.bottom_midpt[1] + (h - taper_length))
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))
    #
    #     lo_left = tp_left
    #     lo_right = tp_right
    #     midx = (lo_left[0] + lo_right[0]) / 2.
    #     midy = tp_left[1] + taper_length
    #     tp_left = (midx - taper_to_width / 2., midy)
    #     tp_right = (midx + taper_to_width / 2., midy)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    # if not (3 in exclude):  # Left, middle
    #     lo_left = (c.left_midpt[0], c.left_midpt[1] - w / 2.)
    #     lo_right = (c.left_midpt[0] + (h - taper_length), c.left_midpt[1] - w / 2.)
    #     tp_left = (c.left_midpt[0], c.left_midpt[1] + w / 2.)
    #     tp_right = (c.left_midpt[0] + (h - taper_length), c.left_midpt[1] + w / 2.)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))
    #
    #     lo_left = lo_right
    #     tp_left = tp_right
    #     midx = tp_left[0] + taper_length
    #     midy = (lo_left[1] + tp_left[1]) / 2.
    #     tp_right = (midx, midy + taper_to_width / 2.)
    #     lo_right = (midx, midy - taper_to_width / 2.)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    # if not (4 in exclude):  # Right, middle
    #     lo_left = (c.right_midpt[0] - (h - taper_length), c.right_midpt[1] - w / 2.)
    #     lo_right = (c.right_midpt[0], c.right_midpt[1] - w / 2.)
    #     tp_left = (c.right_midpt[0] - (h - taper_length), c.right_midpt[1] + w / 2.)
    #     tp_right = (c.right_midpt[0], c.right_midpt[1] + w / 2.)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))
    #
    #     lo_right = lo_left
    #     tp_right = tp_left
    #     midx = tp_left[0] - taper_length
    #     midy = (lo_left[1] + tp_left[1]) / 2.
    #     tp_left = (midx, midy + taper_to_width / 2.)
    #     lo_left = (midx, midy - taper_to_width / 2.)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    # if not (5 in exclude):  # Top, left
    #     lo_left = (c.top_left[0] - w / 2., c.top_left[1] - (h - taper_length))
    #     lo_right = (c.top_left[0] + w / 2., c.top_left[1] - (h - taper_length))
    #     tp_left = (c.top_left[0] - w / 2., c.top_left[1])
    #     tp_right = (c.top_left[0] + w / 2., c.top_left[1])
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))
    #
    #     tp_left = lo_left
    #     tp_right = lo_right
    #     midx = (lo_left[0] + lo_right[0]) / 2.
    #     midy = tp_left[1] - taper_length
    #     lo_left = (midx - taper_to_width / 2., midy)
    #     lo_right = (midx + taper_to_width / 2., midy)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    # if not (6 in exclude):  # Top, right
    #     lo_left = (c.top_right[0] - w / 2., c.top_right[1] - (h - taper_length))
    #     lo_right = (c.top_right[0] + w / 2., c.top_right[1] - (h - taper_length))
    #     tp_left = (c.top_right[0] - w / 2., c.top_right[1])
    #     tp_right = (c.top_right[0] + w / 2., c.top_right[1])
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))
    #
    #     tp_left = lo_left
    #     tp_right = lo_right
    #     midx = (lo_left[0] + lo_right[0]) / 2.
    #     midy = tp_left[1] - taper_length
    #     lo_left = (midx - taper_to_width / 2., midy)
    #     lo_right = (midx + taper_to_width / 2., midy)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    # if not (7 in exclude):  # Bottom, left
    #     lo_left = (c.bottom_left[0] - w / 2., c.bottom_left[1])
    #     lo_right = (c.bottom_left[0] + w / 2., c.bottom_left[1])
    #     tp_left = (c.bottom_left[0] - w / 2., c.bottom_left[1] + (h - taper_length))
    #     tp_right = (c.bottom_left[0] + w / 2., c.bottom_left[1] + (h - taper_length))
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))
    #
    #     lo_left = tp_left
    #     lo_right = tp_right
    #     midx = (lo_left[0] + lo_right[0]) / 2.
    #     midy = tp_left[1] + taper_length
    #     tp_left = (midx - taper_to_width / 2., midy)
    #     tp_right = (midx + taper_to_width / 2., midy)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))
    #
    # if not (8 in exclude):  # Bottom, right
    #     lo_left = (c.bottom_right[0] - w / 2., c.bottom_right[1])
    #     lo_right = (c.bottom_right[0] + w / 2., c.bottom_right[1])
    #     tp_left = (c.bottom_right[0] - w / 2., c.bottom_right[1] + (h - taper_length))
    #     tp_right = (c.bottom_right[0] + w / 2., c.bottom_right[1] + (h - taper_length))
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))
    #
    #     lo_left = tp_left
    #     lo_right = tp_right
    #     midx = (lo_left[0] + lo_right[0]) / 2.
    #     midy = tp_left[1] + taper_length
    #     tp_left = (midx - taper_to_width / 2., midy)
    #     tp_right = (midx + taper_to_width / 2., midy)
    #
    #     if solid:
    #         s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    #     else:
    #         s.append(sdxf.PolyLine([lo_left, tp_left, tp_right, lo_right, lo_left]))


def create_wirebond_border(c, solid, lo_left, lo_right, tp_left, tp_right):
    s = Structure(c, start=c.top_midpt, direction=270, defaults=d)

    # if solid:
    #     s.append(sdxf.Solid([lo_left, lo_right, tp_right, tp_left]))
    # else:
    #     s.append(sdxf.PolyLine([lo_left, lo_right, tp_right, tp_left, lo_left]))


def draw_chip_alignment_marks(solid, d, c):
    """
    Draw the alignment marks on the chip.
    """
    CrossShapeAlignmentMarks(Structure(c, start=(125, 125), direction=90, defaults=d), width=2,
                             armlength=120, solid=solid, layer='0')
    CrossShapeAlignmentMarks(Structure(c, start=(c.size[0] - 125, c.size[1] - 125), direction=90, defaults=d),
                             width=2, armlength=120, solid=solid, layer='0')
    CrossShapeAlignmentMarks(Structure(c, start=(c.size[0] - 125, 125), direction=90, defaults=d),
                             width=2, armlength=120, solid=solid, layer='0')
    CrossShapeAlignmentMarks(Structure(c, start=(125, c.size[1] - 125), direction=90, defaults=d),
                             width=2, armlength=120, solid=solid, layer='0')


def CoupPad(structure, padw=50.0, padl=100.0, girdle_l=0.0, corner_rad=10, connecw=20.0, connecl=50.0, gapw=20.0,
            connecgapw=10.0, coupstart=0, square=0):
    # padl-=padw

    if coupstart == 1:
        structure.move(connecl + padw + gapw + girdle_l)
        structure.last_direction += 180
    else:
        pass
    start_point = structure.last
    start_direction = structure.last_direction
    structure.move(connecl + padw + girdle_l + gapw / 2.)
    structure.move(padl / 2, structure.last_direction - 90)
    structure.last_direction -= 90
    CPWBendNew(structure, angle=-90, pinw=0, gapw=gapw / 2., radius=(padw + gapw) / 2., polyarc=1, segments=4,
               square=square)
    CPWStraight(structure, girdle_l, pinw=0, gapw=gapw / 2.)
    CPWBendNew(structure, angle=-90, pinw=0, gapw=gapw / 2., radius=(padw + gapw) / 2., polyarc=1, segments=4,
               square=square)
    structure.move((padw + gapw + girdle_l) / 2., structure.last_direction - 90)
    CPWTeeNew(structure, arml=padl, armw=padw + girdle_l, armgapw=gapw, corner_rad=corner_rad, stubl=connecl,
              stubw=connecw, stubgapw=connecgapw, couptype=0, square=square)
    structure.move((padw + gapw + girdle_l) / 2., structure.last_direction - 90)
    CPWBendNew(structure, angle=90, pinw=0, gapw=gapw / 2., radius=(padw + gapw) / 2., polyarc=1, segments=4,
               square=square)
    CPWStraight(structure, girdle_l, pinw=0, gapw=gapw / 2.)
    CPWBendNew(structure, angle=90, pinw=0, gapw=gapw / 2., radius=(padw + gapw) / 2., polyarc=1, segments=4,
               square=square)
    structure.last = start_point
    structure.last_direction = start_direction
    if coupstart == 1:
        structure.last_direction += 180
    else:
        structure.move(connecl + padw + gapw + girdle_l)


def CPWBendNew(structure, angle=90, pinw=10.0, gapw=20.0, radius=50.0, polyarc=1, segments=4, square=0):
    if square == 0:
        CPWBend(structure, angle, pinw=pinw, gapw=gapw, radius=radius, polyarc=polyarc, segments=segments)

    elif abs(angle) == 90:
        start_point = structure.last
        start_dir = structure.last_direction
        structure.move((gapw + pinw) / 2., structure.last_direction - (abs(angle) / angle) * 90)
        CPWStraight(structure, radius + gapw + pinw / 2., pinw=0, gapw=gapw / 2.)
        structure.last = start_point
        structure.move(radius + (gapw + pinw) / 2.)
        structure.move(pinw / 2., structure.last_direction - (abs(angle) / angle) * 90)
        structure.last_direction = structure.last_direction + (abs(angle) / angle) * 90
        CPWStraight(structure, pinw / 2. + radius, pinw=0, gapw=gapw / 2.)
        structure.last = start_point
        structure.last_direction = start_dir
        structure.move((gapw + pinw) / 2., structure.last_direction + (abs(angle) / angle) * 90)
        CPWStraight(structure, radius - pinw / 2., pinw=0, gapw=gapw / 2.)
        structure.move(-gapw / 2.)
        structure.move(gapw / 2., structure.last_direction - (abs(angle) / angle) * 90)
        structure.last_direction = structure.last_direction + (abs(angle) / angle) * 90
        CPWStraight(structure, radius - pinw / 2., pinw=0, gapw=gapw / 2.)
        structure.move((gapw + pinw) / 2., structure.last_direction - (abs(angle) / angle) * 90)

    elif abs(angle) == 180:
        start_point = structure.last
        start_dir = structure.last_direction
        structure.move((gapw + pinw) / 2., structure.last_direction - (abs(angle) / angle) * 90)
        CPWStraight(structure, radius + gapw + pinw / 2., pinw=0, gapw=gapw / 2.)
        structure.last = start_point
        structure.move(radius + (gapw + pinw) / 2.)
        structure.move(pinw / 2., structure.last_direction - (abs(angle) / angle) * 90)
        structure.last_direction = structure.last_direction + (abs(angle) / angle) * 90
        CPWStraight(structure, pinw + 2. * radius, pinw=0, gapw=gapw / 2.)
        structure.last = start_point
        structure.last_direction = start_dir
        structure.move((gapw + pinw) / 2, structure.last_direction + (abs(angle) / angle) * 90)
        CPWStraight(structure, radius - pinw / 2, pinw=0, gapw=gapw / 2)
        structure.move(-gapw / 2.)
        structure.move(gapw / 2., structure.last_direction - (abs(angle) / angle) * 90)
        structure.last_direction = structure.last_direction + (abs(angle) / angle) * 90
        CPWStraight(structure, 2. * radius - pinw, pinw=0, gapw=gapw / 2.)
        structure.move(-gapw / 2.)
        structure.move(gapw / 2., structure.last_direction - (abs(angle) / angle) * 90)
        structure.last_direction = structure.last_direction + (abs(angle) / angle) * 90
        CPWStraight(structure, radius - pinw / 2., pinw=0, gapw=gapw / 2.)
        structure.move(pinw + gapw, structure.last_direction - (abs(angle) / angle) * 90)
        structure.last_direction += 180
        CPWStraight(structure, radius + gapw + pinw / 2., pinw=0, gapw=gapw / 2.)
        structure.last_direction += 180
        structure.move(radius + gapw + pinw / 2.)
        structure.move((pinw + gapw) / 2., structure.last_direction + (abs(angle) / angle) * 90)

    else:
        print("this angle is not supported")


def CPWTeeNew(structure, arml=100.0, armw=20.0, armgapw=10.0, corner_rad=10.0, stubl=20.0, stubw=10.0, stubgapw=10.0,
              couptype=0, square=0):
    # couptype=0: input at one side of the arm
    # couptype=1: input at the other
    # couptype=2: input at the stub

    if couptype == 1:
        structure.move(arml)
        structure.last_direction += 180
    elif couptype == 2:
        structure.move(stubl + armw / 2.)
        structure.move(arml / 2., structure.last_direction - 90)
        structure.last_direction += 90
    else:
        pass

    if corner_rad > armgapw:
        print("corner_rad should not be bigger then armgapw. Things may not turn out well.")
    else:
        pass

    if armgapw > stubl:
        print("armgapw should not be bigger then stubl. Things may not turn out well.")
    else:
        pass

    starting_point = structure.last
    starting_direction = structure.last_direction
    fin1_point = starting_point
    fin1_dir = starting_direction + 180
    structure.move((armw + armgapw) / 2., structure.last_direction - 90)
    CPWStraight(structure, arml, pinw=0, gapw=armgapw / 2.)
    structure.move((armw + armgapw) / 2., structure.last_direction + 90)
    fin2_point = structure.last
    fin2_dir = structure.last_direction
    structure.move(armw / 2., structure.last_direction + 90)
    structure.move(arml / 2., structure.last_direction + 180)
    structure.last_direction += 90
    CPWStraight(structure, armgapw, pinw=stubw + 2 * corner_rad, gapw=(arml - stubw - 2 * corner_rad) / 2.)
    CPWStraight(structure, stubl - armgapw, pinw=stubw, gapw=stubgapw)
    stub_point = structure.last
    stub_dir = structure.last_direction
    structure.move(armgapw - stubl)
    structure.move((stubw + corner_rad) / 2., structure.last_direction - 90)
    structure.last_direction += 180
    CPWStraight(structure, armgapw - corner_rad, pinw=0, gapw=corner_rad / 2)
    CPWBendNew(structure, angle=90, pinw=0.0, gapw=corner_rad / 2., radius=corner_rad / 2., polyarc=1, segments=4,
               square=square)
    structure.move(-2 * corner_rad - stubw)
    CPWBendNew(structure, angle=90, pinw=0.0, gapw=corner_rad / 2., radius=corner_rad / 2., polyarc=1, segments=4,
               square=square)
    CPWStraight(structure, armgapw - corner_rad, pinw=0, gapw=corner_rad / 2)

    if couptype == 0:
        structure.last = fin2_point
        structure.last_direction = fin2_dir
    elif couptype == 1:
        structure.last = fin1_point
        structure.last_direction = fin1_dir
    else:
        pass

    if couptype == 1:
        return fin1_point, fin1_dir, stub_point, stub_dir
    elif couptype == 2:
        return fin1_point, fin1_dir, fin2_point, fin2_dir
    else:
        return fin2_point, fin2_dir, stub_point, stub_dir


def CapNew(structure, finw=100.0, finl=300.0, arml=300.0, connecw=20.0, connecl=20.0, cgapw=20.0, couptype=0,
           fin1connecl=0, fin2connecl=0, finconnecw=0, finconnecgapw=0, no_induct=0, square=1):
    # couptype=0: input at one finger
    # couptype=1: input at the other finger
    # couptype=2: input at arm
    # couptype=3: input at inductor connecter

    finl -= cgapw + finw / 2
    arml -= 2 * cgapw

    if couptype == 1:
        structure.move(arml + 2 * (finw + 2 * cgapw))
        structure.last_direction += 180
    elif couptype == 2:
        structure.move(2 * cgapw + finw + finl / 2.)
        structure.move(2 * cgapw + finw + arml / 2., structure.last_direction + 90)
        structure.last_direction -= 90
    elif couptype == 3:
        structure.move(connecl - cgapw - finl / 2.)
        structure.move(2 * cgapw + finw + arml / 2., structure.last_direction - 90)
        structure.last_direction += 90
    else:
        pass

    starting_point = structure.last
    starting_direction = structure.last_direction

    structure.move(cgapw / 2.)
    structure.move(finl / 2., structure.last_direction + 90)
    structure.last_direction += 90

    turning_point = structure.last
    turning_direction = structure.last_direction

    # clear some metal
    CPWStraight(structure, cgapw + finw / 2., pinw=0, gapw=cgapw / 2.)

    structure.last = turning_point
    structure.last_direction = turning_direction
    structure.move(finw / 2.)
    structure.move((finw + cgapw) / 2., turning_direction - 90)
    CPWStraight(structure, cgapw, pinw=0, gapw=finw / 2.)

    structure.last = turning_point
    structure.last_direction = turning_direction
    structure.move(finw + cgapw, turning_direction - 90)
    CPWStraight(structure, cgapw + finw / 2., pinw=0, gapw=cgapw / 2.)

    # draw one finger
    structure.last = turning_point
    structure.last_direction = turning_direction
    CPWBendNew(structure, angle=-180, pinw=0, gapw=cgapw / 2., radius=(finw + cgapw) / 2., polyarc=1, segments=4,
               square=square)
    structure.move((finw + cgapw) / 2., structure.last_direction - 90)
    if fin1connecl != 0:
        structure.last, structure.last_direction, stub1_point, stub1_dir = CPWTeeNew(structure, arml=finl, armw=finw,
                                                                                     armgapw=cgapw, corner_rad=cgapw,
                                                                                     stubl=fin1connecl,
                                                                                     stubw=finconnecw,
                                                                                     stubgapw=finconnecgapw, couptype=1,
                                                                                     square=square)
    else:
        CPWStraight(structure, finl, pinw=finw, gapw=cgapw)

    CPWBendNew(structure, angle=90, pinw=finw, gapw=cgapw, radius=cgapw + finw / 2., polyarc=1, segments=4,
               square=square)

    # draw the arm
    if no_induct == 0:
        nextfin_point, structure.last_direction, inductcoup_point, inductcoup_dir = CPWTeeNew(structure, arml=arml,
                                                                                              armw=finw, armgapw=cgapw,
                                                                                              corner_rad=cgapw,
                                                                                              stubl=connecl,
                                                                                              stubw=connecw, stubgapw=(
                                                                                                                              arml - connecw) / 2,
                                                                                              couptype=0, square=square)
    else:
        CPWStraight(structure, arml, pinw=finw, gapw=cgapw)
        nextfin_point = structure.last
        inductcoup_point = structure.move(-arml / 2.)
        inductcoup_dir = structure.last_direction + 90

    # define the armcoupling point
    structure.last = nextfin_point
    structure.move(-arml / 2.)
    structure.move(cgapw + finw / 2., structure.last_direction - 90)
    armcoup_point = structure.last
    armcoup_dir = structure.last_direction - 90
    structure.last = nextfin_point

    # draw the other finger
    CPWBendNew(structure, angle=90, pinw=finw, gapw=cgapw, radius=cgapw + finw / 2, polyarc=1, segments=4,
               square=square)
    if fin2connecl != 0:
        structure.last, structure.last_direction, stub2_point, stub2_dir = CPWTeeNew(structure, arml=finl, armw=finw,
                                                                                     armgapw=cgapw, corner_rad=cgapw,
                                                                                     stubl=fin2connecl,
                                                                                     stubw=finconnecw,
                                                                                     stubgapw=finconnecgapw, couptype=1,
                                                                                     square=square)
    else:
        CPWStraight(structure, finl, pinw=finw, gapw=cgapw)
    structure.move((finw + cgapw) / 2., structure.last_direction + 90)
    CPWBendNew(structure, angle=-180, pinw=0, gapw=cgapw / 2., radius=(finw + cgapw) / 2., polyarc=1, segments=4,
               square=square)

    # clear some more metal for the other finger
    structure.last_direction += 180
    CPWStraight(structure, cgapw + finw / 2., pinw=0, gapw=cgapw / 2.)
    structure.move((finw + cgapw) / 2., structure.last_direction + 90)
    structure.last_direction += 180
    CPWStraight(structure, cgapw, pinw=0, gapw=finw / 2.)
    structure.move(-cgapw)
    structure.move((finw + cgapw) / 2., structure.last_direction - 90)
    CPWStraight(structure, cgapw + finw / 2., pinw=0, gapw=cgapw / 2.)

    # define the third coupling point
    structure.move(finl / 2.)
    structure.move(finw + 1.5 * cgapw, structure.last_direction + 90)
    structure.last_direction += 90

    if couptype == 1:
        structure.last = starting_point
        structure.last_direction = starting_direction + 180
        fincoup_point = structure.last
        fincoup_dir = structure.last_direction
        return armcoup_point, armcoup_dir, fincoup_point, fincoup_dir, inductcoup_point, inductcoup_dir
    elif couptype == 2:
        fin1coup_point = structure.last
        fin1coup_dir = structure.last_direction
        fin2coup_point = starting_point
        fin2coup_dir = starting_direction + 180
        return fin1coup_point, fin1coup_dir, fin2coup_point, fin2coup_dir, inductcoup_point, inductcoup_dir
    elif couptype == 3:
        fin1coup_point = structure.last
        fin1coup_dir = structure.last_direction
        fin2coup_point = starting_point
        fin2coup_dir = starting_direction + 180
        return armcoup_point, armcoup_dir, fin1coup_point, fin1coup_dir, fin2coup_point, fin2coup_dir
    else:
        fincoup_point = structure.last
        fincoup_dir = structure.last_direction
        return armcoup_point, armcoup_dir, fincoup_point, fincoup_dir, inductcoup_point, inductcoup_dir


def FluxQubit(structure, start_point=(0, 0), large_juncw=2.0, large_juncl=3.0, small_juncw=0.24, bridgel=0.4):
    s = structure
    s.last = start_point
    start_direction = 90
    s.two_layer = True
    junc_number = 7
    loopw = 10.0
    qubitw = large_juncw + small_juncw + loopw
    undercutl = 1.0
    endl = 3.0
    terml = 3.0

    s.pin_layer.last = start_point
    s.pin_layer.last_direction = start_direction
    s.gap_layer.last = start_point
    s.gap_layer.last_direction = start_direction

    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=qubitw / 2.)
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, endl, pinw=0.0, gapw=qubitw / 2.)
    return_point = s.pin_layer.last
    s.pin_layer.last = (s.pin_layer.last[0] + qubitw / 2. - large_juncw / 2., s.pin_layer.last[1])
    CPWStraight(s.pin_layer, terml, pinw=0.0, gapw=large_juncw / 2.)

    for i in range(junc_number):
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
        s.pin_layer.last = s.gap_layer.last
        CPWStraight(s.pin_layer, large_juncl, pinw=0.0, gapw=large_juncw / 2.)
        s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, terml, pinw=0.0, gapw=large_juncw / 2.)
    end_chain_pt = s.pin_layer.last
    s.pin_layer.last = (s.pin_layer.last[0] - qubitw / 2. + large_juncw / 2., s.pin_layer.last[1])
    CPWStraight(s.pin_layer, endl, pinw=0.0, gapw=qubitw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=qubitw / 2.)
    s.pin_layer.last = (return_point[0] - qubitw / 2. + small_juncw / 2., return_point[1])
    s.gap_layer.last = (return_point[0] - qubitw / 2. + small_juncw / 2., return_point[1])
    chain_length = abs(return_point[1] - end_chain_pt[1])
    temp_length = abs(chain_length / 2. - bridgel)
    CPWStraight(s.pin_layer, temp_length, pinw=0.0, gapw=small_juncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=small_juncw / 2.)
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, temp_length + bridgel, pinw=0.0, gapw=small_juncw / 2.)


def FluxQubitv2(structure, start_point=(0, 0), large_juncw=2.0, large_juncl=3.0, small_juncw=0.24, bridgel=0.4):
    s = structure
    s.last = start_point
    start_direction = 90
    s.two_layer = True
    rjunc_number = 50
    ljunc_number = 24
    loopw = 10.0
    qubitw = large_juncw + small_juncw + loopw
    undercutl = 1.0
    small_juncl = 5.3
    endl = 3.0
    terml = 3.0
    cap_connectl = 0.5

    s.pin_layer.last = start_point
    s.pin_layer.last_direction = start_direction
    s.gap_layer.last = start_point
    s.gap_layer.last_direction = start_direction

    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=qubitw / 2.)
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, endl, pinw=0.0, gapw=qubitw / 2.)
    return_point = s.pin_layer.last
    s.pin_layer.last = (s.pin_layer.last[0] + qubitw / 2. - large_juncw / 2., s.pin_layer.last[1])

    for i in range(rjunc_number):
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
        s.pin_layer.last = s.gap_layer.last
        CPWStraight(s.pin_layer, large_juncl, pinw=0.0, gapw=large_juncw / 2.)
        s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
    s.pin_layer.last = s.gap_layer.last

    end_chain_pt = s.pin_layer.last
    s.pin_layer.last = (s.pin_layer.last[0] - qubitw / 2. + large_juncw / 2., s.pin_layer.last[1])
    CPWStraight(s.pin_layer, endl, pinw=0.0, gapw=qubitw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=qubitw / 2.)
    s.pin_layer.last = (return_point[0] - qubitw / 2. + large_juncw / 2., return_point[1])
    s.gap_layer.last = (return_point[0] - qubitw / 2. + large_juncw / 2., return_point[1])
    chain_length = abs(return_point[1] - end_chain_pt[1])

    for i in range(ljunc_number):
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
        s.pin_layer.last = s.gap_layer.last
        CPWStraight(s.pin_layer, large_juncl, pinw=0.0, gapw=large_juncw / 2.)
        s.gap_layer.last = s.pin_layer.last
        cap_connect1 = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=small_juncw, gapw=large_juncw / 2. - small_juncw / 2.)
    lchain_length = 2 * abs(return_point[1] - s.pin_layer.last[1])
    if lchain_length > chain_length:
        print("Left Side of Inductor needs less junctions")
    CPWStraight(s.pin_layer, small_juncl / 2., pinw=0.0, gapw=small_juncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=small_juncw / 2.)
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, small_juncl / 2., pinw=0.0, gapw=small_juncw / 2.)

    s.gap_layer.last = (s.pin_layer.last[0], s.pin_layer.last[1] - undercutl)
    CPWStraight(s.gap_layer, undercutl, pinw=small_juncw, gapw=large_juncw / 2. - small_juncw / 2.)
    cap_connect2 = s.gap_layer.last
    for i in range(ljunc_number):
        CPWStraight(s.pin_layer, large_juncl, pinw=0.0, gapw=large_juncw / 2.)
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
        s.pin_layer.last = s.gap_layer.last


def InductorBox(structure, Inductl=100.0, ipinw=10.0, igapw=10.0, induct_num=2, connecl=50.0, boxgap=50, square=0):
    rad = igapw + ipinw / 2.
    starting_point = structure.last
    starting_direction = structure.last_direction

    # clear some metal before drawing
    structure.move((connecl + igapw) / 2.)
    structure.move(igapw + ipinw / 2., structure.last_direction - 90)
    structure.last_direction -= 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap, pinw=0, gapw=(igapw + connecl) / 2.)

    # clear some more metal before drawing
    structure.last = starting_point
    structure.last_direction = starting_direction
    structure.move((connecl + igapw + ipinw) / 2.)
    structure.move(ipinw / 2., structure.last_direction + 90)
    structure.last_direction = starting_direction + 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap + igapw, pinw=0, gapw=(connecl + igapw + ipinw) / 2.)

    # more!!!!
    # structure.last=(starting_point[0]-prefac*(connecl+ipinw+2*igapw),starting_point[1]+prefac*(igapw+ipinw/2))
    structure.last = starting_point
    structure.last_direction = starting_direction
    structure.move(connecl + ipinw + 2 * igapw)
    structure.move(igapw + ipinw / 2., structure.last_direction - 90)
    structure.last_direction = starting_direction + 90
    CPWStraight(structure, Inductl / 2. + 3 * rad + boxgap, pinw=0, gapw=igapw)

    # draw the connector
    structure.last = starting_point
    structure.last_direction = starting_direction

    # start to draw the inductors
    CPWStraight(structure, connecl, pinw=ipinw, gapw=igapw)
    CPWBendNew(structure, angle=-90, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
    CPWStraight(structure, Inductl / 2. - rad, pinw=ipinw, gapw=igapw)

    for i in range(induct_num):
        turning_position = structure.last
        turning_direction = structure.last_direction

        # clear metal at one side of the turning positions
        structure.move(igapw + ipinw / 2., turning_direction - 90)
        CPWStraight(structure, 2 * rad + boxgap, pinw=0, gapw=igapw)

        structure.move(-(2 * rad + boxgap - ipinw - igapw) / 2.)
        structure.move(igapw, turning_direction + 90)
        structure.last_direction += 90
        CPWStraight(structure, 2 * (ipinw + igapw), pinw=0, gapw=(2 * rad + boxgap - ipinw - igapw) / 2.)

        # clear metal at the other side
        structure.move(-ipinw)
        structure.move(2 * rad + boxgap + ipinw + igapw + Inductl, structure.last_direction + 90)
        CPWStraight(structure, 2 * (ipinw + igapw), pinw=0, gapw=(2 * rad + boxgap - ipinw - igapw) / 2.)

        structure.move((ipinw + igapw) / 2., structure.last_direction - 90)
        CPWStraight(structure, 2 * igapw, pinw=0, gapw=rad + boxgap / 2.)

        structure.last = turning_position
        structure.last_direction = turning_direction

        # the real deal is here!
        CPWBendNew(structure, angle=180, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
        CPWStraight(structure, Inductl, pinw=ipinw, gapw=igapw)
        CPWBendNew(structure, angle=-180, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
        CPWStraight(structure, Inductl, pinw=ipinw, gapw=igapw)

    turning_position = structure.last
    turning_direction = structure.last_direction

    # keep clearing metal...
    structure.move(igapw + ipinw / 2., turning_direction - 90)
    CPWStraight(structure, 2 * rad + boxgap, pinw=0, gapw=igapw)
    structure.last = turning_position

    structure.move(igapw + ipinw)
    structure.move(igapw + ipinw / 2., turning_direction + 90)
    CPWStraight(structure, igapw + boxgap, pinw=0, gapw=igapw + ipinw)

    structure.last = turning_position
    structure.last_direction = turning_direction

    # draw the rest part of the inductor
    CPWBendNew(structure, angle=180, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
    CPWStraight(structure, Inductl / 2. - rad, pinw=ipinw, gapw=igapw)
    CPWBendNew(structure, angle=-90, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
    CPWStraight(structure, connecl, pinw=ipinw, gapw=igapw)

    end_point = structure.last
    end_direction = structure.last_direction

    # clear the rest metal
    structure.move(-(connecl + igapw) / 2.)
    structure.move(igapw + ipinw / 2., end_direction - 90)
    structure.last_direction -= 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap, pinw=0, gapw=(igapw + connecl) / 2.)

    structure.last = end_point
    structure.last_direction = end_direction
    structure.move(-(connecl + igapw + ipinw) / 2.)
    structure.move(ipinw / 2., end_direction + 90)
    structure.last_direction = end_direction + 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap + igapw, pinw=0, gapw=(connecl + igapw + ipinw) / 2.)

    structure.last = end_point
    structure.last_direction = end_direction
    structure.move(-(connecl + ipinw + 2 * igapw))
    structure.move(igapw + ipinw / 2., end_direction - 90)
    structure.last_direction = end_direction + 90
    CPWStraight(structure, Inductl / 2 + 3 * rad + boxgap, pinw=0, gapw=igapw)

    structure.last = end_point
    structure.last_direction = end_direction


def InductorChain(structure, start_point=(0, 0), large_juncw=2.0, large_juncl=3.0, small_juncw=0.24, bridgel=0.4):
    s = structure
    s.last = start_point
    start_direction = 90
    s.two_layer = True
    rjunc_number = 25
    ljunc_number = 24
    loopw = 10.0
    qubitw = large_juncw + small_juncw + loopw
    undercutl = 1.0
    small_juncl = 5.3
    endl = 3.0
    terml = 3.0
    cap_connectl = 0.5

    s.pin_layer.last = start_point
    s.pin_layer.last_direction = start_direction
    s.gap_layer.last = start_point
    s.gap_layer.last_direction = start_direction

    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=qubitw / 2.)
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, endl, pinw=0.0, gapw=qubitw / 2.)
    return_point = s.pin_layer.last
    s.pin_layer.last = (s.pin_layer.last[0] + qubitw / 2. - large_juncw / 2., s.pin_layer.last[1])

    for i in range(rjunc_number):
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
        s.pin_layer.last = s.gap_layer.last
        CPWStraight(s.pin_layer, large_juncl, pinw=0.0, gapw=large_juncw / 2.)
        s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
    s.pin_layer.last = s.gap_layer.last

    end_chain_pt = s.pin_layer.last
    s.pin_layer.last = (s.pin_layer.last[0] - qubitw / 2. + large_juncw / 2., s.pin_layer.last[1])
    CPWStraight(s.pin_layer, endl, pinw=0.0, gapw=qubitw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=qubitw / 2.)
    s.pin_layer.last = (return_point[0] - qubitw / 2. + large_juncw / 2., return_point[1])
    s.gap_layer.last = (return_point[0] - qubitw / 2. + large_juncw / 2., return_point[1])
    chain_length = abs(return_point[1] - end_chain_pt[1])

    for i in range(rjunc_number):
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
        s.pin_layer.last = s.gap_layer.last
        CPWStraight(s.pin_layer, large_juncl, pinw=0.0, gapw=large_juncw / 2.)
        s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, bridgel, pinw=0.0, gapw=large_juncw / 2.)
    s.pin_layer.last = s.gap_layer.last


def InductorLength(Inductl, ipinw, igapw, induct_num, connecl):
    length = (Inductl - ((2 * igapw) + ipinw)) + (Inductl) * (2 * inductnum) + ((2 * igapw) + ipinw) * (
                2 * (2 * inductnum + 1)) + ((2 * igapw) + ipinw) * (2) + 2 * connecl
    return length


def InterdigitatedFingerCap(structure, num_fingers, finger_length, finger_width, finger_gap, fingerpad_gap, cap_pad_y,
                            border_y, wire_thickness, vertical=1, right=1):
    s = structure
    start_pt = s.last
    cap_length = finger_length + finger_gap
    cap_width = (num_fingers * finger_width) + ((num_fingers - 1) * finger_gap)
    border_x = (num_fingers * finger_width) + ((num_fingers - 1) * finger_gap)

    if vertical:
        ref_dir = s.last_direction
        start_dir = 90.0
        s.last_direction = start_dir

        CPWStraight(s, border_y, pinw=0.0, gapw=border_x / 2.0)
        center_pt = s.last
        s.last = (s.last[0] - (border_x / 2.0), s.last[1] + cap_pad_y)
        left_pt = s.last
        s.last = (left_pt[0], left_pt[1])

        for i in range(num_fingers):
            s.last = (s.last[0] + finger_width / 2., left_pt[1])
            if i % 2 == 0:
                s.last = (s.last[0], s.last[1] + finger_length)
            else:
                s.last = (s.last[0], s.last[1])

            CPWStraight(s, fingerpad_gap, pinw=0.0, gapw=finger_width / 2.)
            s.last = (s.last[0] + finger_width / 2. + finger_gap / 2., left_pt[1])
            if not i == (num_fingers - 1):
                CPWStraight(s, finger_length + fingerpad_gap, pinw=0.0, gapw=finger_gap / 2.0)
                s.last = (s.last[0] + finger_gap / 2., left_pt[1])

        s.last = (center_pt[0], left_pt[1] + finger_length + fingerpad_gap + cap_pad_y)
        CPWStraight(s, border_y, pinw=0.0, gapw=border_x / 2.0)
        if right:
            s.last = (start_pt[0] - border_x / 2. - border_y / 2., start_pt[1])
            CPWStraight(s, 2 * (border_y + cap_pad_y) + finger_length + fingerpad_gap, pinw=0.0, gapw=border_y / 2.0)

            s.last = (start_pt[0] + border_x / 2. + wire_thickness / 2., start_pt[1])
            wire1_pt = (s.last[0] + wire_thickness / 2., s.last[1])
            CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
            s.last = (s.last[0], s.last[1] + cap_pad_y)
            CPWStraight(s, finger_length + fingerpad_gap, pinw=0.0, gapw=wire_thickness / 2.0)
            s.last = (s.last[0], s.last[1] + cap_pad_y)
            CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
            wire2_pt = (s.last[0] + wire_thickness / 2.0, s.last[1])

        else:
            s.last = (start_pt[0] - border_x / 2. - wire_thickness / 2., start_pt[1])
            wire1_pt = (s.last[0] + wire_thickness / 2., s.last[1])
            CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
            s.last = (s.last[0], s.last[1] + cap_pad_y)
            CPWStraight(s, finger_length + fingerpad_gap, pinw=0.0, gapw=wire_thickness / 2.0)
            s.last = (s.last[0], s.last[1] + cap_pad_y)
            CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
            wire2_pt = (s.last[0] + wire_thickness / 2.0, s.last[1])

            s.last = (start_pt[0] + border_x / 2. + border_y / 2., start_pt[1])
            CPWStraight(s, 2 * (border_y + cap_pad_y) + finger_length + fingerpad_gap, pinw=0.0, gapw=border_y / 2.0)

        s.last_direction = ref_dir
        return wire1_pt, wire2_pt


def InterdigitatedFingerCapVertical(structure, num_fingers, finger_length, finger_width, finger_gap, fingerpad_gap,
                                    cap_pad_y,
                                    border_y, wire_thickness):
    s = structure
    ref_pt = s.last
    cap_length = finger_length + finger_gap
    cap_width = (num_fingers * finger_width) + ((num_fingers - 1) * finger_gap)
    border_x = (num_fingers * finger_width) + ((num_fingers - 1) * finger_gap)

    ref_dir = s.last_direction
    start_dir = 90.0
    s.last_direction = start_dir
    start_pt = (s.last[0] - cap_width, s.last[1])

    CPWStraight(s, border_y, pinw=0.0, gapw=border_x / 2.0)
    center_pt = s.last
    s.last = (s.last[0] - (border_x / 2.0), s.last[1] + cap_pad_y)
    left_pt = s.last
    s.last = (left_pt[0], left_pt[1])

    for i in range(num_fingers):
        s.last = (s.last[0] + finger_width / 2., left_pt[1])
        if i % 2 == 0:
            s.last = (s.last[0], s.last[1] + finger_length)
        else:
            s.last = (s.last[0], s.last[1])

        CPWStraight(s, fingerpad_gap, pinw=0.0, gapw=finger_width / 2.)
        s.last = (s.last[0] + finger_width / 2. + finger_gap / 2., left_pt[1])
        if not i == (num_fingers - 1):
            CPWStraight(s, finger_length + fingerpad_gap, pinw=0.0, gapw=finger_gap / 2.0)
            s.last = (s.last[0] + finger_gap / 2., left_pt[1])

    s.last = (center_pt[0], left_pt[1] + finger_length + fingerpad_gap + cap_pad_y)
    CPWStraight(s, border_y, pinw=0.0, gapw=border_x / 2.0)
    # if right:
    #     s.last = (start_pt[0] - border_x / 2. - border_y / 2., start_pt[1])
    #     CPWStraight(s, 2 * (border_y + cap_pad_y) + finger_length + fingerpad_gap, pinw=0.0, gapw=border_y / 2.0)
    #
    #     s.last = (start_pt[0] + border_x / 2. + wire_thickness / 2., start_pt[1])
    #     wire1_pt = (s.last[0] + wire_thickness / 2., s.last[1])
    #     CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
    #     s.last = (s.last[0], s.last[1] + cap_pad_y)
    #     CPWStraight(s, finger_length + fingerpad_gap, pinw=0.0, gapw=wire_thickness / 2.0)
    #     s.last = (s.last[0], s.last[1] + cap_pad_y)
    #     CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
    #     wire2_pt = (s.last[0] + wire_thickness / 2.0, s.last[1])
    #
    # else:
    #     s.last = (start_pt[0] - border_x / 2. - wire_thickness / 2., start_pt[1])
    #     wire1_pt = (s.last[0] + wire_thickness / 2., s.last[1])
    #     CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
    #     s.last = (s.last[0], s.last[1] + cap_pad_y)
    #     CPWStraight(s, finger_length + fingerpad_gap, pinw=0.0, gapw=wire_thickness / 2.0)
    #     s.last = (s.last[0], s.last[1] + cap_pad_y)
    #     CPWStraight(s, border_y, pinw=0.0, gapw=wire_thickness / 2.0)
    #     wire2_pt = (s.last[0] + wire_thickness / 2.0, s.last[1])
    #
    #     s.last = (start_pt[0] + border_x / 2. + border_y / 2., start_pt[1])
    #     CPWStraight(s, 2 * (border_y + cap_pad_y) + finger_length + fingerpad_gap, pinw=0.0, gapw=border_y / 2.0)

    s.last = ref_pt
    s.last_direction = ref_dir


def InterdigitatedFingerCapHorizontal(structure, num_fingers, finger_length, finger_width, finger_gap, fingerpad_gap,
                                      cap_pad_y,
                                      border_y, wire_thickness):
    s = structure
    ref_pt = s.last
    cap_length = finger_length + finger_gap
    cap_width = (num_fingers * finger_width) + ((num_fingers - 1) * finger_gap)
    border_x = (num_fingers * finger_width) + ((num_fingers - 1) * finger_gap)

    ref_dir = s.last_direction
    start_dir = 0.0
    s.last_direction = start_dir
    start_pt = (ref_pt[0], ref_pt[1] - cap_width)

    CPWStraight(s, border_y, pinw=0.0, gapw=border_x / 2.0)
    center_pt = s.last
    s.last = (s.last[0] + cap_pad_y, s.last[1] - (border_x / 2.0))
    left_pt = s.last

    for i in range(num_fingers):
        s.last = (left_pt[0], s.last[1] + finger_width / 2.)
        if i % 2 == 0:
            s.last = (s.last[0] + finger_length, s.last[1])
        else:
            s.last = (s.last[0], s.last[1])

        CPWStraight(s, fingerpad_gap, pinw=0.0, gapw=finger_width / 2.)
        s.last = (left_pt[0], s.last[1] + finger_width / 2. + finger_gap / 2.)
        if not i == (num_fingers - 1):
            CPWStraight(s, finger_length + fingerpad_gap, pinw=0.0, gapw=finger_gap / 2.0)
            s.last = (left_pt[0], s.last[1] + finger_gap / 2.)

    s.last = (left_pt[0] + finger_length + fingerpad_gap + cap_pad_y, center_pt[1])
    CPWStraight(s, border_y, pinw=0.0, gapw=border_x / 2.0)

    s.last = ref_pt
    s.last_direction = ref_dir


def StackedFluxonium(structure, start_point=(0, 0), juncw=0.25, juncl=5.1, sjuncl=0.8, sjuncw=0.5, sjuncl2=1.9,
                     undercutw=1.5, undercutl=0.7, bufferl=0.2):
    s = structure
    s.two_layer = True
    s.pin_layer.last = start_point
    s.gap_layer.last = start_point
    start_direction = 0
    s.pin_layer.last_direction = start_direction
    s.gap_layer.last_direction = start_direction
    junc_number = 6
    qjuncl = 0.4
    qjuncw = 0.12
    qbridgel = 0.38
    qbridgew = 1.0
    end_juncl = 5.0

    return_point = s.pin_layer.last
    for i in range(junc_number):
        CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last_direction += 90
        s.pin_layer.last = (s.gap_layer.last[0] - bufferl - juncw / 2., s.gap_layer.last[1] + undercutw / 2.)
        CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
        s.gap_layer.last = (s.pin_layer.last[0] - bufferl - juncw / 2., s.pin_layer.last[1] + undercutw / 2.)
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last_direction -= 90
        s.pin_layer.last = s.gap_layer.last
        CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last_direction -= 90
        s.pin_layer.last = (s.gap_layer.last[0] - bufferl - juncw / 2., s.gap_layer.last[1] - undercutw / 2.)
        CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
        s.gap_layer.last = (s.pin_layer.last[0] - juncw / 2. - bufferl, s.pin_layer.last[1] - undercutw / 2.)
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last = s.gap_layer.last
        s.pin_layer.last_direction += 90

    CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction += 90
    s.pin_layer.last = (s.gap_layer.last[0] - bufferl - juncw / 2., s.gap_layer.last[1] + undercutw / 2.)
    CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
    s.gap_layer.last = (s.pin_layer.last[0] - bufferl - juncw / 2., s.pin_layer.last[1] + undercutw / 2.)
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction -= 90
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction += 90
    s.pin_layer.last = (s.gap_layer.last[0] - bufferl - juncw / 2., s.gap_layer.last[1] + undercutw / 2.)
    CPWStraight(s.pin_layer, end_juncl, pinw=0.0, gapw=juncw / 2.)
    s.gap_layer.last = (s.pin_layer.last[0] - undercutl + bufferl, s.pin_layer.last[1] + undercutw / 2.)
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last = (s.gap_layer.last[0] - undercutl, s.gap_layer.last[1])
    s.pin_layer.last_direction += 90
    s.gap_layer.last_direction = s.pin_layer.last_direction
    s.pin_layer.last = (s.gap_layer.last[0] - undercutl, s.gap_layer.last[1])
    CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction -= 90
    s.pin_layer.last = (s.gap_layer.last[0] + juncw / 2. + bufferl, s.gap_layer.last[1] + undercutw / 2.)
    CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
    s.gap_layer.last_direction = s.pin_layer.last_direction + 90
    s.gap_layer.last = (s.pin_layer.last[0] + juncw / 2. + bufferl, s.pin_layer.last[1] + undercutw / 2.)
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction = s.gap_layer.last_direction
    s.pin_layer.last = s.gap_layer.last
    for i in range(junc_number):
        CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last_direction += 90
        s.pin_layer.last = (s.gap_layer.last[0] + bufferl + juncw / 2., s.gap_layer.last[1] - undercutw / 2.)
        CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
        s.gap_layer.last = (s.pin_layer.last[0] + bufferl + juncw / 2., s.pin_layer.last[1] - undercutw / 2.)
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last_direction -= 90
        s.pin_layer.last = s.gap_layer.last
        CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
        s.gap_layer.last = s.pin_layer.last
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last_direction -= 90
        s.pin_layer.last = (s.gap_layer.last[0] + bufferl + juncw / 2., s.gap_layer.last[1] + undercutw / 2.)
        CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
        s.gap_layer.last = (s.pin_layer.last[0] + juncw / 2. + bufferl, s.pin_layer.last[1] + undercutw / 2.)
        CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
        s.pin_layer.last = s.gap_layer.last
        s.pin_layer.last_direction += 90

    CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction += 90
    s.pin_layer.last = (s.gap_layer.last[0] + bufferl + juncw / 2., s.gap_layer.last[1] - undercutw / 2.)
    CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
    s.gap_layer.last = (s.pin_layer.last[0] + bufferl + juncw / 2., s.pin_layer.last[1] - undercutw / 2.)
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction -= 90
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, sjuncl2, pinw=0.0, gapw=sjuncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction += 90
    s.pin_layer.last = (s.gap_layer.last[0] + bufferl + juncw / 2., s.gap_layer.last[1] - undercutw / 2.)
    CPWStraight(s.pin_layer, end_juncl, pinw=0.0, gapw=juncw / 2.)
    s.gap_layer.last = (s.pin_layer.last[0] + undercutl - bufferl, s.pin_layer.last[1] - undercutw / 2.)
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)

    s.pin_layer.last = (s.gap_layer.last[0] + undercutl, s.gap_layer.last[1])
    s.pin_layer.last_direction += 90
    s.gap_layer.last_direction = s.pin_layer.last_direction
    CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
    return_point = s.pin_layer.last
    return_direction = s.pin_layer.last_direction
    CPWStraight(s.pin_layer, qjuncl, pinw=0.0, gapw=qjuncw / 2.)
    s.gap_layer.last = return_point
    CPWStraight(s.gap_layer, qjuncl, pinw=qjuncw, gapw=undercutw / 2.)
    CPWStraight(s.gap_layer, qbridgel, pinw=0.0, gapw=qbridgew / 2.)
    s.pin_layer.last = s.gap_layer.last
    cap_connect2 = s.pin_layer.last
    CPWStraight(s.pin_layer, sjuncl, pinw=0.0, gapw=sjuncw / 2.)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)
    s.pin_layer.last_direction -= 90
    s.pin_layer.last = (s.gap_layer.last[0] - bufferl - juncw / 2., s.gap_layer.last[1] - undercutw / 2.)
    CPWStraight(s.pin_layer, juncl, pinw=0.0, gapw=juncw / 2.)
    s.gap_layer.last = (s.pin_layer.last[0] - bufferl - juncw / 2., s.pin_layer.last[1] - undercutw / 2.)
    CPWStraight(s.gap_layer, undercutl, pinw=0.0, gapw=undercutw / 2.)

    # putting leads to connect to qubit
    leadl = 0.3
    leadw = 10.0
    lead_undercutl = 0.3
    s.pin_layer.last = (return_point[0] - leadl / 2. - 0.2, return_point[1] - sjuncw / 2.)
    cap_connect = s.pin_layer.last
    s.pin_layer.last_direction = return_direction - 90
    CPWStraight(s.pin_layer, leadw, pinw=0.0, gapw=leadl / 2.)
    s.gap_layer.last = (cap_connect[0] + lead_undercutl / 2. + leadl / 2., cap_connect[1])
    s.gap_layer.last_direction = s.pin_layer.last_direction
    CPWStraight(s.gap_layer, leadw + 0.4, pinw=0.0, gapw=lead_undercutl / 2.)

    s.pin_layer.last = (cap_connect2[0] + leadl / 2. + 0.2, cap_connect2[1] - sjuncw / 2.)
    CPWStraight(s.pin_layer, leadw, pinw=0.0, gapw=leadl / 2.)
    s.gap_layer.last = (cap_connect2[0] - lead_undercutl / 2. + 0.2, cap_connect2[1] - sjuncw / 2.)
    CPWStraight(s.gap_layer, leadw + 0.4, pinw=0.0, gapw=lead_undercutl / 2.)


def StackQubitBoxSymF(structure, qubit_boxw=40.0, fpinw=cpw_pinw, fgapw=cpw_gapw, squ=0):
    qubit_capl = 200.0
    qubit_capw = 50.0
    flux_sep1 = 10.0 - 2.
    flux_sep2 = 20.0 - 5.8
    flux_pinw = 3.0
    flux_taperl = 100.0
    flux_length = 30.0
    pad_sep = 118.0

    s = structure
    starting_point = (s.last[0], s.last[1] + flux_sep1)
    starting_direction = s.last_direction

    structure.last = (s.last[0] + flux_pinw + flux_taperl, starting_point[1])
    temp_point = s.last
    #    CPWStraight(s,qubit_boxw,pinw=0.0,gapw=pad_sep/2.)
    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 5., starting_point[1] + pad_sep / 2.)
    s.last_direction = starting_direction + 90
    CoupPad(s, padw=qubit_capw, padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=20.0, connecl=50.0,
            gapw=30.0, connecgapw=65.0, coupstart=0, square=squ)
    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 10.0, starting_point[1] - pad_sep / 2.)
    s.last_direction = starting_direction - 90
    CoupPad(s, padw=qubit_capw, padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=20.0, connecl=50.0,
            gapw=30.0, connecgapw=60.0, coupstart=0, square=squ)
    #    CoupPad(s,padw=qubit_capw,padl=qubit_capl, girdle_l=girdle_l, corner_rad=10, connecw=cpw_pinw,connecl=conneclq,gapw=gapwq,connecgapw=cpw_gapw,coupstart=1,square=square)

    clear1 = 30.0
    s.last = (temp_point[0], temp_point[1] + pad_sep / 2. - clear1 / 2.)
    s.last_direction = starting_direction + 180
    CPWStraight(s, 60.0, pinw=0.0, gapw=clear1 / 2.)
    clear2 = 15.0
    s.last = (temp_point[0], temp_point[1] - pad_sep / 2. + clear2 / 2.)
    s.last_direction = starting_direction + 180
    CPWStraight(s, 60.0, pinw=0.0, gapw=clear2 / 2.)
    clear3 = 10.0
    s.last = (temp_point[0] + qubit_boxw, temp_point[1] + pad_sep / 2. - clear3 / 2.)
    s.last_direction = starting_direction
    CPWStraight(s, 60.0, pinw=0.0, gapw=clear3 / 2.)
    clear4 = 35.0
    s.last = (temp_point[0] + qubit_boxw, temp_point[1] - pad_sep / 2. + clear4 / 2.)
    s.last_direction = starting_direction
    CPWStraight(s, 60.0, pinw=0.0, gapw=clear4 / 2.)

    s.last = (starting_point[0], starting_point[1] - flux_sep1)
    s.last_direction = starting_direction
    CPWLinearTaper(s, flux_taperl, start_pinw=fpinw, stop_pinw=flux_pinw, start_gapw=fgapw, stop_gapw=flux_length)
    s.last = (starting_point[0] + qubit_boxw + 2 * flux_pinw + flux_taperl, starting_point[1] + flux_sep2)
    s.last_direction = starting_direction


def StackJuncCapPads(structure, i, qubit_boxw=40.0, fpinw=cpw_pinw, fgapw=cpw_gapw, squ=0):
    # Capacitor pads for resonator
    # Holds one inductor
    # Even spacing
    # Space for E-beam pattern

    qubit_capl = 150.0
    qubit_capw = 50.0
    flux_sep1 = 10.0 - 2.
    flux_sep2 = 20.0 - 5.8
    flux_pinw = 3.0
    flux_taperl = 100.0
    flux_length = 30.0
    pad_sep = 118.0

    border = 30.0
    gap = 20.0
    gap_stop = 9.2
    taper_stop = border + (gap - gap_stop) / 2.0

    s = structure
    starting_point = (s.last[0], s.last[1] + flux_sep1)
    starting_direction = s.last_direction

    structure.last = (s.last[0] + flux_pinw + flux_taperl, starting_point[1])
    temp_point = s.last

    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 5., starting_point[1] + pad_sep / 2.)
    s.last_direction = starting_direction + 90
    if not i % 2 == 0:
        CoupPad(s, padw=qubit_capw, padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=gap, connecl=50.0,
                gapw=30.0, connecgapw=border, coupstart=0, square=squ)
    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 5.0, starting_point[1] + 59.0)

    s.last_direction = starting_direction - 90

    CPWLinearTaper(c.s2, 50.0, start_pinw=gap, stop_pinw=gap_stop, start_gapw=border, stop_gapw=taper_stop)
    CPWStraight(c.s2, 80.0, pinw=gap_stop, gapw=taper_stop)
    CPWLinearTaper(c.s2, 50.0, start_pinw=gap_stop, stop_pinw=gap, start_gapw=taper_stop, stop_gapw=border)
    if i % 2 == 0:
        CoupPad(s, padw=qubit_capw, padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=gap, connecl=50.0,
                gapw=30.0, connecgapw=border, coupstart=0, square=squ)


def StackJuncCapPads2(structure, qubit_boxw=40.0, fpinw=cpw_pinw, fgapw=cpw_gapw, squ=0):
    # Capacitor pads for resonator
    # Holds a pair of inductors
    # Even spacing
    # Space for E-beam pattern

    qubit_capl = 150.0
    qubit_capw = 50.0
    flux_sep1 = 10.0 - 2.
    flux_sep2 = 20.0 - 5.8
    flux_pinw = 3.0
    flux_taperl = 100.0
    flux_length = 30.0
    pad_sep = 118.0

    border = 30.0
    gap = 20.0
    flux_line_sep = 3.0

    s = structure
    starting_point = (s.last[0], s.last[1] + flux_sep1)
    starting_direction = s.last_direction

    structure.last = (s.last[0] + flux_pinw + flux_taperl, starting_point[1])
    temp_point = s.last

    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 5., starting_point[1] + pad_sep / 2.)
    s.last_direction = starting_direction + 90
    #    CoupPad(s,padw=qubit_capw,padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=gap,connecl=50.0,gapw=30.0,connecgapw=border,coupstart=0,square=squ)
    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 5.0, starting_point[1] + 59.0)

    s.last_direction = starting_direction - 90

    CPWLinearTaper(s, 50.0, start_pinw=gap, stop_pinw=gap, start_gapw=border, stop_gapw=border)
    # set center point
    center_pt = s.last

    # draw left side
    left_pt = (center_pt[0] - (border + gap) / 2.0, center_pt[1])
    s.last = left_pt
    CPWStraight(s, 99.5, pinw=0.0, gapw=border / 2.0)

    # draw right side
    right_pt = (center_pt[0] + (border + gap) / 2.0, center_pt[1])
    s.last = right_pt
    CPWStraight(s, 60.5, pinw=0.0, gapw=border / 2.0)
    s.last = (right_pt[0] - border / 2.0 + flux_line_sep / 2.0, s.last[1])
    CPWStraight(s, 39.0, pinw=0.0, gapw=1.5)

    # return to center
    s.last = (center_pt[0], center_pt[1] - 80.0 - 19.5)
    CPWLinearTaper(s, 82.5 - 50.0, start_pinw=gap, stop_pinw=gap, start_gapw=border, stop_gapw=border)

    CoupPad(s, padw=qubit_capw, padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=gap, connecl=50.0,
            gapw=30.0, connecgapw=border, coupstart=0, square=squ)


def StackJuncCapPadsFlux(structure, qubit_boxw=40.0, fpinw=cpw_pinw, fgapw=cpw_gapw, squ=0):
    # Capacitor pads for Fluxonium
    # Holds a pair of inductors
    # Even spacing
    # Space for E-beam pattern

    qubit_capl = 200.0
    qubit_capw = 50.0
    flux_sep1 = 10.0 - 2.
    flux_sep2 = 20.0 - 5.8
    flux_pinw = 3.0
    flux_taperl = 100.0
    flux_length = 15.0
    pad_sep = 118.0

    border = 30.0
    ebeam_pinw = 20.0

    s = structure
    starting_point = (s.last[0], s.last[1] + flux_sep1 - 17.5)
    starting_direction = s.last_direction

    structure.last = (s.last[0] + flux_pinw + flux_taperl, starting_point[1])
    temp_point = s.last

    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 7.0, starting_point[1] + pad_sep / 2.)
    s.last_direction = starting_direction + 90

    CoupPad(s, padw=qubit_capw, padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=ebeam_pinw, connecl=50.0,
            gapw=30.0, connecgapw=border, coupstart=0, square=squ)
    s.last = (starting_point[0] + qubit_boxw / 2. + flux_pinw + flux_taperl - 7.0, starting_point[1] + 59.0)
    s.last_direction = starting_direction - 90
    center_pt = s.last

    # left side
    right_pt = (center_pt[0] - (ebeam_pinw + border) / 2.0, center_pt[1])
    s.last = right_pt
    CPWStraight(s, 17.0 - 1.7 + 42.0 - 18.0 + 0.2, pinw=0.0, gapw=border / 2)
    #    s.last = (s.last[0]-5.0,s.last[1])
    #    CPWStraight(s,42.0-18.0+0.2,pinw=0.0,gapw=(border)/2)
    s.last = (right_pt[0], s.last[1])
    CPWStraight(s, 19.5, pinw=0.0, gapw=border / 2.0)
    s.last = center_pt

    # right Side
    left_pt = (center_pt[0] + (ebeam_pinw + border) / 2.0, center_pt[1])
    s.last = left_pt
    #    CPWStraight(s,5.0,pinw=0.0,gapw=border/2.0)
    s.last = (s.last[0] - border / 2.0 + flux_pinw / 2.0 + 8.0, s.last[1])
    temp_pt = (s.last[0] + (3.0 + 19.0) / 2.0, s.last[1])
    CPWStraight(s, 39.0 + 4.7 + 10.3 + 5.0, pinw=0.0, gapw=1.5)
    ref_pt = s.last
    s.last = temp_pt
    CPWStraight(s, 20.0, pinw=0.0, gapw=19.0 / 2.0)
    s.last = ref_pt
    s.last = (left_pt[0] - 9.5, s.last[1])
    #    CPWStraight(s,19.5,pinw=0.0,gapw=11.0/2.0)
    s.last = (center_pt[0], center_pt[1] - 59.0)

    #    CPWStraight(s,100.0,pinw=20.0,gapw=10.0)

    CoupPad(s, padw=qubit_capw, padl=qubit_capw, girdle_l=qubit_capl, corner_rad=10, connecw=ebeam_pinw, connecl=50.0,
            gapw=30.0, connecgapw=border, coupstart=0, square=squ)

    s.last = (starting_point[0] + 70.0 + 70.0, starting_point[1] - flux_sep1 + 17.5 + 10.0)
    s.last_direction = starting_direction
    CPWLinearTaper(s, 30.0, start_pinw=flux_pinw, stop_pinw=fpinw, start_gapw=flux_length, stop_gapw=fgapw)


def StackJuncEbeamPads(structure, numpads, pad_x, pad_y, sep_x, sep_y, overlap, horizontal=1, even=1):
    '''
    Base layer pads to connect stacks
    numpads: number of pads on left (starting) side
    direction: determines horizontal or vertical direction for evap stacks
    even: even length between chains
    '''
    s = structure
    start_pt = (s.last[0], s.last[1])
    start_dir = s.last_direction
    num_pads = numpads - 1

    for i in range(num_pads):
        CPWStraight(s, pad_y, pinw=pad_x, gapw=sep_x / 2.0)
        CPWStraight(s, sep_y, pinw=0.0, gapw=(sep_x + pad_x) / 2.0)
    CPWStraight(s, pad_y, pinw=pad_x, gapw=sep_x / 2.0)

    if horizontal:
        s.last = (start_pt[0] + 6.6, start_pt[1])
    else:
        s.last = (start_pt[0], start_pt[1] + 6.6)

    CPWStraight(s, (pad_y - overlap), pinw=0.0, gapw=(sep_x + pad_x) / 2.0)
    for i in range(num_pads):
        CPWStraight(s, pad_y, pinw=pad_x, gapw=sep_x / 2.0)
        CPWStraight(s, sep_y, pinw=0.0, gapw=(sep_x + pad_x) / 2.0)
    if even:
        CPWStraight(s, overlap, pinw=0.0, gapw=(sep_x + pad_x) / 2.0)


def StackJuncEbeamPads0Pi(structure, numpads, pad_x, pad_y, sep_x, sep_y, pad_border, overlap, horizontal=1, even=1):
    '''
    Base layer pads to connect stacks
    numpads: number of pads on left (starting) side
    direction: determines horizontal or vertical direction for evap stacks
    even: even length between chains
    '''
    s = structure
    start_pt = (s.last[0], s.last[1])
    start_dir = 90.0
    num_pads = numpads - 1

    gap_x = sep_x - 2 * pad_border

    for i in range(num_pads):
        CPWStraight(s, pad_y, pinw=pad_x, gapw=pad_border)
        CPWStraight(s, sep_y, pinw=0.0, gapw=(2 * pad_border + pad_x) / 2.0)
    end_pt = s.last
    s.last = (start_pt[0] + pad_x / 2. + pad_border + gap_x / 2., start_pt[1])
    gap_y = end_pt[1] - start_pt[1]
    CPWStraight(s, gap_y, pinw=0.0, gapw=gap_x / 2.)

    if horizontal:
        s.last = (start_pt[0] + (pad_x + sep_x), start_pt[1])
    else:
        s.last = (start_pt[0], start_pt[1] + (pad_x + sep_x))

    CPWStraight(s, (pad_y - overlap), pinw=0.0, gapw=(2 * pad_border + pad_x) / 2.0)
    end1_pt = s.last
    for i in range(num_pads - 1):
        CPWStraight(s, pad_y, pinw=pad_x, gapw=pad_border)
        CPWStraight(s, sep_y, pinw=0.0, gapw=(2 * pad_border + pad_x) / 2.0)
    end1_pt = s.last
    if even:
        s.last = (s.last[0], s.last[1] + 0.2 + sep_y)
        height = (end1_pt[1] - end_pt[1])
        CPWStraight(s, height, pinw=0.0, gapw=pad_border + pad_x / 2.)


def StackJuncEbeamLayer2(structure, numpads, undercut_x, undercut_y, junc_x, junc_y, horizontal=1, even=1, sign=-1):
    '''
    Base layer pads to connect stacks
    numpads: number of pads on left (starting) side
    direction: determines horizontal or vertical direction for evap stacks
    even: even length between chains
    '''
    s = structure
    start_pt = (s.last[0], s.last[1])
    gap_start_pt = start_pt
    s.gap_layer.last = gap_start_pt
    pin_start_pt = start_pt
    s.pin_layer.last = pin_start_pt
    start_dir = s.last_direction
    s.pin_layer_direction = start_direction
    s.gap_layer_direction = start_direction
    num_pads = numpads - 1

    # draw left undercut
    ref_pt = s.gap_layer.last
    s.gap_layer.last = (gap_start_pt[0] + 0.075, gap_start_pt[1] + sign * 0.375)
    for i in range(2 * num_pads):
        CPWStraight(s.gap_layer, undercut_y, pinw=0.0, gapw=undercut_x / 2.0)
        s.gap_layer.last = (gap_start_pt[0] + 0.075, s.gap_layer.last[1] + sign * 0.15)
    s.gap_layer.last = ref_pt

    # draw junctions
    ref_pt = s.pin_layer.last
    s.pin_layer.last = (pin_start_pt[0] + 3.3, pin_start_pt[1] + sign * 0.39)
    for i in range(2 * num_pads):
        CPWStraight(s.pin_layer, junc_y, pinw=0.0, gapw=junc_x / 2.0)
        s.pin_layer.last = (start_pt[0] + 3.3, s.pin_layer.last[1] + sign * 0.18)
    s.pin_layer.last = ref_pt

    if horizontal:
        s.last = (start_pt[0] + 6.6, start_pt[1])
    else:
        s.last = (start_pt[0], start_pt[1] + 6.6)

    # draw right undercut
    ref_pt = s.gap_layer.last
    s.gap_layer.last = (gap_start_pt[0] + 6.6 - 0.075, gap_start_pt[1] + sign * 0.375)
    for i in range(2 * num_pads):
        CPWStraight(s.gap_layer, undercut_y, pinw=0.0, gapw=undercut_x / 2.0)
        s.gap_layer.last = (gap_start_pt[0] + 6.6 - 0.075, s.gap_layer.last[1] + sign * 0.15)
    s.gap_layer.last = ref_pt


def StackJuncEbeamLayer2_Nate(structure, start_point=(0, 0), junc_sep=0.2, juncw=5.5, juncl=0.2, undercutw=1.0,
                              undercutl=0.25, junc_number=10):
    s = structure
    start_direction = 90
    s.pin_layer.last = start_point
    s.pin_layer.last_direction = start_direction
    s.gap_layer.last_direction = start_direction
    s.gap_layer.last = start_point
    for i in range(junc_number):
        CPWStraight(s.pin_layer, juncl, pinw=0, gapw=juncw / 2.)
        ref_point = s.pin_layer.last
        s.gap_layer.last = (s.pin_layer.last[0], s.pin_layer.last[1] - juncl - (abs(juncl - undercutl) / 2.))
        CPWStraight(s.gap_layer, undercutl, pinw=juncw, gapw=undercutw)
        s.pin_layer.last = (ref_point[0], ref_point[1] + junc_sep)


def StackJuncEbeamLayer2_Sim(structure, start_point=(0, 0), junc_sep=0.2, juncw=5.5, juncl=0.2, undercutw=1.0,
                             undercutl=0.25, junc_number=10):
    s = structure
    start_direction = 90
    for i in range(junc_number):
        CPWStraight(s, juncl, pinw=0, gapw=juncw / 2.)
        ref_point = s.last
        s.last = (ref_point[0], ref_point[1] + junc_sep)


def StackJuncEbeamFlux(structure, junc_x, junc_y, pad_x, pad_y, sep_x, sep_y, overlap):
    '''
    Draws the fluxonium circuit with stack junctions

    in_x: width of lead from cap pads
    in_y: length of input lead
    out_y: length of output lead

    tab1_y: length of tab 1
    tab_x: width of tabs
    tab2_y: length of tab 2

    junc_x: width of small Josephson junction
    junc_y: length of small Josephson junction

    pad_x: width of inductor base
    pad_y: length of inductor base
    sep_x: x separation between inductor pads
    sep_y: y separation between inductor pads

    '''

    in_x = 4.0
    in_dx = 3.0
    in_dy = 0.8
    in_y = 11.8
    out_y = 9.2

    tab_x = junc_x
    tab1_y = 2.0
    tab2_y = 2.0

    tab_sep = (tab1_y - in_dy) + junc_y

    borderw = 4 * (sep_x + pad_x)
    borderh = 3.0

    s = structure
    start_pt = (s.last[0] + in_x + (in_dx / 2.0), s.last[1])
    s.last = start_pt
    # draw input:
    CPWStraight(s, in_y, pinw=0.0, gapw=(in_dx / 2.0))
    # draw output:
    s.last = (s.last[0], s.last[1] - (2 * in_dy) - tab_sep)
    CPWStraight(s, out_y, pinw=0.0, gapw=(in_dx / 2.0))
    # draw separation:
    s.last = (start_pt[0] - (in_x / 2.0) - 0.5, start_pt[1] - in_y - in_dy)
    CPWStraight(s, tab_sep, pinw=0.0, gapw=(in_x + in_dx + 1.0) / 2.0)
    s.last = (start_pt[0] - (in_x / 2.0) + (in_x + in_dx) / 2.0 + (junc_x / 2.0), s.last[1] + junc_y)
    CPWStraight(s, junc_y, pinw=0.0, gapw=junc_x / 2.0)
    # draw inductor:
    s.last = (s.last[0] + (tab_x - pad_x) - 0.1, s.last[1] - in_dy - tab2_y)
    # chain 1
    box_stop = s.last[1]
    StackJuncEbeamPads(s, 9, pad_x, pad_y, sep_x, sep_y, overlap, horizontal=1, even=0)  # +13 junctions
    s.last = (s.last[0] - (sep_x + pad_x), s.last[1] - overlap)
    CPWStraight(s, pad_y, pinw=0.0, gapw=(sep_x + pad_x) / 2.0)
    s.last = (s.last[0] + (sep_x + pad_x), s.last[1] + overlap + pad_y)
    CPWStraight(s, pad_y, pinw=pad_x, gapw=sep_x / 2.0)  # +1 junction
    CPWStraight(s, overlap, pinw=0.0, gapw=(sep_x + pad_x) / 2.0)
    bottom_pt = s.last
    # chain 2
    s.last_direction = s.last_direction + 180.0
    s.last = (s.last[0] + 3 * (sep_x + pad_x) / 2.0, s.last[1])
    CPWStraight(s, overlap, pinw=0.0, gapw=(sep_x + pad_x))
    s.last = (s.last[0] - (sep_x + pad_x) / 2.0, s.last[1])
    StackJuncEbeamPads(s, 28, pad_x, pad_y, sep_x, sep_y, overlap, horizontal=1, even=1)  # +58 junctions
    s.last = (s.last[0] - 3 * (sep_x + pad_x) / 2.0, s.last[1])
    top_pt = s.last
    CPWStraight(s, sep_y, pinw=0.0, gapw=2 * (sep_x + pad_x))
    # chain 3
    s.last_direction = s.last_direction + 180.0
    s.last = (s.last[0] - (sep_x + pad_x) / 2.0, s.last[1] - sep_y)
    CPWStraight(s, pad_y, pinw=pad_x, gapw=sep_x / 2.0)  # +2 junction

    s.last = (s.last[0] - sep_x - pad_x, s.last[1] + pad_y)
    CPWStraight(s, pad_y - overlap, pinw=0.0, gapw=(sep_x + pad_x) / 2.0)
    CPWStraight(s, overlap, pinw=pad_x, gapw=(sep_x) / 2.0)
    StackJuncEbeamPads(s, 14, pad_x, pad_y, sep_x, sep_y, overlap, horizontal=1, even=1)  # +26 junctions
    # fill center
    box_start = s.last[1]
    dx = -(sep_x + pad_x / 2.0) + ((3 * sep_x / 2 + pad_x) / 2.0)
    s.last = (s.last[0] + dx, s.last[1])
    CPWStraight(s, (box_start - box_stop), pinw=0.0, gapw=((3 * sep_x / 2 + pad_x) / 2.0))
    # draw top border
    s.last_direction = s.last_direction + 180.0
    s.last = top_pt
    CPWStraight(s, borderh, pinw=0.0, gapw=borderw / 2.0)
    s.last_direction = s.last_direction - 180.0
    # draw bottom border
    bottom_pt = (bottom_pt[0] + (sep_x + pad_x) / 2.0, bottom_pt[1])
    s.last = bottom_pt
    CPWStraight(s, borderh, pinw=0.0, gapw=borderw / 2.0)


def StackJuncEbeamFluxLayer2(structure, start_pt, junc_x, junc_y, pad_x, pad_y, sep_x, sep_y, overlap, stack_x, stack_y,
                             stack_undercut_x, stack_undercut_y, junc_sep):
    '''
    Draws the fluxonium circuit with stack junctions

    in_x: width of lead from cap pads
    in_y: length of input lead
    out_y: length of output lead

    tab1_y: length of tab 1
    tab_x: width of tabs
    tab2_y: length of tab 2

    junc_x: width of small Josephson junction
    junc_y: length of small Josephson junction

    pad_x: width of inductor base
    pad_y: length of inductor base
    sep_x: x separation between inductor pads
    sep_y: y separation between inductor pads

    '''

    in_x = 4.0
    in_dx = 3.0
    in_dy = 0.8
    in_y = 11.8
    out_y = 9.2

    tab_x = junc_x
    tab1_y = 2.0
    tab2_y = 2.0

    tab_sep = (tab1_y - in_dy) + junc_y

    borderw = 4 * (sep_x + pad_x)
    borderh = 3.0

    dx = pad_sep_x + pad_x
    dy = junc_sep + stack_y

    num_stacks1 = 17
    num_stacks2 = 54
    num_stacks3 = 26

    s = structure
    start_pt = (s.last[0] + in_x + (in_dx / 2.0), s.last[1])
    s.last = start_pt

    StackJuncEbeamLayer2_Nate(structure, start_point=s.last, junc_sep=stack_sep, juncw=stack_x, juncl=stack_y,
                              undercutw=stacku_x, undercutl=stacku_y, junc_number=num_stacks1)
    s.last = (s.last[0] + dx, s.last[1] - dy)
    StackJuncEbeamLayer2_Nate(structure, start_point=s.last, junc_sep=stack_sep, juncw=stack_x, juncl=stack_y,
                              undercutw=stacku_x, undercutl=stacku_y, junc_number=1)
    s.last = (s.last[0] + dx, s.last[1] + dy)
    StackJuncEbeamLayer2_Nate(structure, start_point=s.last, junc_sep=stack_sep, juncw=stack_x, juncl=stack_y,
                              undercutw=stacku_x, undercutl=stacku_y, junc_number=num_stacks2)
    s.last = (s.last[0] - dx, s.last[1] + (dy * num_stacks2))
    StackJuncEbeamLayer2_Nate(structure, start_point=s.last, junc_sep=stack_sep, juncw=stack_x, juncl=stack_y,
                              undercutw=stacku_x, undercutl=stacku_y, junc_number=1)
    s.last = (s.last[0] - dx, s.last[1] - dy)
    StackJuncEbeamLayer2_Nate(structure, start_point=s.last, junc_sep=stack_sep, juncw=stack_x, juncl=stack_y,
                              undercutw=stacku_x, undercutl=stacku_y, junc_number=1)
    s.last = (s.last[0], s.last[1] - (dy * num_stacks3) - overlap)
    StackJuncEbeamLayer2_Nate(structure, start_point=s.last, junc_sep=stack_sep, juncw=stack_x, juncl=stack_y,
                              undercutw=stacku_x, undercutl=stacku_y, junc_number=num_stacks3)

    s.last = start_pt
    s.last = (s.last[0] - 3.4, s.last[1] + (dy * num_stacks1 + 1.51))
    s.pin_layer.last = s.last
    s.gap_layer.last = s.last
    CPWStraight(s.pin_layer, 1.0, pinw=0, gapw=0.4)
    CPWStraight(s.pin_layer, 0.5, pinw=0, gapw=0.15 / 2)
    s.gap_layer.last = s.pin_layer.last
    CPWStraight(s.gap_layer, 1.0, pinw=0, gapw=0.45)
    s.pin_layer.last = s.gap_layer.last
    CPWStraight(s.pin_layer, 0.5, pinw=0, gapw=0.15 / 2)
    CPWStraight(s.pin_layer, 1.0, pinw=0, gapw=0.4)


def StackJuncEbeamFlux2(structure, junc_x, junc_y, pad_x, pad_y, sep_x, sep_y, draw_Ebeam2=1):
    '''
    Draws the fluxonium circuit with stack junctions

    in_x: width of lead from cap pads
    in_y: length of input lead
    out_y: length of output lead

    tab1_y: length of tab 1
    tab_x: width of tabs
    tab2_y: length of tab 2

    junc_x: width of small Josephson junction
    junc_y: length of small Josephson junction

    pad_x: width of inductor base
    pad_y: length of inductor base
    sep_x: x separation between inductor pads
    sep_y: y separation between inductor pads

    '''

    in_x = 4.0
    in_dx = 3.0
    in_dy = 0.8
    in_y = 11.8
    out_y = 10.0

    tab_x = junc_x
    tab1_y = 1.0
    tab2_y = 3.6

    tab_sep = (tab1_y - in_dy) + junc_y

    borderw = 4 * (sep_x + pad_x)
    borderh = 3.0

    s = structure
    start_pt = (s.last[0] + in_x + (in_dx / 2.0), s.last[1])
    s.last = start_pt

    # draw separation:
    s.last = (start_pt[0] - (in_x / 2.0) + (in_x + in_dx) / 2.0 + (junc_x / 2.0), start_pt[1] - in_y - in_dy + junc_y)
    junc_pt = s.last

    # draw inductor:
    s.last = (junc_pt[0] + (tab_x - pad_x) - 0.1, junc_pt[1] - junc_y - in_dy - tab2_y)
    layer2_chain1 = s.last
    layer2_chain1 = (layer2_chain1[0], layer2_chain1[1] - 0.8 - 0.4)
    # chain 1

    if draw_Ebeam2:
        # chain 1
        ref_pt = s.last
        s.last = layer2_chain1
        StackJuncEbeamLayer2(s, 7, 0.95, 0.25, 5.5, 0.22, horizontal=1, even=1, sign=-1)
        gap_pt = (layer2_chain1[0] + 0.075, layer2_chain1[1] - 4.8 - 0.375)
        s.gap_layer.last = gap_pt
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        s.gap_layer.last = (gap_pt[0] + 6.45, gap_pt[1])
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        pin_pt = (layer2_chain1[0] + 3.3, layer2_chain1[1] - 4.8 - 0.375 - 0.015)
        s.pin_layer.last = pin_pt
        CPWStraight(s.pin_layer, 0.22, pinw=0.0, gapw=5.5 / 2.0)
        s.gap_layer.last = (s.gap_layer.last[0] + 0.15, s.gap_layer.last[1] - 0.15)
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        s.gap_layer.last = (s.gap_layer.last[0] + 6.5 - 0.05, s.gap_layer.last[1] + 0.25)
        gap_pt = s.gap_layer.last
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        s.pin_layer.last = (s.pin_layer.last[0] + 6.6, s.pin_layer.last[1] - 0.18)
        pin_pt = s.pin_layer.last
        CPWStraight(s.pin_layer, 0.22, pinw=0.0, gapw=5.5 / 2.0)

        # chain 2
        ref_pt = s.last
        ref_dir = s.last_direction
        s.last = (s.last[0] + 6.6, s.last[1] - 5.8)
        s.last_direction = s.last_direction + 180.0
        StackJuncEbeamLayer2(s, 30, 0.95, 0.25, 5.5, 0.22, horizontal=1, even=1, sign=1)
        s.last_direction = ref_dir
        gap_pt = (gap_pt[0], gap_pt[1] + 23.6)
        s.gap_layer.last = gap_pt
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        gap_pt = (gap_pt[0] - 6.45, gap_pt[1])
        s.gap_layer.last = gap_pt
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        s.gap_layer.last = (gap_pt[0] - 0.15, gap_pt[1] - 0.18 - 0.245 + 0.025)
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        s.gap_layer.last = (gap_pt[0] - 6.6, gap_pt[1] - 0.18 - 0.245 + 0.025)
        CPWStraight(s.gap_layer, 0.25, pinw=0.0, gapw=0.95 / 2.0)
        s.pin_layer.last = (pin_pt[0], pin_pt[1] + 23.6)
        pin_pt = s.pin_layer.last
        CPWStraight(s.pin_layer, 0.22, pinw=0.0, gapw=5.5 / 2.0)
        s.pin_layer.last = (pin_pt[0] - 6.6, pin_pt[1] - 0.4)
        CPWStraight(s.pin_layer, 0.22, pinw=0.0, gapw=5.5 / 2.0)

        # chain 3
        ref_pt = s.last
        s.last = (layer2_chain1[0], layer2_chain1[1] + 17.175 + 0.225)
        StackJuncEbeamLayer2(s, 14, 0.95, 0.25, 5.5, 0.22, horizontal=1, even=1, sign=-1)

        # draw junction
        s.last = ref_pt
        junc_pt = (junc_pt[0], junc_pt[1] - 1.2)
        s.gap_layer.last = junc_pt
        CPWStraight(s.gap_layer, 1.0, pinw=0.0, gapw=0.9 / 2.0)
        s.pin_layer.last = (junc_pt[0], junc_pt[1] + 1.3)
        CPWStraight(s.pin_layer, 1.0, pinw=0.0, gapw=0.8 / 2.0)
        CPWStraight(s.pin_layer, 0.3, pinw=0.0, gapw=0.15 / 2.0)
        s.pin_layer.last = (s.pin_layer.last[0], s.pin_layer.last[1] - 1.0)
        CPWStraight(s.pin_layer, 0.3, pinw=0.0, gapw=0.15 / 2.0)
        CPWStraight(s.pin_layer, 2.0, pinw=0.0, gapw=0.8 / 2.0)


def shot_noise(xpos, ypos, linein_w, dir, top):
    if dir:
        origin = [xpos, ypos]
        c.s2.pin_layer.last = (origin[0], origin[1])
        CPWStraight(c.s2.pin_layer, 6.93, pinw=0., gapw=6.93 / 2.)
        c.s2.pin_layer.last = (origin[0], origin[1] - 6.93)
        CPWStraight(c.s2.pin_layer, 1, pinw=0., gapw=linein_w / 2.)
        c.s2.gap_layer.last = (origin[0] + .4 + linein_w / 2, origin[1] - 6.93)
        CPWStraight(c.s2.gap_layer, 1, pinw=0., gapw=.8 / 2.)
        c.s2.pin_layer.last = (origin[0], origin[1] + 1)
        CPWStraight(c.s2.pin_layer, 1, pinw=0., gapw=linein_w / 2.)
        c.s2.gap_layer.last = (origin[0] - .4 - linein_w / 2, origin[1] + 1)
        CPWStraight(c.s2.gap_layer, 1, pinw=0., gapw=.8 / 2.)
        # sides
        c.s2.gap_layer.last = (origin[0] + 6.93 / 2 + .4, origin[1] + 1)
        CPWStraight(c.s2.gap_layer, 8.93, pinw=0., gapw=.8 / 2.)
        c.s2.gap_layer.last = (origin[0] - 6.93 / 2 - .4, origin[1] + 1)
        CPWStraight(c.s2.gap_layer, 8.93, pinw=0., gapw=.8 / 2.)

        if top:
            c.s2.pin_layer.last = (origin[0], origin[1] + 11)
            CPWLinearTaper(c.s2.pin_layer, 10, start_pinw=0, stop_pinw=0, start_gapw=2.5, stop_gapw=2.5)
        else:
            c.s2.pin_layer.last = (origin[0], origin[1] - 7.93)
            CPWLinearTaper(c.s2.pin_layer, 10, start_pinw=0, stop_pinw=0, start_gapw=2.5, stop_gapw=2.5)
    else:
        origin = [xpos, ypos]
        c.s1.pin_layer.last = (origin[0], origin[1])
        CPWStraight(c.s1.pin_layer, 6.93, pinw=0., gapw=6.93 / 2.)
        c.s1.pin_layer.last = (origin[0] + 6.93, origin[1] - 6.93 + 10 - 3.07)
        CPWStraight(c.s1.pin_layer, 1, pinw=0., gapw=linein_w / 2.)
        c.s1.gap_layer.last = (origin[0] + .4 + 6.38 + .15, origin[1] - 6.93 + 5 + 2.48 + (linein_w - .3) / 2)
        CPWStraight(c.s1.gap_layer, 1, pinw=0., gapw=.8 / 2.)
        c.s1.pin_layer.last = (origin[0] - 1, origin[1] + 1 - 11.5 + 10.95 - .45)
        CPWStraight(c.s1.pin_layer, 1, pinw=0., gapw=linein_w / 2.)
        c.s1.gap_layer.last = (origin[0] - .4 - .6, origin[1] + 1 - 1.55 - (linein_w - .3) / 2)
        CPWStraight(c.s1.gap_layer, 1, pinw=0., gapw=.8 / 2.)

        # sides
        c.s1.gap_layer.last = (origin[0] + 6.93 / 2 + .4 - 4.865, origin[1] + 1 - 4.865)
        CPWStraight(c.s1.gap_layer, 8.93, pinw=0., gapw=.8 / 2.)
        c.s1.gap_layer.last = (origin[0] - 6.93 / 2 - .4 + 2.865, origin[1] + 1 + 2.865)
        CPWStraight(c.s1.gap_layer, 8.93, pinw=0., gapw=.8 / 2.)

        if top:
            c.s1.pin_layer.last = (origin[0] - 6, origin[1])
            CPWLinearTaper(c.s1.pin_layer, 10, start_pinw=0, stop_pinw=0, start_gapw=2.5, stop_gapw=2.5)
        else:
            c.s1.pin_layer.last = (origin[0] + 7.93, origin[1])
            CPWLinearTaper(c.s1.pin_layer, 10, start_pinw=0, stop_pinw=0, start_gapw=2.5, stop_gapw=2.5)


def Stripline(structure, center_pt=(0, 0), stripw=100.0, stripl=12200.0, qstripsep=2342.5, offset=1652.5):
    s = structure
    #    s/.two_layer = 0
    s.last = center_pt
    s.last_direction = 90

    start_pt = (center_pt[0] + stripl / 2.0 + qstripsep, center_pt[1] + offset)
    s.last = start_pt
    CPWStraight(s, stripw, pinw=0.0, gapw=stripl / 2.)
    s.last_direction += -90
    # s.last = center_pt


def TransPadsAssym(structure, center_pt=(0, 0), padw=250.0, padh=900.0, taperw=40.0, leadw1=450.0, leadw2=450.0,
                   leadh=20.0, qugap=20.0):
    s = structure
    #    s/.two_layer = 0
    # s = structure.pin_layer
    s.last = center_pt
    s.last_direction = 90

    start_pt = (center_pt[0] - qugap / 2. - leadw1 - taperw - padw, center_pt[1])
    s.last = start_pt
    CPWStraight(s, padw, pinw=0., gapw=padh / 2.)
    CPWLinearTaper(s, taperw, start_pinw=0.0, stop_pinw=0.0, start_gapw=padh / 2., stop_gapw=leadh / 2.)
    CPWStraight(s, leadw1, pinw=0.0, gapw=leadh / 2.)

    return_pt = s.last
    return_dir = s.last_direction

    s.last_direction += 180
    CPWLinearTaper(s, 1.0, start_pinw=0.0, stop_pinw=0.0, start_gapw=1.0, stop_gapw=2.0)
    s.last_direction += 180

    s.last = (return_pt[0], return_pt[1] + qugap)
    s.last_direction = return_dir

    return_pt = s.last

    CPWLinearTaper(s, 1.0, start_pinw=0.0, stop_pinw=0.0, start_gapw=1.0, stop_gapw=2.0)

    s.last_direction += 180
    s.last = return_pt
    s.last_direction += 180
    CPWStraight(s, leadw2, pinw=0.0, gapw=leadh / 2.)
    CPWLinearTaper(s, taperw, start_pinw=0.0, stop_pinw=0.0, start_gapw=leadh / 2., stop_gapw=padh / 2.)
    CPWStraight(s, padw, pinw=0., gapw=padh / 2.)
    s.last_direction += 180


def para_squidA(structure, xpos, ypos, con_len, side_push, sep):
    c = structure
    # SQUIDS e.g. xpos = 3300, ypos = 2325

    # Line-in to cap pads
    c.s2.pin_layer.last = (xpos, ypos + 0.2 * con_pin_l)
    CPWStraight(c.s2.pin_layer, con_pin_l, pinw=0., gapw=cpw_pinw / 2.)

    # Bottom capacitor pads
    c.s2.pin_layer.last = (xpos + cap_botm_x / 2 - cpw_pinw / 2., c.s2.pin_layer.last[1])
    CPWStraight(c.s2.pin_layer, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

    c.s2.pin_layer.last = (xpos + cap_botm_x / 2 - cpw_pinw / 2., c.s2.pin_layer.last[1] - cap_sep)
    CPWStraight(c.s2.pin_layer, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

    # Line-out cap to gnd
    c.s2.pin_layer.last = (xpos, c.s2.pin_layer.last[1])
    CPWStraight(c.s2.pin_layer, con_pin_l, pinw=0., gapw=cpw_pinw / 2.)

    junc_w = 0.6
    junc_l = 4.0
    loop_w = 8.0
    loop_h = 3.0
    gap = 0.5

    xpos = xpos + cap_botm_x - cpw_pinw / 2 + loop_w
    # ypos = move to center and then top offset.
    ypos = ypos - 0.8 * con_pin_l - cap_botm_y - cap_sep / 2 + (gap / 2 + loop_h + junc_l) - junc_l / 2

    # Top C
    c.s2.pin_layer.last = (xpos, ypos + junc_l / 2.)
    CPWStraight(c.s2.pin_layer, junc_l, pinw=0., gapw=(loop_w + 2 * junc_l) / 2.)

    c.s1.last_direction += -90

    c.s1.pin_layer.last = (xpos - (loop_w + junc_l) / 2., ypos - junc_l / 2.)
    CPWStraight(c.s1.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

    c.s1.pin_layer.last = (xpos + (loop_w + junc_l) / 2, ypos - junc_l / 2.)
    CPWStraight(c.s1.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

    # Bottom C
    c.s1.pin_layer.last = (xpos - (loop_w + junc_l) / 2., ypos - junc_l / 2. - gap - loop_h)
    CPWStraight(c.s1.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

    c.s1.pin_layer.last = (xpos + (loop_w + junc_l) / 2, ypos - junc_l / 2. - gap - loop_h)
    CPWStraight(c.s1.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

    c.s2.pin_layer.last = (xpos, ypos - junc_l / 2. - gap - 2 * loop_h)
    CPWStraight(c.s2.pin_layer, junc_l, pinw=0., gapw=(loop_w + 2 * junc_l) / 2.)

    c.s1.last_direction += +90

    ####### Undercut#######

    # Inner Top
    c.s2.gap_layer.last = (xpos, ypos - junc_l / 2.)
    CPWStraight(c.s2.gap_layer, 0.5, pinw=0., gapw=loop_w / 2.)

    # Dolan Bridge
    c.s2.gap_layer.last = (xpos - (loop_w + junc_l) / 2., ypos - junc_l / 2. - loop_h)
    CPWStraight(c.s2.gap_layer, gap, pinw=0., gapw=(junc_l + 2 * gap) / 2.)

    c.s2.gap_layer.last = (xpos + (loop_w + junc_l) / 2., ypos - junc_l / 2. - loop_h)
    CPWStraight(c.s2.gap_layer, gap, pinw=0., gapw=(junc_l + 2 * gap) / 2.)

    # Inner Bottom
    c.s2.gap_layer.last = (xpos, ypos - junc_l / 2. - gap - 2 * loop_h)
    CPWStraight(c.s2.gap_layer, -0.5, pinw=0., gapw=loop_w / 2.)


def para_squidA_test(structure, xpos, ypos, junc_l, gap, loop_h, loop_w):
    c = structure

    cap_botm_x = 1000
    cap_botm_y = 400

    if etching == True:
        # Bottom capacitor pads for an etching process on a metalic wafer
        if draw_layer1 == True and draw_layer2 == True:
            # Top patch 50% of cap_botm_y
            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, ypos + cap_botm_y / 2)
            CPWStraight(c.s2.pin_layer, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Middle patch width = cap_sep
            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, c.s2.pin_layer.last[1] - cap_botm_y)
            CPWStraight(c.s2.pin_layer, cap_sep, pinw=0., gapw=cap_botm_x / 2.)

            # Bottom patch 50% of cap_botm_y
            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, c.s2.pin_layer.last[1] - cap_botm_y)
            CPWStraight(c.s2.pin_layer, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Left patch
            c.s2.pin_layer.last = (xpos - 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2.pin_layer, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

            # Right patch
            c.s2.pin_layer.last = (xpos + cap_botm_x + 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2.pin_layer, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

        if draw_layer1 == True and draw_layer2 == False:
            # Top patch 50% of cap_botm_y
            c.s2.last = (xpos + cap_botm_x / 2, ypos + cap_botm_y / 2)
            CPWStraight(c.s2, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Middle patch width = cap_sep
            c.s2.last = (xpos + cap_botm_x / 2, c.s2.last[1] - cap_botm_y)
            CPWStraight(c.s2, cap_sep, pinw=0., gapw=cap_botm_x / 2.)

            # Bottom patch 50% of cap_botm_y
            c.s2.last = (xpos + cap_botm_x / 2, c.s2.last[1] - cap_botm_y)
            CPWStraight(c.s2, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Left patch
            c.s2.last = (xpos - 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

            # Right patch
            c.s2.last = (xpos + cap_botm_x + 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

    else:
        # etching = False
        # Bottom capacitor pads for a deposition process on a bare wafer
        if draw_layer1 == True and draw_layer2 == True:
            c.s2new.pin_layer.last = (xpos + cap_botm_x / 2, ypos)
            CPWStraight(c.s2.pin_layer, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, c.s2.pin_layer.last[1] - cap_sep)
            CPWStraight(c.s2.pin_layer, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)
        elif draw_layer1 == True and draw_layer2 == False:
            c.s2.last = (xpos + cap_botm_x / 2, ypos)
            CPWStraight(c.s2, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

            c.s2.last = (xpos + cap_botm_x / 2, c.s2.last[1] - cap_sep)
            CPWStraight(c.s2, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

    if draw_layer2 == True:
        xpos = xpos - 0 * cap_botm_x - loop_w / 2 - junc_l + 3  # 3 um offset for overlap
        # ypos = move to center and then top offset.
        ypos = ypos - 0 * con_pin_l - cap_botm_y - cap_sep / 2 + (gap / 2 + loop_h + junc_pad_y) - junc_pad_y / 2

        # Top C
        c.s2.pin_layer.last = (xpos, ypos + junc_pad_y / 2.)
        CPWStraight(c.s2.pin_layer, junc_pad_y, pinw=0., gapw=(loop_w + 2 * junc_l) / 2.)

        c.s2.pin_layer.last = (xpos - (loop_w + junc_l) / 2., ypos - junc_pad_y / 2.)
        CPWStraight(c.s2.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

        c.s2.pin_layer.last = (xpos + (loop_w + junc_l) / 2, ypos - junc_pad_y / 2.)
        CPWStraight(c.s2.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

        # Bottom C
        c.s2.pin_layer.last = (xpos - (loop_w + junc_l) / 2., ypos - junc_pad_y / 2. - gap - loop_h)
        CPWStraight(c.s2.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

        c.s2.pin_layer.last = (xpos + (loop_w + junc_l) / 2, ypos - junc_pad_y / 2. - gap - loop_h)
        CPWStraight(c.s2.pin_layer, loop_h, pinw=0., gapw=junc_l / 2.)

        c.s2.pin_layer.last = (xpos, ypos - junc_pad_y / 2. - gap - 2 * loop_h)
        CPWStraight(c.s2.pin_layer, junc_pad_y, pinw=0., gapw=(loop_w + 2 * junc_l) / 2.)

        ####### Undercut #######

        # Inner Top
        c.s2.gap_layer.last = (xpos, ypos - junc_pad_y / 2.)
        CPWStraight(c.s2.gap_layer, 0.5, pinw=0., gapw=loop_w / 2.)

        # Dolan Bridge
        c.s2.gap_layer.last = (xpos - (loop_w + junc_l) / 2., ypos - junc_pad_y / 2. - loop_h)
        CPWStraight(c.s2.gap_layer, gap, pinw=0., gapw=(junc_l + 2 * gap) / 2.)

        c.s2.gap_layer.last = (xpos + (loop_w + junc_l) / 2., ypos - junc_pad_y / 2. - loop_h)
        CPWStraight(c.s2.gap_layer, gap, pinw=0., gapw=(junc_l + 2 * gap) / 2.)

        # Inner Bottom
        c.s2.gap_layer.last = (xpos, ypos - junc_pad_y / 2. - gap - 2 * loop_h)
        CPWStraight(c.s2.gap_layer, -0.5, pinw=0., gapw=loop_w / 2.)


def test_short(structure, xpos, ypos, junc_l, gap, loop_h, loop_w):
    c = structure

    cap_botm_x = 1000
    cap_botm_y = 400

    if etching == True:
        # Bottom capacitor pads for an etching process on a metalic wafer
        if draw_layer1 == True and draw_layer2 == True:
            # Top patch 50% of cap_botm_y
            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, ypos + cap_botm_y / 2)
            CPWStraight(c.s2.pin_layer, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Middle patch width = cap_sep
            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, c.s2.pin_layer.last[1] - cap_botm_y)
            CPWStraight(c.s2.pin_layer, cap_sep, pinw=0., gapw=cap_botm_x / 2.)

            # Bottom patch 50% of cap_botm_y
            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, c.s2.pin_layer.last[1] - cap_botm_y)
            CPWStraight(c.s2.pin_layer, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Left patch
            c.s2.pin_layer.last = (xpos - 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2.pin_layer, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

            # Right patch
            c.s2.pin_layer.last = (xpos + cap_botm_x + 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2.pin_layer, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

        if draw_layer1 == True and draw_layer2 == False:
            # Top patch 50% of cap_botm_y
            c.s2.last = (xpos + cap_botm_x / 2, ypos + cap_botm_y / 2)
            CPWStraight(c.s2, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Middle patch width = cap_sep
            c.s2.last = (xpos + cap_botm_x / 2, c.s2.last[1] - cap_botm_y)
            CPWStraight(c.s2, cap_sep, pinw=0., gapw=cap_botm_x / 2.)

            # Bottom patch 50% of cap_botm_y
            c.s2.last = (xpos + cap_botm_x / 2, c.s2.last[1] - cap_botm_y)
            CPWStraight(c.s2, cap_botm_y / 2, pinw=0., gapw=1.6 * cap_botm_x / 2)

            # Left patch
            c.s2.last = (xpos - 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

            # Right patch
            c.s2.last = (xpos + cap_botm_x + 0.3 * cap_botm_x / 2, ypos)
            CPWStraight(c.s2, 2 * cap_botm_y + cap_sep, pinw=0., gapw=0.3 * cap_botm_x / 2)

    else:
        # etching = False
        # Bottom capacitor pads for a deposition process on a bare wafer
        if draw_layer1 == True and draw_layer2 == True:
            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, ypos)
            CPWStraight(c.s2.pin_layer, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

            c.s2.pin_layer.last = (xpos + cap_botm_x / 2, c.s2.pin_layer.last[1] - cap_sep)
            CPWStraight(c.s2.pin_layer, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)
        elif draw_layer1 == True and draw_layer2 == False:
            c.s2.last = (xpos + cap_botm_x / 2, ypos)
            CPWStraight(c.s2, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

            c.s2.last = (xpos + cap_botm_x / 2, c.s2.last[1] - cap_sep)
            CPWStraight(c.s2, cap_botm_y, pinw=0., gapw=cap_botm_x / 2.)

    if draw_layer2 == True:
        xpos = xpos - 0 * cap_botm_x - loop_w / 2 - junc_l + 3  # 3 um offset for overlap
        # ypos = move to center and then top offset.
        ypos = ypos - 0 * con_pin_l - cap_botm_y - cap_sep / 2 + (gap / 2 + loop_h + junc_pad_y) - junc_pad_y / 2

        # Top patch
        c.s2.pin_layer.last = (xpos, ypos + junc_pad_y / 2.)
        CPWStraight(c.s2.pin_layer, junc_pad_y, pinw=0., gapw=(loop_w + 2 * junc_l) / 2.)

        # Left patch
        c.s2.pin_layer.last = (xpos - (loop_w + junc_l) / 2., ypos - junc_pad_y / 2.)
        CPWStraight(c.s2.pin_layer, 2 * loop_h + gap, pinw=0., gapw=junc_l / 2.)

        # Right patch
        c.s2.pin_layer.last = (xpos + (loop_w + junc_l) / 2, ypos - junc_pad_y / 2.)
        CPWStraight(c.s2.pin_layer, 2 * loop_h + gap, pinw=0., gapw=junc_l / 2.)

        # Bottom patch
        c.s2.pin_layer.last = (xpos, ypos - junc_pad_y / 2. - gap - 2 * loop_h)
        CPWStraight(c.s2.pin_layer, junc_pad_y, pinw=0., gapw=(loop_w + 2 * junc_l) / 2.)


def draw_square_alignment_marks(structure):
    # alignment boxes for e-beam
    c = structure

    # align_box = 80  # center is the reference
    # c.s2.last = (300, 6300 + align_box / 2)
    # CPWStraight(c.s2, 80, pinw=0, gapw=align_box / 2)
    # c.s2.last = (6300, 6300 + align_box / 2)
    # CPWStraight(c.s2, 80, pinw=0, gapw=align_box / 2)
    # c.s2.last = (300, 300 + align_box / 2)
    # CPWStraight(c.s2, 80, pinw=0, gapw=align_box / 2)
    # c.s2.last = (6300, 300 + align_box / 2)
    # CPWStraight(c.s2, 80, pinw=0, gapw=align_box / 2)
    # c.s2.last = (c.size[0] / 2 - 1900, c.size[1] - 600)


def draw_test_full_transformer(structure, cpw_pinw, cpw_gapw, cpw_pinw1, cpw_pinw2, cpw_gapw1, cpw_gapw2, cpw_rad1,
                               cpw_rad2,
                               lambda4_len, lambda2_len, max_len):
    c = structure
    # ############### Input line #####################
    CPWStraight(c.s3, 100., pinw=cpw_pinw, gapw=cpw_gapw)  # 50 ohm line in, set Y position

    CPWBendNew(c.s3, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=cpw_rad, polyarc=1, segments=4,
               square=square)
    CPWStraight(c.s3, 51.77, pinw=cpw_pinw, gapw=cpw_gapw)  # 50 ohm line, set X position
    CPWLinearTaper(c.s3, taperl, start_pinw=cpw_pinw, stop_pinw=cpw_pinw1, start_gapw=cpw_gapw,
                   stop_gapw=cpw_gapw1)

    # lambda/4 transformer section
    first_len = max_len / 2.0 - cpw_rad - taperl
    DrawMeander(c.s3, cpw_rad1, cpw_pinw1, cpw_gapw1, lambda4_len, max_len, first_len, square)

    CPWLinearTaper(c.s3, taperl, start_pinw=cpw_pinw1, stop_pinw=cpw_pinw2, start_gapw=cpw_gapw1,
                   stop_gapw=cpw_gapw2)

    # lambda/2 transformer section
    first_len = max_len - draw_len - taperl
    DrawMeander(c.s3, cpw_rad2, cpw_pinw2, cpw_gapw2, lambda2_len - np.pi / 2 * cpw_rad2, max_len, first_len,
                square)

    CPWBendNew(c.s3, angle=-90, pinw=cpw_pinw2, gapw=cpw_gapw2, radius=cpw_rad2, polyarc=1, segments=4,
               square=square)

    # Taper to 50 ohm line
    CPWLinearTaper(c.s3, taperl, start_pinw=cpw_pinw2, stop_pinw=cpw_pinw, start_gapw=cpw_gapw2,
                   stop_gapw=cpw_gapw)
    # 50 ohm line
    CPWStraight(c.s3, c.s3.last[1] - c.s8.last[1], pinw=cpw_pinw, gapw=cpw_gapw)


sign = 1
draw_len = 0


def DrawMeander(structure, curr_rad, curr_pinw, curr_gapw, cpw_len, max_len, first_len, square):
    # first_len is the available length for the first straight section
    global sign
    global draw_len
    curr_len = 0
    flag_bend = 0
    count = 1
    print("Draw length = %f" % draw_len)
    print("First length = %f" % first_len)
    while curr_len < cpw_len:
        if flag_bend == 0:
            if count == 1:
                draw_len = min(first_len, cpw_len - curr_len)
            else:
                draw_len = min(max_len, cpw_len - curr_len)
            CPWStraight(structure, draw_len, pinw=curr_pinw, gapw=curr_gapw)
            curr_len = curr_len + draw_len
            flag_bend = 1
        else:
            CPWBendNew(structure, angle=sign * 180, pinw=curr_pinw, gapw=curr_gapw, radius=curr_rad, polyarc=1,
                       segments=4, square=square)
            curr_len = curr_len + np.pi * curr_rad
            draw_len = 0
            sign = sign * (-1)
            flag_bend = 0

        count = count + 1
        print("Current cpw length: %f" % curr_len)


## Function draw_on_chip created by Tanay
def draw_on_chip(structure, d, junc_l, cap_top_x):
    ### JPA junction common parameters
    gap = 0.2
    loop_w = 8.0
    loop_h = 3.0

    c = structure
    # draw_chip_alignment_marks(solid, d, c)
    draw_launchers(c, d, exclude=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ## alignment boxes for e-beam
    if draw_layer1 == True:
        draw_square_alignment_marks(c)

    draw_square_alignment_marks(c)

    # Draw test squids
    para_squidA_test(c, c.s0.last[0] + 500, c.s0.last[1] + 1000, junc_l, gap, loop_h, loop_w)
    para_squidA_test(c, c.s1.last[0] + 500, c.s1.last[1] + 1000, junc_l, gap, loop_h, loop_w)
    para_squidA_test(c, c.s5.last[0] - 1500, c.s5.last[1] + 1000, junc_l, gap, loop_h, loop_w)
    para_squidA_test(c, c.s6.last[0] - 1500, c.s6.last[1] + 1000, junc_l, gap, loop_h, loop_w)
    # Draw test short
    xpos = c.s8.last[0] - 500
    ypos = c.s8.last[1] + 800
    test_short(c, xpos, ypos, junc_l, gap, loop_h, loop_w)

    if draw_layer3 == True:
        c.s0.last = (c.s0.last[0] + 700, c.s0.last[1] + 595)
        CPWStraight(c.s0, cap_top_x, pinw=0, gapw=420)
        c.s1.last = (c.s1.last[0] + 700, c.s1.last[1] + 595)
        CPWStraight(c.s1, cap_top_x, pinw=0, gapw=420)
        c.s5.last = (c.s5.last[0] - 1100, c.s5.last[1] + 595)
        CPWStraight(c.s5, cap_top_x, pinw=0, gapw=420)
        c.s6.last = (c.s6.last[0] - 1100, c.s6.last[1] + 595)
        CPWStraight(c.s6, cap_top_x, pinw=0, gapw=420)

    chip_names.append(c.name)


## Bridge Junction created by Ziqian Li
def RoundLCorner(structure, square, cornerl=10.0, gapw=2.0, whichedge=0):
    # starting point is at the outer corner of a L corner (L corner must have an outer corner)
    # whichedge = 0 or 1 : direction is along one edge or the other

    if whichedge == 0:
        angle = -90
    else:
        angle = 90
    structure.last_direction += angle
    structure.last_direction += angle

    structure.last_direction += angle
    structure.move(cornerl)
    structure.last_direction -= angle
    structure.last_direction += 2 * angle
    structure.move(cornerl * 2)
    structure.last_direction -= 2 * angle
    CPWBendNew(structure, angle=angle, pinw=0, gapw=cornerl, radius=cornerl, polyarc=1, segments=4,
               square=square)
    structure.move(-cornerl * 2)
    CPWStraight(structure, cornerl * 2, pinw=0, gapw=cornerl)


def InductorBox(structure, Inductl=100.0, ipinw=10.0, igapw=10.0, induct_num=2, connecl=50.0, boxgap=50, couptype=0,
                square=0, armlt=410):
    boxl = (2 * induct_num + 2) * (ipinw + 2 * igapw) + 2 * connecl

    Initial_direction = structure.last_direction
    Initial_point = structure.last
    # print boxl
    if couptype == 1:
        structure.move(boxl)
        structure.last_direction += 180

    cpw_pinw = 10.

    rad = igapw + ipinw / 2.
    starting_point = structure.last
    starting_direction = structure.last_direction

    # clear some metal before drawing
    structure.move((connecl + igapw) / 2.)
    structure.move(igapw + ipinw / 2., structure.last_direction - 90)
    structure.last_direction -= 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap, pinw=0, gapw=(igapw + connecl) / 2.)

    # clear some more metal before drawing
    structure.last = starting_point
    structure.last_direction = starting_direction
    structure.move((connecl + igapw + ipinw) / 2.)
    structure.move(ipinw / 2., structure.last_direction + 90)
    structure.last_direction = starting_direction + 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap + igapw, pinw=0, gapw=(connecl + igapw + ipinw) / 2.)

    # more!!!!
    # structure.last=(starting_point[0]-prefac*(connecl+ipinw+2*igapw),starting_point[1]+prefac*(igapw+ipinw/2))
    structure.last = starting_point
    structure.last_direction = starting_direction
    structure.move(connecl + ipinw + 2 * igapw)
    structure.move(igapw + ipinw / 2., structure.last_direction - 90)
    structure.last_direction = starting_direction + 90
    CPWStraight(structure, Inductl / 2. + 3 * rad + boxgap, pinw=0, gapw=igapw)

    # draw the connector
    structure.last = starting_point
    structure.last_direction = starting_direction

    # start to draw the inductors
    CPWStraight(structure, connecl, pinw=ipinw, gapw=igapw)
    CPWBendNew(structure, angle=-90, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
    CPWStraight(structure, Inductl / 2. - rad, pinw=ipinw, gapw=igapw)

    for i in range(induct_num):
        turning_position = structure.last
        turning_direction = structure.last_direction

        # clear metal at one side of the turning positions
        structure.move(igapw + ipinw / 2., turning_direction - 90)
        CPWStraight(structure, 2 * rad + boxgap, pinw=0, gapw=igapw)

        structure.move(-(2 * rad + boxgap - ipinw - igapw) / 2.)
        structure.move(igapw, turning_direction + 90)
        structure.last_direction += 90
        CPWStraight(structure, 2 * (ipinw + igapw), pinw=0, gapw=(2 * rad + boxgap - ipinw - igapw) / 2.)

        # clear metal at the other side
        structure.move(-ipinw)
        structure.move(2 * rad + boxgap + ipinw + igapw + Inductl, structure.last_direction + 90)
        CPWStraight(structure, 2 * (ipinw + igapw), pinw=0, gapw=(2 * rad + boxgap - ipinw - igapw) / 2.)

        structure.move((ipinw + igapw) / 2., structure.last_direction - 90)
        CPWStraight(structure, 2 * igapw, pinw=0, gapw=rad + boxgap / 2.)

        structure.last = turning_position
        structure.last_direction = turning_direction

        # the real deal is here!
        CPWBendNew(structure, angle=180, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
        CPWStraight(structure, Inductl, pinw=ipinw, gapw=igapw)
        CPWBendNew(structure, angle=-180, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
        CPWStraight(structure, Inductl, pinw=ipinw, gapw=igapw)

    turning_position = structure.last
    turning_direction = structure.last_direction

    # keep clearing metal...
    structure.move(igapw + ipinw / 2., turning_direction - 90)
    CPWStraight(structure, 2 * rad + boxgap, pinw=0, gapw=igapw)
    structure.last = turning_position

    structure.move(igapw + ipinw)
    structure.move(igapw + ipinw / 2., turning_direction + 90)
    CPWStraight(structure, igapw + boxgap, pinw=0, gapw=igapw + ipinw)

    structure.last = turning_position
    structure.last_direction = turning_direction

    # draw the rest part of the inductor
    CPWBendNew(structure, angle=180, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
    CPWStraight(structure, Inductl / 2. - rad, pinw=ipinw, gapw=igapw)
    CPWBendNew(structure, angle=-90, pinw=ipinw, gapw=igapw, radius=rad, polyarc=True, segments=4, square=square)
    # CPWStraight(structure,connecl,pinw=ipinw,gapw=igapw)
    CPWLinearTaper(structure, connecl, start_pinw=ipinw, stop_pinw=cpw_pinw, start_gapw=igapw, stop_gapw=igapw)

    end_point = structure.last
    end_direction = structure.last_direction

    # clear the rest metal
    structure.move(-(connecl + igapw) / 2.)
    structure.move(igapw + ipinw / 2., end_direction - 90)
    structure.last_direction -= 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap, pinw=0, gapw=(igapw + connecl) / 2.)

    structure.last = end_point
    structure.last_direction = end_direction
    structure.move(-(connecl + igapw + ipinw) / 2.)
    structure.move(cpw_pinw / 2., end_direction + 90)
    structure.last_direction = end_direction + 90
    CPWStraight(structure, Inductl / 2. + rad + boxgap + igapw, pinw=0, gapw=(connecl + igapw + ipinw) / 2.)

    structure.last = end_point
    structure.last_direction = end_direction
    structure.move(-(connecl + ipinw + 2 * igapw))
    structure.move(igapw + ipinw / 2., end_direction - 90)
    structure.last_direction = end_direction + 90
    CPWStraight(structure, Inductl / 2 + 3 * rad + boxgap, pinw=0, gapw=igapw)

    structure.last = end_point
    structure.last_direction = end_direction

    if couptype == 1:
        structure.move(boxl, end_direction + 180)
        structure.last_direction += 180

    # # Correcting this ffffffffffffffff bull-shit
    # aa1 = (armlt - Inductl) / 2 - 39
    # aa2 = 30 - aa1
    # aa3 = (433-388)/(280-250)*(Inductl - 280)+433
    # structure.last_direction = Initial_direction
    # structure.last = Initial_point
    # if Initial_direction != 180:
    #     structure.last_direction = 90
    #     structure.move(armlt / 2 - aa2 - aa1 / 2)
    #     structure.last_direction = Initial_direction
    #     CPWStraight(structure, aa3, pinw=0, gapw=aa1/2)
    #
    # if Initial_direction == 180:
    #     structure.last_direction = 90
    #     structure.move(410/2-14-16/2)
    #     structure.last_direction = Initial_direction
    #     CPWStraight(structure, 430, pinw=0, gapw=8)
    #
    #     structure.last_direction = Initial_direction
    #     structure.last = Initial_point
    #
    #     structure.last_direction = 90
    #     structure.move(410/2-14-51/2)
    #     structure.last_direction = 0
    #     structure.move(3)
    #     structure.last_direction = Initial_direction
    #     CPWStraight(structure, 16, pinw=0, gapw=51/2)
    #
    #     structure.last_direction = Initial_direction
    #     structure.last = Initial_point
    #
    #     structure.last_direction = 90
    #     structure.move(410/2 - 100/2 + 70)
    #     structure.last_direction = 180
    #     structure.move(380)
    #     CPWBendNew(structure, angle=180, pinw=0, gapw=0, radius=20, polyarc=True, segments=4, square=square)
    #
    #     structure.last_direction = Initial_direction
    #     structure.last = Initial_point
    #     structure.last_direction = 90
    #     structure.move(410 / 2 - 100 / 2 + 70 + 35)
    #     structure.last_direction = 180
    #     structure.move(400)
    #     structure.last_direction = 0
    #     structure.move(20)
    #     structure.last_direction = 180
    #     CPWBend(structure, 180, pinw=0, gapw=15, radius=35, polyarc=True, segments=4)
    #
    #     structure.last_direction = Initial_direction
    #     structure.last = Initial_point
    #     structure.last_direction = -90
    #     structure.move(410 / 2 - 14 - 16 / 2)
    #     structure.last_direction = Initial_direction
    #     CPWStraight(structure, 430, pinw=0, gapw=8)
    #
    #
    # structure.last_direction = Initial_direction
    # structure.last = Initial_point


def RoundZCorner(structure, square, cornerl=10.0, gapw=2.0, cornertype=0):
    # starting point is at the outer corner of a Z corner
    # direction is pointing from the out corner to the inner corner
    # cornerl is the distance between the two corners of the z corner
    # cornertype = 0 or 1 : z or mirrored z

    if cornertype == 0:
        angle = -90
    else:
        angle = 90
    structure.move(0.75 * cornerl)
    structure.last_direction += angle
    CPWBendNew(structure, angle=angle, pinw=0, gapw=0.25 * cornerl, radius=0.25 * cornerl, polyarc=1, segments=4,
               square=square)
    ref = structure.last
    CPWStraight(structure, 0.5 * cornerl, 0, 0.25 * cornerl)
    structure.last = ref
    structure.last_direction -= angle
    structure.move(0.25 * cornerl)
    structure.last_direction += angle
    structure.move(0.25 * cornerl)
    structure.last_direction -= angle
    CPWStraight(structure, 0.5 * cornerl, 0, 0.25 * cornerl)
    structure.move(-0.25 * cornerl, structure.last_direction)
    structure.last_direction += angle
    structure.move(-0.25 * cornerl)

    CPWBend(structure, -angle, pinw=0, gapw=0.25 * cornerl, radius=0.25 * cornerl, polyarc=1, segments=4)
    # CPWBendNew(structure, angle=-angle, pinw=0, gapw=gapw, radius=0.5 * cornerl + gapw, polyarc=1, segments=4,
    #            square=square)


def curve_corner(structure, xpos, ypos, radius, type):
    c2 = structure
    ref_pos = c2.last
    ref_direction = c2.last_direction
    square = 0
    ########################################
    # Corner type: 0:left top, 1:right top, 2:right bottom, 3:left bottom
    #
    #
    #  1#0
    #################
    #  2#3
    #
    #
    # starting position at corner
    c2.last = (xpos, ypos)
    if type == 0:
        c2.last_direction = 0
        c2.move(radius / 2)
        c2.last_direction = 90
        CPWStraight(c2, radius, pinw=0, gapw=radius / 2)
        c2.last = (xpos, ypos)
        c2.last_direction = 0
        c2.move(radius / 2)
        c2.last_direction = 90
        c2.move(radius)
        c2.last_direction = 270
        CPWBendNew(c2, angle=90, pinw=0, gapw=radius / 2, radius=radius / 2, polyarc=1, segments=4,
                   square=square)
    if type == 1:
        c2.last_direction = 180
        c2.move(radius / 2)
        c2.last_direction = 90
        CPWStraight(c2, radius, pinw=0, gapw=radius / 2)
        c2.last = (xpos, ypos)
        c2.last_direction = 180
        c2.move(radius / 2)
        c2.last_direction = 90
        c2.move(radius)
        c2.last_direction = 270
        CPWBendNew(c2, angle=-90, pinw=0, gapw=radius / 2, radius=radius / 2, polyarc=1, segments=4,
                   square=square)
    if type == 2:
        c2.last_direction = 180
        c2.move(radius / 2)
        c2.last_direction = 270
        CPWStraight(c2, radius, pinw=0, gapw=radius / 2)
        c2.last = (xpos, ypos)
        c2.last_direction = 180
        c2.move(radius / 2)
        c2.last_direction = 270
        c2.move(radius)
        c2.last_direction = 90
        CPWBendNew(c2, angle=90, pinw=0, gapw=radius / 2, radius=radius / 2, polyarc=1, segments=4,
                   square=square)
    if type == 3:
        c2.last_direction = 0
        c2.move(radius / 2)
        c2.last_direction = 270
        CPWStraight(c2, radius, pinw=0, gapw=radius / 2)
        c2.last = (xpos, ypos)
        c2.last_direction = 0
        c2.move(radius / 2)
        c2.last_direction = 270
        c2.move(radius)
        c2.last_direction = 90
        CPWBendNew(c2, angle=-90, pinw=0, gapw=radius / 2, radius=radius / 2, polyarc=1, segments=4,
                   square=square)
    ########################################
    c2.last_direction = ref_direction
    c2.last = ref_pos


def perforate(chip, grid_x, grid_y):
    nx, ny = map(int, [chip.size[0] / grid_x, chip.size[1] / grid_y])
    occupied = [[False] * ny for i in range(nx)]
    for i in range(nx):
        occupied[i][0] = True
        occupied[i][-1] = True
    for i in range(ny):
        occupied[0][i] = True
        occupied[-1][i] = True

    for e in chip.entities:
        o_x_list = []
        o_y_list = []
        for p in e.points:
            o_x, o_y = map(int, (p[0] / grid_x, p[1] / grid_y))
            if 0 <= o_x < nx and 0 <= o_y < ny:
                o_x_list.append(o_x)
                o_y_list.append(o_y)
        if o_x_list:
            for x in range(min(o_x_list), max(o_x_list) + 1):
                for y in range(min(o_y_list), max(o_y_list) + 1):
                    occupied[x][y] = True

    second_pass = deepcopy(occupied)
    for i in range(nx):
        for j in range(ny):
            if occupied[i][j]:
                for ip, jp in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    try:
                        second_pass[ip][jp] = True
                    except IndexError:
                        pass

    for i in range(nx):
        for j in range(ny):
            if not second_pass[i][j]:
                size = 2.5
                pos = i * grid_x + grid_x / 2., j * grid_y + grid_y / 2.
                p0 = vadd(pos, (-size, -size))
                p1 = vadd(pos, (size, size))
                abs_rect(chip, p0, p1)


def Xmon_pad(structure, xpos, ypos, shape):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    ref_pos = (xpos, ypos)
    # Default pad gap: 30um
    capgap = shape['capgap']
    capgap1 = shape['capgap1']
    capgap3 = shape['capgap3']
    square = 0
    ########################################
    #### parameter description:
    #### cross shape, labeling 0, 90, 180, 270 degree as 1,2,3,4
    #### widthx, widthy, length1, length2, length3, length4 is the cross length
    #### curve is the curve for all corners

    curve_rad = shape['curve']
    widthx = shape['widthx']
    widthy = shape['widthy']
    length1 = shape['length1']
    length2 = shape['length2']
    length3 = shape['length3']
    length4 = shape['length4']
    ext1 = shaep['end1_extend']
    ext3 = shaep['end3_extend']

    ## Draw right
    c2.s5.last = ref_pos
    c2.s5.last_direction = 0
    c2.s5.move(widthy / 2)
    CPWStraight(c2.s5, length1 - widthy / 2, pinw=widthx, gapw=capgap)
    CPWStraight(c2.s5, capgap1, pinw=0, gapw=widthx / 2 + capgap)
    ## Draw top
    c2.s5.last = ref_pos
    c2.s5.last_direction = 90
    c2.s5.move(widthx / 2 + capgap)
    CPWStraight(c2.s5, length2 - widthx / 2 - capgap, pinw=widthy, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=widthy / 2 + capgap)
    ## Draw left
    c2.s5.last = ref_pos
    c2.s5.last_direction = 180
    c2.s5.move(widthy / 2)
    CPWStraight(c2.s5, length3 - widthy / 2, pinw=widthx, gapw=capgap)
    CPWStraight(c2.s5, capgap3, pinw=0, gapw=widthx / 2 + capgap)
    ## Draw down
    c2.s5.last = ref_pos
    c2.s5.last_direction = 270
    c2.s5.move(widthx / 2 + capgap)
    CPWStraight(c2.s5, length4 - widthx / 2 - capgap, pinw=widthy, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=widthy / 2 + capgap)

    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Hmon(structure, xpos, ypos, shape):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    ref_pos = (xpos, ypos)

    length1 = shape['length1']
    length2 = shape['length2']
    length3 = shape['length3']
    length4 = shape['length4']
    length5 = shape['length5']
    capgap = shape['capgap']
    QQgap = shape['QQgap']
    width_l = shape['width_l']  # normal pad width
    width_QQ = shape['width_QQ']  # QQ coupling bar width
    curve = shape['curve']
    ref_pos1 = (xpos + length3 + length4 + QQgap + width_QQ, ypos)

    # Draw left H mon
    c2.s5.last = ref_pos
    c2.s5.last_direction = -180
    c2.s5.move(width_l / 2)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=width_l / 2)

    c2.s5.last = ref_pos
    c2.s5.last_direction = 90
    c2.s5.move(width_l / 2)
    CPWStraight(c2.s5, length1 - width_l / 2, pinw=width_l, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=capgap + width_l / 2)

    c2.s5.last = ref_pos
    c2.s5.last_direction = -90
    c2.s5.move(width_l / 2)
    CPWStraight(c2.s5, length1 - width_l / 2, pinw=width_l, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=capgap + width_l / 2)

    c2.s5.last = ref_pos
    c2.s5.last_direction = 0
    c2.s5.move(width_l / 2 + capgap)
    CPWStraight(c2.s5, length3 - capgap * 2 - width_l / 2 - width_QQ / 2, pinw=width_l, gapw=capgap)

    # Draw center part
    CPWStraight(c2.s5, capgap, pinw=width_l, gapw=(length5 - width_l) / 2 + capgap)
    CPWStraight(c2.s5, width_QQ, pinw=length5, gapw=capgap)
    CPWStraight(c2.s5, QQgap, pinw=0, gapw=length5 / 2 + capgap)
    CPWStraight(c2.s5, width_QQ, pinw=length5, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=width_l, gapw=(length5 - width_l) / 2 + capgap)

    # Draw Right H mon
    CPWStraight(c2.s5, length4 - capgap * 2 - width_l / 2 - width_QQ / 2, pinw=width_l, gapw=capgap)

    c2.s5.last = ref_pos1
    c2.s5.last_direction = 0
    c2.s5.move(width_l / 2)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=width_l / 2)

    c2.s5.last = ref_pos1
    c2.s5.last_direction = 90
    c2.s5.move(width_l / 2)
    CPWStraight(c2.s5, length2 - width_l / 2, pinw=width_l, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=capgap + width_l / 2)

    c2.s5.last = ref_pos1
    c2.s5.last_direction = -90
    c2.s5.move(width_l / 2)
    CPWStraight(c2.s5, length2 - width_l / 2, pinw=width_l, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=capgap + width_l / 2)

    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def junctionbox(structure, xpos, ypos, shape, fluxline=True):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    extension = shape['extension']
    x = shape['x']
    y1 = shape['y1']
    y2 = shape['y2']
    shiftx = shape['flux_shift']
    cpw_pinw = 10.0
    cpw_gapw1 = calculate_gap_width(eps_eff, 50, cpw_pinw)
    cpw_gapw = 20

    aa = 25 - 0.158

    # Draw junction box
    xpos1 = xpos - extension - x / 2 + shiftx
    ypos1 = ypos
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, extension, pinw=cpw_pinw, gapw=cpw_gapw)
    c2.s5.move(x)
    CPWStraight(c2.s5, extension, pinw=cpw_pinw, gapw=cpw_gapw)
    xpos1 = xpos - x / 2 + shiftx
    ypos1 = ypos + y1 / 2 - y2 / 2
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, x, pinw=0, gapw=(y1 + y2 + cpw_pinw + cpw_gapw1 * 2) / 2)

    c2.s5.last = (xpos1, ypos1 - 47.421)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, x, pinw=0, gapw=15.158 / 2)
    # Draw T shape
    xpos1 = xpos - x / 2 + shiftx
    ypos1 = ypos
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 180
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    xpos1 = xpos + x / 2 + shiftx
    ypos1 = ypos
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    # Curve junction box
    # # top right

    xpos1 = xpos + x / 2 + shiftx
    ypos1 = ypos + y1 + cpw_pinw / 2 + cpw_gapw1
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 2)
    curve_corner(c2.s5, xpos1, ypos1 - aa, aa / 2, 0)
    # top left
    xpos1 = xpos - x / 2 + shiftx
    ypos1 = ypos + y1 + cpw_pinw / 2 + cpw_gapw1
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 3)
    curve_corner(c2.s5, xpos1, ypos1 - aa, aa / 2, 1)
    # bottom left
    xpos1 = xpos - x / 2 + shiftx
    ypos1 = ypos - y2 - cpw_pinw / 2 - cpw_gapw
    curve_corner(c2.s5, xpos1, ypos1, y2 / 2, 0)
    curve_corner(c2.s5, xpos1, ypos1 + y2, y2 / 2, 2)
    # bottom right
    xpos1 = xpos + x / 2 + shiftx
    ypos1 = ypos - y2 - cpw_pinw / 2 - cpw_gapw
    curve_corner(c2.s5, xpos1, ypos1, y2 / 2, 1)
    curve_corner(c2.s5, xpos1, ypos1 + y2, y2 / 2, 3)

    ####################################
    if fluxline:
        cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)
        # Flux line coming from the top
        linear = 50
        fluxpin = 3
        fluxgap = 11 - 3
        fluxw1 = 3.0
        fluxtapergap = 16.0
        ext = 4.5
        flux_rad = 5
        shifty = shape['flux_dis'] - 15.158
        xtarget = c2.s3.last[0]
        ytarget = c2.s3.last[1]

        xpos1 = xpos - 9
        ypos1 = ypos + y1 + cpw_pinw / 2 + 20 + fluxgap + fluxpin + linear + shifty
        c2.s5.last = (xtarget, ytarget)
        c2.s5.last_direction = 270
        CPWStraight(c2.s5, ytarget - ypos1, pinw=cpw_pinw, gapw=cpw_gapw)

        c2.s5.last = (xpos1, ypos1)
        c2.s5.last_direction = 270
        CPWLinearTaper(c2.s5, linear, start_pinw=cpw_pinw, stop_pinw=fluxw1, start_gapw=cpw_gapw,
                       stop_gapw=fluxtapergap)

        c2.s5.last = (xpos1 - cpw_pinw / 2 - ext, ypos1 - linear)
        c2.s5.last_direction = 270
        CPWStraight(c2.s5, fluxw1, pinw=0, gapw=fluxtapergap / 2)

        c2.s5.last = (xpos1, ypos1 - linear - fluxw1)
        c2.s5.last_direction = 270
        CPWStraight(c2.s5, fluxw1, pinw=0, gapw=(fluxtapergap * 2 + ext * 2 + fluxw1) / 2)

        # curve flux line
        xx = xpos1 - (fluxtapergap * 2 + ext * 2 + fluxw1) / 2 + ext
        yy = ypos1 - linear - fluxw1
        curve_corner(c2.s5, xx, yy, fluxw1, 1)

        xx = xx + fluxtapergap
        yy = ypos1 - linear - fluxw1
        curve_corner(c2.s5, xx, yy, fluxw1, 0)

        xx = xpos1 - (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
        yy = ypos1 - linear - fluxw1
        curve_corner(c2.s5, xx, yy, fluxw1 / 2, 3)

        xx = xpos1 + (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
        yy = ypos1 - linear - fluxw1
        curve_corner(c2.s5, xx, yy, fluxw1 / 2, 2)

        xx = xpos1 - (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
        yy = ypos1 - linear - fluxw1 * 2
        curve_corner(c2.s5, xx, yy, fluxw1 / 2, 0)

        xx = xpos1 + (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
        yy = ypos1 - linear - fluxw1 * 2
        curve_corner(c2.s5, xx, yy, fluxw1 / 2, 1)

    ########################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def junctionbox_test(structure, xpos, ypos, shape):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    extension = shape['extension']
    x = shape['x']
    y1 = shape['y1']
    y2 = shape['y2']
    shiftx = shape['flux_shift']
    cpw_pinw = 10.0
    cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)

    aa = 25 - 0.158

    # Draw junction box
    xpos1 = xpos
    ypos1 = ypos + extension + x / 2
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 270
    CPWStraight(c2.s5, extension, pinw=cpw_pinw, gapw=cpw_gapw)
    c2.s5.move(x)
    CPWStraight(c2.s5, extension, pinw=cpw_pinw, gapw=cpw_gapw)
    xpos1 = xpos - y1 / 2 + y2 / 2
    ypos1 = ypos + x / 2
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 270
    CPWStraight(c2.s5, x, pinw=0, gapw=(y1 + y2) / 2)
    # Draw T shape
    xpos1 = xpos
    ypos1 = ypos + x / 2
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    xpos1 = xpos
    ypos1 = ypos - x / 2
    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 270
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    ## curve corners
    aa = 20.158
    xpos1 = xpos - 9.842
    ypos1 = ypos + x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 1)

    xpos1 = xpos + 9.842
    ypos1 = ypos + x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 0)

    xpos1 = xpos - 30
    ypos1 = ypos + x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 3)

    xpos1 = xpos + 30
    ypos1 = ypos + x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 2)

    xpos1 = xpos - 9.842
    ypos1 = ypos - x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 2)

    xpos1 = xpos + 9.842
    ypos1 = ypos - x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 3)

    xpos1 = xpos - 30
    ypos1 = ypos - x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 0)

    xpos1 = xpos + 30
    ypos1 = ypos - x / 2
    curve_corner(c2.s5, xpos1, ypos1, aa / 2, 1)

    ########################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Draw_junc_optical(structure, xpos, ypos, shape):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    ref_pos = (xpos, ypos)

    length = shape['length']
    top = shape['top']
    width = shape['width']
    bottom = shape['bottom']
    c2.s5.last = (xpos, ypos+length/2)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, top, pinw=0, gapw=width / 2)
    # cut T shape
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    c2.s5.last = (xpos, ypos - length / 2)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, bottom, pinw=0, gapw=width / 2)
    # cut T shape
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    ###############################################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Zmon(structure, xpos, ypos, shape):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    ref_pos = (xpos, ypos)

    length1 = shape['length1']
    length2 = shape['length2']
    length3 = shape['length3']
    length4 = shape['length4']

    capgap = shape['capgap']
    gap1 = shape['gap1']
    width_QQ = shape['width_QQ']
    width = shape['width']
    gap_QQ = shape['QQgap']
    curve = shape['curve']
    ref_pos2 = (xpos + width_QQ + gap1 * 2 + gap_QQ, ypos)

    # draw the first Zmon
    # draw left part
    c2.s5.last = ref_pos
    c2.s5.last_direction = 180
    c2.s5.move(width_QQ / 2)
    CPWStraight(c2.s5, length1 - width_QQ / 2, pinw=width, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=capgap + width / 2)

    # draw right part
    c2.s5.last = ref_pos
    c2.s5.last_direction = 0
    c2.s5.move(width_QQ / 2)
    CPWStraight(c2.s5, gap1, pinw=0, gapw=capgap + width / 2)

    c2.s5.last_direction = 270
    c2.s5.last = (xpos, ypos - width / 2)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=width_QQ / 2)

    c2.s5.last_direction = 0
    c2.s5.last = (xpos - width_QQ / 2 - capgap, ypos + length2 / 2 + width / 4 + capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=length2 / 2 - width / 4)
    c2.s5.last = (xpos - width_QQ / 2, ypos + length2 + capgap / 2)
    CPWStraight(c2.s5, width_QQ, pinw=0, gapw=capgap / 2)
    c2.s5.last = (xpos + width_QQ / 2, ypos + length2 / 2 + width / 4 + capgap)
    CPWStraight(c2.s5, gap1, pinw=0, gapw=length2 / 2 - width / 4)

    # draw the second Zmon
    # draw right part
    c2.s5.last = ref_pos2
    c2.s5.last_direction = 0
    c2.s5.move(width_QQ / 2)
    CPWStraight(c2.s5, length3 - width_QQ / 2, pinw=width, gapw=capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=capgap + width / 2)

    c2.s5.last = ref_pos2
    c2.s5.last_direction = 180
    c2.s5.move(width_QQ / 2)
    CPWStraight(c2.s5, gap1, pinw=0, gapw=capgap + width / 2)

    # draw left part
    c2.s5.last_direction = 270
    c2.s5.last = (ref_pos2[0], ref_pos2[1] - width / 2)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=width_QQ / 2)

    c2.s5.last_direction = 180
    c2.s5.last = (ref_pos2[0] + width_QQ / 2 + capgap, ref_pos2[1] + length4 / 2 + width / 4 + capgap)
    CPWStraight(c2.s5, capgap, pinw=0, gapw=length4 / 2 - width / 4)
    c2.s5.last = (ref_pos2[0] + width_QQ / 2, ref_pos2[1] + length4 + capgap / 2)
    CPWStraight(c2.s5, width_QQ, pinw=0, gapw=capgap / 2)
    c2.s5.last = (ref_pos2[0] - width_QQ / 2, ref_pos2[1] + length4 / 2 + width / 4 + capgap)
    CPWStraight(c2.s5, gap1, pinw=0, gapw=length4 / 2 - width / 4)

    # curve corners
    # left Zmon
    curve_l = 25
    x = ref_pos[0] + width_QQ / 2
    y = ref_pos[1] + length2
    curve_corner(c2.s5, x, y, curve, 2)
    curve_corner(c2.s5, x + gap1, y + capgap, curve, 2)

    x = ref_pos[0] - width_QQ / 2
    y = ref_pos[1] + length2
    curve_corner(c2.s5, x, y, curve, 3)
    curve_corner(c2.s5, x - capgap, y + capgap, curve, 3)

    x = ref_pos[0] - width_QQ / 2
    y = ref_pos[1] + width / 2
    curve_corner(c2.s5, x, y, curve_l, 1)
    curve_corner(c2.s5, x - capgap, y + capgap, curve_l, 1)

    x = ref_pos[0] - length1
    y = ref_pos[1] + width / 2
    curve_corner(c2.s5, x, y, curve_l, 3)
    curve_corner(c2.s5, x - capgap, y + capgap, curve_l, 3)

    x = ref_pos[0] - length1
    y = ref_pos[1] - width / 2
    curve_corner(c2.s5, x, y, curve_l, 0)
    curve_corner(c2.s5, x - capgap, y - capgap, curve_l, 0)

    x = ref_pos[0] + width_QQ / 2
    y = ref_pos[1] - width / 2
    curve_corner(c2.s5, x, y, curve_l, 1)
    curve_corner(c2.s5, x + gap1, y - capgap, curve_l, 1)

    # right Zmon
    x = ref_pos2[0] - width_QQ / 2
    y = ref_pos2[1] + length4
    curve_corner(c2.s5, x, y, curve, 3)
    curve_corner(c2.s5, x - gap1, y + capgap, curve, 3)

    x = ref_pos2[0] + width_QQ / 2
    y = ref_pos2[1] + length4
    curve_corner(c2.s5, x, y, curve, 2)
    curve_corner(c2.s5, x + capgap, y + capgap, curve, 2)

    x = ref_pos2[0] + width_QQ / 2
    y = ref_pos2[1] + width / 2
    curve_corner(c2.s5, x, y, curve_l, 0)
    curve_corner(c2.s5, x + capgap, y + capgap, curve_l, 0)

    x = ref_pos2[0] + length3
    y = ref_pos2[1] + width / 2
    curve_corner(c2.s5, x, y, curve_l, 2)
    curve_corner(c2.s5, x + capgap, y + capgap, curve_l, 2)

    x = ref_pos2[0] + length3
    y = ref_pos2[1] - width / 2
    curve_corner(c2.s5, x, y, curve_l, 1)
    curve_corner(c2.s5, x + capgap, y - capgap, curve_l, 1)

    x = ref_pos2[0] - width_QQ / 2
    y = ref_pos2[1] - width / 2
    curve_corner(c2.s5, x, y, curve_l, 0)
    curve_corner(c2.s5, x - gap1, y - capgap, curve_l, 0)

    ###############################################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Lumped_LC_modified(structure, xpos, ypos, shape, type):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction

    if type==1:
        phase_correction = 0
    else:
        phase_correction = 180
    C_x = shape['C_x']
    C_y = shape['C_y']
    C_width = shape['C_width']
    C_round = shape['C_round']
    finger_number = shape['finger_number']
    finger_width = shape['finger_width']
    finger_length = shape['finger_length']
    finger_gap = shape['finger_gap']
    C_gap = 30

    ## Cleanup the metal
    LC_x = C_x+C_width+C_gap*2
    LC_y = C_y+C_gap*2+C_width
    c2.s5.last = (xpos, ypos)
    c2.s5.last_direction = phase_correction
    CPWStraight(c2.s5, LC_x, pinw=0, gapw=LC_y/2)
    ref1 = c2.s5.last

    ## Draw the Capacitive part
    c2.s5.last = (xpos, ypos)
    c2.s5.last_direction = phase_correction
    c2.s5.move(C_gap)
    CPWStraight(c2.s5, C_width, pinw=0, gapw=C_y / 2+C_width/2)
    CPWStraight(c2.s5, C_x, pinw=C_y-C_width, gapw=C_width)

    ## Curve corners
    if type==1:

        curve_Z = [C_width/2, C_width/2, C_width/2,
                   C_round-C_width/2, C_round, C_round+C_width/2,
                   C_round-C_width/2, C_round, C_round+C_width/2,
                   C_width/2, C_width/2, C_width/2]

        xlistQ1 = [ref1[0]-C_gap, ref1[0]-C_gap, ref1[0],
                   xpos+C_gap+C_width, xpos+C_gap, xpos,
                   xpos+C_gap+C_width, xpos+C_gap, xpos,
                   ref1[0]-C_gap, ref1[0]-C_gap, ref1[0]]
        ylistQ1 = [ref1[1]+LC_y/2-C_gap-C_width, ref1[1]+LC_y/2-C_gap, ref1[1]+LC_y/2,
                   ref1[1]+LC_y/2-C_gap-C_width, ref1[1]+LC_y/2-C_gap, ref1[1]+LC_y/2,
                   ref1[1]-LC_y/2+C_gap+C_width, ref1[1]-LC_y/2+C_gap, ref1[1]-LC_y/2,
                   ref1[1]-LC_y/2+C_gap+C_width, ref1[1]-LC_y/2+C_gap, ref1[1]-LC_y/2]
        cornerQ1 = [1,2,2,3,3,3,0,0,0,2,1,1]
        for ii in range(len(cornerQ1)):
            curve_corner(c2.s5, xlistQ1[ii], ylistQ1[ii], curve_Z[ii], cornerQ1[ii])
    else:

        curve_Z = [C_width / 2, C_width / 2, C_width / 2,
                   C_round-C_width/2, C_round, C_round+C_width/2,
                   C_round-C_width/2, C_round, C_round+C_width/2,
                   C_width / 2, C_width / 2, C_width / 2]

        xlistQ1 = [ref1[0] + C_gap, ref1[0] + C_gap, ref1[0],
                   xpos - C_gap - C_width, xpos - C_gap, xpos,
                   xpos - C_gap - C_width, xpos - C_gap, xpos,
                   ref1[0] + C_gap, ref1[0] + C_gap, ref1[0]]
        ylistQ1 = [ref1[1] + LC_y / 2 - C_gap - C_width, ref1[1] + LC_y / 2 - C_gap, ref1[1] + LC_y / 2,
                   ref1[1] + LC_y / 2 - C_gap - C_width, ref1[1] + LC_y / 2 - C_gap, ref1[1] + LC_y / 2,
                   ref1[1] - LC_y / 2 + C_gap + C_width, ref1[1] - LC_y / 2 + C_gap, ref1[1] - LC_y / 2,
                   ref1[1] - LC_y / 2 + C_gap + C_width, ref1[1] - LC_y / 2 + C_gap, ref1[1] - LC_y / 2]
        cornerQ1 = [0,3,3,2,2,2,1,1,1,3,0,0]
        for ii in range(len(cornerQ1)):
            curve_corner(c2.s5, xlistQ1[ii], ylistQ1[ii], curve_Z[ii], cornerQ1[ii])

    ## Draw inductive fingers
    if type==1:
        c2.s5.last = (xpos+C_gap+C_width, ypos)
        c2.s5.last_direction = phase_correction
        CPWStraight(c2.s5, 35, pinw=0, gapw=(finger_width)/2)
        CPWBendNew(c2.s5, angle=-90, pinw=0, gapw=finger_width/2, radius=(finger_gap+finger_width/2), polyarc=1, segments=4,
                   square=square)
        CPWStraight(c2.s5, finger_length-(finger_gap+finger_width/2), pinw=0, gapw=(finger_width) / 2)
        CPWBendNew(c2.s5, angle=180, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2), polyarc=1,
                   segments=4, square=square)
        CPWStraight(c2.s5, finger_length, pinw=0, gapw=(finger_width) / 2)
        for i in range(finger_number):
            CPWStraight(c2.s5, finger_length, pinw=0, gapw=(finger_width) / 2)
            CPWBendNew(c2.s5, angle=-180, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2),
                       polyarc=1,
                       segments=4, square=square)
            CPWStraight(c2.s5, finger_length*2, pinw=0, gapw=(finger_width) / 2)
            CPWBendNew(c2.s5, angle=180, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2),
                       polyarc=1,
                       segments=4, square=square)
            CPWStraight(c2.s5, finger_length, pinw=0, gapw=(finger_width) / 2)
        # Connect to the edge
        CPWBendNew(c2.s5, angle=-90, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2),
                   polyarc=1,
                   segments=4, square=square)
        CPWStraight(c2.s5, ref1[0]-c2.s5.last[0]-5, pinw=0, gapw=(finger_width) / 2)
        CPWLinearTaper(c2.s5, 5, start_pinw=0, stop_pinw=0, start_gapw=(finger_width) / 2,
                       stop_gapw=5)

        # Curve boundary
        curve_Z = [30,30]

        xlistQ1 = [xpos+C_gap+C_width, xpos+C_gap+C_width]
        ylistQ1 = [ypos+finger_width/2, ypos-finger_width/2]
        cornerQ1 = [0,3]
        for ii in range(len(cornerQ1)):
            curve_corner(c2.s5, xlistQ1[ii], ylistQ1[ii], curve_Z[ii], cornerQ1[ii])
    else:
        c2.s5.last = (xpos - C_gap - C_width, ypos)
        c2.s5.last_direction = phase_correction
        CPWStraight(c2.s5, 35, pinw=0, gapw=(finger_width) / 2)
        CPWBendNew(c2.s5, angle=90, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2), polyarc=1,
                   segments=4,
                   square=square)
        CPWStraight(c2.s5, finger_length - (finger_gap + finger_width / 2), pinw=0, gapw=(finger_width) / 2)
        CPWBendNew(c2.s5, angle=-180, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2), polyarc=1,
                   segments=4, square=square)
        CPWStraight(c2.s5, finger_length, pinw=0, gapw=(finger_width) / 2)
        for i in range(finger_number):
            CPWStraight(c2.s5, finger_length, pinw=0, gapw=(finger_width) / 2)
            CPWBendNew(c2.s5, angle=180, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2),
                       polyarc=1,
                       segments=4, square=square)
            CPWStraight(c2.s5, finger_length * 2, pinw=0, gapw=(finger_width) / 2)
            CPWBendNew(c2.s5, angle=-180, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2),
                       polyarc=1,
                       segments=4, square=square)
            CPWStraight(c2.s5, finger_length, pinw=0, gapw=(finger_width) / 2)
        # Connect to the edge
        CPWBendNew(c2.s5, angle=90, pinw=0, gapw=finger_width / 2, radius=(finger_gap + finger_width / 2),
                   polyarc=1,
                   segments=4, square=square)
        CPWStraight(c2.s5, -ref1[0] + c2.s5.last[0] - 5, pinw=0, gapw=(finger_width) / 2)
        CPWLinearTaper(c2.s5, 5, start_pinw=0, stop_pinw=0, start_gapw=(finger_width) / 2,
                       stop_gapw=5)

        # Curve boundary
        curve_Z = [30, 30]

        xlistQ1 = [xpos - C_gap - C_width, xpos - C_gap - C_width]
        ylistQ1 = [ypos + finger_width / 2, ypos - finger_width / 2]
        cornerQ1 = [1, 2]
        for ii in range(len(cornerQ1)):
            curve_corner(c2.s5, xlistQ1[ii], ylistQ1[ii], curve_Z[ii], cornerQ1[ii])


    ############################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1

def Lumped_LC(structure, xpos, ypos, position):
    c2 = structure
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    # The left resonator
    c2.s5.last = (xpos + position['leftx'], ypos + position['lefty'])
    Left_cap = position['Left_cap']
    Right_cap = position['Right_cap']
    shiftR1 = 80
    finlt = 420.0 + Left_cap + 80*0
    armlt = 410.0 + shiftR1*0
    finwt = 40.0
    gapwt = 30.0

    Inductlb = 280.0 + 150*0
    ipinwb = 5.0
    igapwb = 8.0+4*0
    induct_num_b = 9
    connecl_b = 5.0
    boxgap_b = 30.0
    ### My correction by ZiqianLi
    C1Q1 = -40
    C2Q2 = -55
    C_Q_Leftdistance = 155.0 - 2 * 30 + C1Q1
    C_Q_Rightdistance = 130.0 - 2 * 30 + C2Q2
    C_Position = 0
    rad = 50

    ### End of My correction
    c2.s5.last_direction = 0

    c2.s5.move(C_Q_Leftdistance)
    c2.s5.move(C_Position, c2.s5.last_direction + 90)
    fin1, fin1_dir, fin2, fin2_dir, induct, induct_dir = CapNew(c2.s5, finw=finwt, finl=finlt + 10.0,
                                                                arml=armlt,
                                                                connecw=5.0, connecl=30.0, cgapw=gapwt,
                                                                couptype=2, fin1connecl=0, fin2connecl=0,
                                                                finconnecw=0, finconnecgapw=0, square=square)
    c2.s5.last = induct
    c2.s5.last_direction = induct_dir
    InductorBox(c2.s5, Inductl=Inductlb, ipinw=ipinwb, igapw=igapwb, induct_num=induct_num_b, connecl=connecl_b,
                boxgap=boxgap_b, couptype=0, square=square, armlt=armlt)

    # Left input charge1
    padlb = 25.0 * 0.75
    padwb = 10.0
    pgapwb = 20.0
    stubwb = 2.0

    c2.s5.last = fin1
    c2.s5.last_direction = fin1_dir

    c2.s5.move(10)
    c2.s5.move(340 + 2, direction=180)
    c2.s5.move(310, direction=90)
    c2.s5.last_direction = 180

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    CPWStraight(c2.s5, 400, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s0.last[1] - c2.s5.last[1] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = -c2.s0.last[0] + c2.s5.last[0]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    # Left output
    padlb = 180.0 * 0.7
    padwb = 20.0
    pgapwb = 20.0
    stubwb = 5.0

    c2.s5.last = fin2
    c2.s5.last_direction = fin2_dir

    c2.s5.move(10)
    c2.s5.move(570, direction=270)
    c2.s5.last_direction = 270

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    CPWStraight(c2.s5, 50, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s5.last[0] - c2.s9.last[0] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = -c2.s9.last[1] + c2.s5.last[1]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    ################################ Perfect Left Resonator  ####################

    (x_a, y_a) = (xpos + position['leftx'], ypos + position['lefty'])
    x_a = x_a + 585
    y_a = y_a - 987
    direction_a = c2.s5.last_direction

    x_cur = x_a + 80
    y_cur = y_a + 1262
    refer_left = c2.s5.last

    curve_corner(c2.s5, x_cur, y_cur, 20, 2)
    curve_corner(c2.s5, x_cur, y_cur - 100, 20, 1)
    curve_corner(c2.s5, x_cur - 80, y_cur - 100, 30, 3)

    curve_corner(c2.s5, x_cur, y_cur - 450, 20, 2)
    curve_corner(c2.s5, x_cur - 80, y_cur - 450, 20, 0)
    curve_corner(c2.s5, x_cur, y_cur - 550, 30, 1)

    ### Left up corner and down corner
    x0 = x_a - 10 + Left_cap / 2
    y0 = y_a + 1237
    xx = x0
    yy = y0
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWBendNew(c2.s5, angle=-180, pinw=0, gapw=25, radius=25, polyarc=1, segments=4,
               square=square)

    y0 = y0 - 25
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, 20, 0, 20)

    x0 = x_a - 10 + Left_cap / 2
    y0 = y_a + 1237 - 450
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWBendNew(c2.s5, angle=-180, pinw=0, gapw=25, radius=25, polyarc=1, segments=4,
               square=square)

    y0 = y0 - 25
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, 20, 0, 20)

    ## Draw upper and lower bar
    x0 = xx + 50 - Left_cap
    y0 = yy - 67
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 180
    CPWStraight(c2.s5, 430, 0, 8)

    (x0, y0) = c2.s5.last
    x0 = x0 - 34 + 430
    y0 = y0 - 34 + 16.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, 16, 0, 25.5)

    c2.s5.last = (c2.s5.last[0] + 9, c2.s5.last[1] + 28)
    c2.s5.last_direction = 270
    CPWStraight(c2.s5, 2.5, 0, 9)

    (x0, y0) = c2.s5.last
    c2.s5.last_direction = 180
    x0 = x0 - 16 + 25
    y0 = y0 + 1.25 - 375.25
    c2.s5.last = (x0, y0)
    CPWStraight(c2.s5, 396 + 34, 0, 8)

    c2.s5.last_direction = 90
    c2.s5.last = (x0 + 8 - 396 - 37, y0 - 8)
    CPWStraight(c2.s5, 35 + 16, 0, 8)

    # Draw input and output
    x0 = xx - 9.5 + 50.5 - Left_cap
    y0 = yy - 137 + 27 - 151 + 0.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 129.5, 0, 4)

    x0 = x0 + 9
    y0 = y0 + 10.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 180
    CPWLinearTaper(c2.s5, 5, 21, 21, 2.5, 0)

    (x0, y0) = c2.s5.last
    x0 = x0 + 5
    y0 = y0 + 7.75
    c2.s5.last = (x0, y0)
    CPWStraight(c2.s5, 5, 0, 5.5 / 2)
    (x0, y0) = c2.s5.last
    x0 = x0
    y0 = y0 - 7.75
    c2.s5.last = (x0, y0)
    CPWBendNew(c2.s5, angle=90, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
               square=square)

    (x0, y0) = c2.s5.last
    x0 = x0 - 10.5 + 8
    y0 = y0 - 7.75 + 15.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, 13, 0, 15.5 / 2)

    c2.s5.last_direction = 90
    (x0, y0) = c2.s5.last
    x0 = x0 - 25
    y0 = y0 - 7.75
    c2.s5.last = (x0, y0)
    CPWStraight(c2.s5, 150.5, 0, 4)

    ## inductor finger perfect
    (x0, y0) = c2.s5.last
    x0 = x0 - 405 + 41.5
    y0 = y0
    c2.s5.last = (x0, y0)
    i_up = 9
    i_down = 10
    for ii in range(i_up):
        c2.s5.last_direction = 90
        CPWBendNew(c2.s5, angle=-180, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
                   square=square)
        (x0, y0) = c2.s5.last
        x1 = x0 - 23.5
        y1 = y0 + 6.5
        c2.s5.last = (x1, y1)
        c2.s5.last_direction = 0
        CPWStraight(c2.s5, 26, 0, 6.5)
        c2.s5.last = (x0 + 21, y0)

    x0 = x0 - 378
    y0 = y0 - 280
    c2.s5.last = (x0, y0)
    for ii in range(i_down):
        c2.s5.last_direction = -90
        CPWBendNew(c2.s5, angle=180, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
                   square=square)
        (x0, y0) = c2.s5.last
        x1 = x0 - 23.5
        y1 = y0 - 6.5
        c2.s5.last = (x1, y1)
        c2.s5.last_direction = 0
        CPWStraight(c2.s5, 26, 0, 6.5)
        c2.s5.last = (x0 + 21, y0)

    c2.s5.last_direction = -90
    x0 = xx - 422 + 51 - Left_cap
    y0 = yy - 390 + 129.5
    c2.s5.last = (x0, y0)
    CPWStraight(c2.s5, 129.5, 0, 4)

    c2.s5.last_direction = 90
    (x0, y0) = c2.s5.last
    x0 = x0 + 6.5
    y0 = y0 + 129.5
    c2.s5.last = (x0, y0)
    CPWBendNew(c2.s5, angle=90, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
               square=square)

    c2.s5.last_direction = 0
    (x0, y0) = c2.s5.last
    x0 = x0
    y0 = y0 - 4
    c2.s5.last = (x0, y0)
    CPWStraight(c2.s5, 13, 0, 6.5)

    c2.s5.last_direction = -90
    (x0, y0) = c2.s5.last
    x0 = x0 + 2.5 - 18
    y0 = y0 - 6.5 + 21
    c2.s5.last = (x0, y0)
    CPWStraight(c2.s5, 8, 0, 2.5)

    c2.s5.last_direction = -90
    (x0, y0) = c2.s5.last
    x0 = x0 + 2.5 - 30 + 55
    y0 = y0 - 6 + 27 + 115 + 1.5
    c2.s5.last = (x0, y0)
    CPWStraight(c2.s5, 150.5, 0, 4)

    c2.s5.last = (x_a, y_a - 50)
    c2.s5.last_direction = direction_a

    ########################################
    # The right resonator
    c2.s5.last_direction = 180
    c2.s5.last = (xpos + position['rightx'], ypos + position['righty'] + 10)
    finlt = 378.0 + Right_cap
    armlt = 370.0
    finwt = 40.0
    gapwt = 30.0

    Inductlb = 250.0
    ipinwb = 5.0
    igapwb = 8.0
    induct_num_b = 8
    connecl_b = 5.0
    boxgap_b = 30.0

    c2.s5.move(C_Q_Rightdistance)
    c2.s5.move(C_Position, c2.s5.last_direction - 90)
    fin1, fin1_dir, fin2, fin2_dir, induct, induct_dir = CapNew(c2.s5, finw=finwt, finl=finlt + 10.0,
                                                                arml=armlt,
                                                                connecw=5.0, connecl=30.0, cgapw=gapwt,
                                                                couptype=2, fin1connecl=0, fin2connecl=0,
                                                                finconnecw=0, finconnecgapw=0, square=square)
    c2.s5.last = induct
    c2.s5.last_direction = induct_dir
    InductorBox(c2.s5, Inductl=Inductlb, ipinw=ipinwb, igapw=igapwb, induct_num=induct_num_b, connecl=connecl_b,
                boxgap=boxgap_b, couptype=0, square=square, armlt=armlt)

    # Right input charge2
    padlb = 25.0 * 0.75
    padwb = 10.0
    pgapwb = 20.0
    stubwb = 2.0

    c2.s5.last = fin2
    c2.s5.last_direction = fin2_dir

    c2.s5.move(10)
    c2.s5.move(309 + 2, direction=0)
    c2.s5.move(280, direction=90)
    c2.s5.last_direction = 0

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    remaining = -c2.s5.last[0] + c2.s7.last[0] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = -c2.s7.last[1] + c2.s5.last[1]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    # Right output
    padlb = 180.0 * 0.7
    padwb = 20.0
    pgapwb = 20.0
    stubwb = 5.0

    c2.s5.last = fin1
    c2.s5.last_direction = fin1_dir

    c2.s5.move(10)
    c2.s5.move(530, direction=270)
    c2.s5.last_direction = 270

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    CPWStraight(c2.s5, 100, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s5.last[0] - c2.s8.last[0] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s5.last[1] - c2.s8.last[1]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    ####################### Perfect Right resonator  #############################

    (x_a, y_a) = refer_left
    y_a = y_a +2000+46.5
    x_a = x_a -500+1.8+6.7*2-331.7
    sss = c2.s5.last_direction

    x_cur = x_a + 3120 - 50 + 0.5
    y_cur = y_a - 960 + 2

    curve_corner(c2.s5, x_cur, y_cur, 20, 3)
    curve_corner(c2.s5, x_cur, y_cur - 100, 20, 0)
    curve_corner(c2.s5, x_cur + 60, y_cur - 100, 30, 2)

    curve_corner(c2.s5, x_cur, y_cur - 410, 20, 3)
    curve_corner(c2.s5, x_cur + 60, y_cur - 410, 20, 1)
    curve_corner(c2.s5, x_cur, y_cur - 510, 30, 0)

    # Top right and bottom right
    x0 = x_a + 3000 + 17.5 + 25 + Right_cap + 18
    y0 = y_a - 960 - 23
    xx = x0
    yy = y0
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 180
    CPWBendNew(c2.s5, angle=180, pinw=0, gapw=25, radius=25, polyarc=1, segments=4,
               square=square)

    (x0, y0) = c2.s5.last
    x0 = x0 - 10
    y0 = y0 + 45
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 40, 0, 10)

    (x0, y0) = c2.s5.last
    x0 = x0 + 10
    y0 = y0 - 365
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 180
    CPWBendNew(c2.s5, angle=180, pinw=0, gapw=25, radius=25, polyarc=1, segments=4,
               square=square)

    (x0, y0) = c2.s5.last
    x0 = x0 - 10
    y0 = y0 + 45
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 40, 0, 10)

    # # Upper and bottom bar
    (x0, y0) = c2.s5.last
    x0 = x0 - 6 + Right_cap - 34
    y0 = y0 + 390.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWStraight(c2.s5, 354 + 34, 0, 10.5)

    (x0, y0) = c2.s5.last
    x0 = x0 - 5
    y0 = y0 + 10.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 51, 0, 8)

    (x0, y0) = c2.s5.last
    x0 = x0 + 5
    y0 = y0 - 355 + 34.5 + 30
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 180
    CPWStraight(c2.s5, 388, 0, 10.5)

    c2.s5.last = (c2.s5.last[0] + 9, c2.s5.last[1] - 13)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 2.5, 0, 9)

    # Draw input and output
    (x0, y0) = c2.s5.last
    x0 = x0 + 17
    y0 = y0
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 51, 0, 8)

    (x0, y0) = c2.s5.last
    x0 = x0 - 50 + 17 + 7
    y0 = y0 + 123 + 2
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWLinearTaper(c2.s5, 5, 21, 21, 2.5, 0)

    (x0, y0) = c2.s5.last
    x0 = x0
    y0 = y0
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 0
    CPWBendNew(c2.s5, angle=90, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
               square=square)

    (x0, y0) = c2.s5.last
    x0 = x0 - 4
    y0 = y0
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 15.5, 0, 6.5)

    (x0, y0) = c2.s5.last
    x0 = x0 - 9
    y0 = y0
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 5.5, 0, 2.5)

    (x0, y0) = c2.s5.last
    x0 = x0 + 6.5
    y0 = y0 + 21
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 114.5, 0, 4)

    (x0, y0) = c2.s5.last
    x0 = x0 - 27.5 + 51.5 - 3
    y0 = y0 - 2.5 - 13 - 120 + 21
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, 135.5, 0, 4)

    ## inductor finger perfect
    (x0, y0) = c2.s5.last
    i_up = 9
    i_down = 8
    x0 = x0 + 11 + 1.5 + 330 + 0 * Right_cap - 357
    y0 = y0 + 280 - 28 - 2
    c2.s5.last = (x0, y0)
    for ii in range(i_up):
        c2.s5.last_direction = 90
        CPWBendNew(c2.s5, angle=-180, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
                   square=square)
        (x0, y0) = c2.s5.last
        x1 = x0 - 23.5
        y1 = y0 + 6.5
        c2.s5.last = (x1, y1)
        c2.s5.last_direction = 0
        CPWStraight(c2.s5, 26, 0, 6.5)
        c2.s5.last = (x0 + 21, y0)

    x0 = x0 - 336
    y0 = y0 + 280 - 1 - 571 + 13 - 1 + 30
    c2.s5.last = (x0, y0)
    for ii in range(i_down):
        c2.s5.last_direction = -90
        CPWBendNew(c2.s5, angle=180, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
                   square=square)
        (x0, y0) = c2.s5.last
        x1 = x0 - 23.5
        y1 = y0 - 6.5
        c2.s5.last = (x1, y1)
        c2.s5.last_direction = 0
        CPWStraight(c2.s5, 26, 0, 6.5)
        c2.s5.last = (x0 + 21, y0)

    (x0, y0) = c2.s5.last
    x0 = x0 + 6.5
    y0 = y0 + 135.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 114.5, 0, 4)

    (x0, y0) = c2.s5.last
    x0 = x0 - 6.5
    y0 = y0 - 114.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = -90
    CPWBendNew(c2.s5, angle=90, pinw=0, gapw=10.5, radius=10.5, polyarc=1, segments=4,
               square=square)

    (x0, y0) = c2.s5.last
    x0 = x0 - 6.5
    y0 = y0 - 2.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 13, 0, 6.5)

    (x0, y0) = c2.s5.last
    x0 = x0 + 9
    y0 = y0 - 21
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 8, 0, 2.5)

    (x0, y0) = c2.s5.last
    x0 = x0 - 9 - 18.5
    y0 = y0 - 21 - 101.5
    c2.s5.last = (x0, y0)
    c2.s5.last_direction = 90
    CPWStraight(c2.s5, 135.5, 0, 4)

    c2.s5.last_direction = sss
    c2.s5.last = (x_a, y_a - 50)
    ############################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Draw_VSLQ_star(structure, xpos, ypos, flux_bias, junc_correction):
    #  The starting position of the code is at the top middle, where the flux line is coming, but slightly shifted
    c2 = structure
    cpw_pinw = 10.0
    cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)
    # Default settings for Xmon pad (left)
    shape1 = {}
    moregap = 30
    moveup = 13
    QQ_change = junc_correction['QQ_move']
    shape1['gapQ1'] = 30
    shape1['gapQ2'] = 30
    shape1['Q1_width'] = 75
    shape1['Q2_width'] = 75
    shape1['Q1_x'] = 680+30+10-5+5
    shape1['Q2_x'] = 420+30+10+10-5+5
    shape1['Q1_y'] = 155
    shape1['QQ_gap'] = 260-110-20+QQ_change
    shape1['Q_bar_rad'] = 20
    shape1['Q_bar_pin'] = 10
    shape1['Q_bar_x'] = 90+15-25-15
    shape1['Q_bar_y'] = 40
    shape1['Qc_pad_x'] = 100
    shape1['Qc_pad_y'] = 80
    shape1['Qc_pad_gapx'] = 80
    shape1['Qc_pad_gapy'] = 20-7
    shape1['Qc_pad_gapy_bottom'] = 25-7


    # Clean up metal
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    c2.s5.last = (xpos, ypos)
    # calculate top brick width

    Top_brick_x = shape1['Qc_pad_x'] + shape1['Qc_pad_gapx']*2
    Top_brick_y = shape1['Qc_pad_y'] + shape1['Qc_pad_gapy']
    Middle_brick_x = shape1['QQ_gap'] + shape1['Q1_width'] + shape1['Q2_width'] + shape1['gapQ1'] + shape1['gapQ2']
    Middle_brick_y = shape1['Q1_y'] + shape1['Q_bar_y'] + shape1['Qc_pad_gapy_bottom'] - shape1['gapQ1']+ shape1['Q_bar_rad']

    c2.s5.last_direction = -90
    CPWStraight(c2.s5, Top_brick_y, pinw=0, gapw=Top_brick_x/2)

    # calculate middle brick width

    c2.s5.last_direction = -90
    CPWStraight(c2.s5, Middle_brick_y, pinw=0, gapw=Middle_brick_x / 2)

    # calculate bottom brick width
    ref_pos2 = c2.s5.last
    Bottom_brick_x = shape1['QQ_gap'] + shape1['Q2_x'] + shape1['Q1_x'] + shape1['gapQ1'] + shape1['gapQ2'] + shape1['Q1_width']/2 + shape1['Q2_width']/2
    Bottom_brick_y = max(shape1['Q1_width'], shape1['Q2_width']) + shape1['gapQ1'] * 2
    c2.s5.last_direction = -90
    c2.s5.last = (c2.s5.last[0]-shape1['Q1_x']/2 + shape1['Q2_x']/2, c2.s5.last[1])
    ref_pos3 = c2.s5.last
    CPWStraight(c2.s5, Bottom_brick_y, pinw=0, gapw=Bottom_brick_x / 2)

    # clean up bottom metal
    ly = 250
    lx = shape1['QQ_gap']-shape1['gapQ1']-shape1['gapQ2']
    c2.s5.last_direction = 90
    c2.s5.last = (xpos, c2.s5.last[1])
    CPWStraight(c2.s5, ly, pinw=0, gapw=lx / 2)
    reff = c2.s5.last

    xx = reff[0] - lx/2
    yy = reff[1]
    curve_corner(c2.s5, xx, yy, 30, 3)

    xx = reff[0] + lx/2
    yy = reff[1]
    curve_corner(c2.s5, xx, yy, 30, 2)

    xx = reff[0] - lx/2
    yy = reff[1] - ly
    curve_corner(c2.s5, xx, yy, 30, 1)

    xx = reff[0] + lx/2
    yy = reff[1] - ly
    curve_corner(c2.s5, xx, yy, 30, 0)

    # Curve corners
    curve_large = 25-5-5
    curve_very_large = 40
    # top brick

    xx = xpos-max(Top_brick_x,0)/2
    yy = ypos
    curve_corner(c2.s5, xx, yy, curve_large, 3)

    xx = xpos + max(Top_brick_x,0) / 2
    yy = ypos
    curve_corner(c2.s5, xx, yy, curve_large, 2)

    xx = xpos -max(Top_brick_x,0)/2
    yy = ypos - Top_brick_y
    curve_corner(c2.s5, xx, yy, curve_large, 1)

    xx = xpos + max(Top_brick_x,0) / 2
    yy = ypos - Top_brick_y
    curve_corner(c2.s5, xx, yy, curve_large, 0)

    xx = ref_pos2[0] - max(0, Middle_brick_x) / 2
    yy = ypos - Top_brick_y
    curve_corner(c2.s5, xx, yy, curve_large, 3)

    xx = ref_pos2[0] + max(0, Middle_brick_x) / 2
    yy = ypos - Top_brick_y
    curve_corner(c2.s5, xx, yy, curve_large, 2)

    ## middle brick
    xx = ref_pos2[0] - max(0, Middle_brick_x) / 2
    yy = ref_pos2[1]
    curve_corner(c2.s5, xx, yy, curve_large, 1)

    xx = ref_pos2[0] + max(0, Middle_brick_x) / 2
    yy = ref_pos2[1]
    curve_corner(c2.s5, xx, yy, curve_large, 0)



    ## bottom brick
    xx = ref_pos3[0] - Bottom_brick_x / 2
    yy = ref_pos3[1]
    curve_corner(c2.s5, xx, yy, curve_very_large, 3)

    xx = ref_pos3[0] + Bottom_brick_x / 2
    yy = ref_pos3[1]
    curve_corner(c2.s5, xx, yy, curve_very_large, 2)

    xx = ref_pos3[0] - Bottom_brick_x / 2
    yy = ref_pos3[1] - Bottom_brick_y
    curve_corner(c2.s5, xx, yy, curve_very_large, 0)

    xx = ref_pos3[0] + Bottom_brick_x / 2
    yy = ref_pos3[1] - Bottom_brick_y
    curve_corner(c2.s5, xx, yy, curve_very_large, 1)

    ###############################################

    # Draw Coupler + shape pad

    c2.s5.last = (xpos, ypos - shape1['Qc_pad_gapy'])
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, shape1['Qc_pad_y'], pinw=0, gapw=shape1['Qc_pad_x'] / 2)
    #
    # c2.s5.last = (xpos-60, ypos - shape1['Qc_pad_gapy'])
    # c2.s5.last_direction = 270
    # CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    # CPWStraight(c2.s5, 2, pinw=0, gapw=3)
    #
    # c2.s5.last = (xpos +60, ypos - shape1['Qc_pad_gapy'])
    # c2.s5.last_direction = 270
    # CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    # CPWStraight(c2.s5, 2, pinw=0, gapw=3)
    #
    # c2.s5.last = (xpos - 60+1.5, ypos - shape1['Qc_pad_gapy']- shape1['Qc_pad_y'])
    # c2.s5.last_direction = 90
    # CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    # CPWStraight(c2.s5, 2, pinw=0, gapw=3)
    #
    # c2.s5.last = (xpos + 60-1.5, ypos - shape1['Qc_pad_gapy']- shape1['Qc_pad_y'])
    # c2.s5.last_direction = 90
    # CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    # CPWStraight(c2.s5, 2, pinw=0, gapw=3)
    #
    # c2.s5.last = (xpos, ypos - shape1['gapQc_y'])
    # c2.s5.last_direction = -90
    # CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    # CPWStraight(c2.s5, 2, pinw=0, gapw=3)
    #
    # curve corners
    curve_small = 9
    xx = xpos - shape1['Qc_pad_x']/ 2
    yy = ypos - shape1['Qc_pad_gapy']
    curve_corner(c2.s5, xx, yy, curve_small, 3)

    xx = xpos + shape1['Qc_pad_x'] / 2
    yy = ypos - shape1['Qc_pad_gapy']
    curve_corner(c2.s5, xx, yy, curve_small, 2)

    xx = xpos - shape1['Qc_pad_x'] / 2
    yy = ypos - shape1['Qc_pad_gapy'] - shape1['Qc_pad_y']
    curve_corner(c2.s5, xx, yy, curve_small, 0)

    xx = xpos + shape1['Qc_pad_x'] / 2
    yy = ypos - shape1['Qc_pad_gapy'] - shape1['Qc_pad_y']
    curve_corner(c2.s5, xx, yy, curve_small, 1)

    ##########################################
    # Qubit1 L shape pad
    xx = xpos-shape1['QQ_gap']/2 - shape1['Q1_width']/2
    yy = ypos - shape1['Qc_pad_gapy'] - shape1['Qc_pad_gapy_bottom'] - shape1['Q_bar_rad'] - shape1['Qc_pad_y']
    c2.s5.last = (xx, yy)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, shape1['Q_bar_y'], pinw=0, gapw=shape1['Q_bar_pin'] / 2)
    CPWStraight(c2.s5, shape1['Q1_y'], pinw=0, gapw=shape1['Q1_width'] / 2)
    c2.s5.last = (xx, yy)
    c2.s5.last_direction = 90
    CPWBendNew(c2.s5, angle=-90, pinw=0, gapw=shape1['Q_bar_pin'] / 2, radius=shape1['Q_bar_rad'], polyarc=1, segments=4,
                          square=0)
    CPWStraight(c2.s5, shape1['Q_bar_x'], pinw=0, gapw=shape1['Q_bar_pin'] / 2)
    c2.s5.last_direction = -90
    c2.s5.last = (c2.s5.last[0] - 6, c2.s5.last[1] + 5)
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)
    c2.s5.last_direction = 90
    c2.s5.last = (c2.s5.last[0], c2.s5.last[1] + 17)
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    c2.s5.last = (xx-shape1['Q1_x']/2+shape1['Q1_width']/2, yy-shape1['Q_bar_y']-shape1['Q1_y'])
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, shape1['Q1_width'], pinw=0, gapw=shape1['Q1_x'] / 2)

    # Q1 curve
    curve_Z = [5, 5, 20, 20, 25, 25, 25, 25]
    xpos11 = xx
    ypos11 = yy - shape1['Q_bar_y']
    xlistQ1 = [xpos11 - shape1['Q_bar_pin'] / 2, xpos11 + shape1['Q_bar_pin'] / 2,
               xpos11 - shape1['Q1_width'] / 2, xpos11 + shape1['Q1_width'] / 2,
               xpos11 - shape1['Q1_width'] / 2, xpos11 + shape1['Q1_width'] / 2,
               xpos11 - shape1['Q1_x'] + shape1['Q1_width'] / 2, xpos11 - shape1['Q1_x'] + shape1['Q1_width'] / 2]
    ylistQ1 = [ypos11, ypos11, ypos11, ypos11,
               ypos11 - shape1['Q1_y'], ypos11 - shape1['Q1_y'] - shape1['Q1_width'],
               ypos11 - shape1['Q1_y'], ypos11 - shape1['Q1_y'] - shape1['Q1_width']]
    cornerQ1 = [1, 0, 3, 2, 1, 1, 3, 0]
    for ii in range(len(cornerQ1)):
        curve_corner(c2.s5, xlistQ1[ii], ylistQ1[ii], curve_Z[ii], cornerQ1[ii])

    # Qubit2 L shape pad
    xx = xpos + shape1['QQ_gap'] / 2 + shape1['Q2_width'] / 2
    yy = ypos - shape1['Qc_pad_gapy'] - shape1['Qc_pad_gapy_bottom'] - shape1['Q_bar_rad'] - shape1['Qc_pad_y']
    c2.s5.last = (xx, yy)
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, shape1['Q_bar_y'], pinw=0, gapw=shape1['Q_bar_pin'] / 2)
    CPWStraight(c2.s5, shape1['Q1_y'], pinw=0, gapw=shape1['Q2_width'] / 2)
    c2.s5.last = (xx, yy)
    c2.s5.last_direction = 90
    CPWBendNew(c2.s5, angle=90, pinw=0, gapw=shape1['Q_bar_pin'] / 2, radius=shape1['Q_bar_rad'], polyarc=1,
               segments=4,
               square=0)
    CPWStraight(c2.s5, shape1['Q_bar_x'], pinw=0, gapw=shape1['Q_bar_pin'] / 2)
    c2.s5.last_direction = -90
    c2.s5.last = (c2.s5.last[0]+6,c2.s5.last[1]+5)
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    c2.s5.last_direction = 90
    c2.s5.last = (c2.s5.last[0], c2.s5.last[1] + 17)
    CPWStraight(c2.s5, 2, pinw=0, gapw=1)
    CPWStraight(c2.s5, 2, pinw=0, gapw=3)

    c2.s5.last = (xx + shape1['Q2_x'] / 2 - shape1['Q2_width'] / 2, yy - shape1['Q_bar_y'] - shape1['Q1_y'])
    c2.s5.last_direction = -90
    CPWStraight(c2.s5, shape1['Q2_width'], pinw=0, gapw=shape1['Q2_x'] / 2)

    # Q2 curve
    curve_Z = [5, 5, 20, 20, 25, 25, 25, 25]
    xpos11 = xx
    ypos11 = yy - shape1['Q_bar_y']
    xlistQ1 = [xpos11 + shape1['Q_bar_pin'] / 2, xpos11 - shape1['Q_bar_pin'] / 2,
               xpos11 + shape1['Q2_width'] / 2, xpos11 - shape1['Q2_width'] / 2,
               xpos11 + shape1['Q2_width'] / 2, xpos11 - shape1['Q2_width'] / 2,
               xpos11 + shape1['Q2_x'] - shape1['Q2_width'] / 2, xpos11 + shape1['Q2_x'] - shape1['Q2_width'] / 2]
    ylistQ1 = [ypos11, ypos11, ypos11, ypos11,
               ypos11 - shape1['Q1_y'], ypos11 - shape1['Q1_y'] - shape1['Q2_width'],
               ypos11 - shape1['Q1_y'], ypos11 - shape1['Q1_y'] - shape1['Q2_width']]
    cornerQ1 = [0,1,2,3,0,0,2,1]
    for ii in range(len(cornerQ1)):
        curve_corner(c2.s5, xlistQ1[ii], ylistQ1[ii], curve_Z[ii], cornerQ1[ii])





    ##########################################

    ## Draw Flux lines coming from the top

    linear = 50
    fluxpin = 3
    fluxgap = 11 - 3
    fluxw1 = 3.0
    fluxtapergap = 16.0+10
    ext = 4.5
    flux_rad = 100
    shifty = -60
    xtarget = c2.s3.last[0]
    ytarget = c2.s3.last[1]-2580
    reference11 = (xtarget, ytarget)
    y1 = 40
    y2 = 20

    xpos1 = xpos - 9-30+2.5+4.5+20-5.5-6+18+6-14-4-2
    ypos1 = ypos + y1 + cpw_pinw / 2 + 20 + fluxgap + fluxpin + linear + shifty+20-25-7-1+3
    c2.s5.last = (xtarget, ytarget)
    c2.s5.last_direction = 270
    # CPWStraight(c2.s5, ytarget - ypos1, pinw=cpw_pinw, gapw=cpw_gapw)

    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 270

    refer = c2.s5.last  # target end position
    direction = c2.s5.last_direction

    CPWLinearTaper(c2.s5, linear, start_pinw=cpw_pinw, stop_pinw=fluxw1, start_gapw=cpw_gapw,
                   stop_gapw=fluxtapergap)
    CPWStraight(c2.s5, 3, fluxw1, fluxtapergap)
    xpo = c2.s5.last[0]
    ypo = c2.s5.last[1]

    curve_small = 1.5
    xx = xpo - fluxw1 / 2
    yy = ypo
    curve_corner(c2.s5, xx, yy, curve_small, 1)

    xx = xpo + fluxw1 / 2
    yy = ypo
    curve_corner(c2.s5, xx, yy, curve_small, 0)

    xx = xpo - fluxtapergap- fluxw1 / 2
    yy = ypo
    curve_corner(c2.s5, xx, yy, curve_small, 0)

    xx = xpo + fluxtapergap+ fluxw1 / 2
    yy = ypo
    curve_corner(c2.s5, xx, yy, curve_small, 1)



    c2.s5.last = (xpos1, ypos1)
    c2.s5.last_direction = 90
    fluxy = c2.s4.last[1]-c2.s5.last[1]-flux_rad
    CPWStraight(c2.s5, fluxy, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=flux_rad, polyarc=1, segments=4,
               square=square)
    c2.s5.last_direction = 0
    fluxx = c2.s4.last[0] - c2.s5.last[0]
    CPWStraight(c2.s5, fluxx, cpw_pinw, cpw_gapw)

    if flux_bias:
        cut_x = 6
        cut_y = 4.5
        c2.s5.last = (xpos1-25.5+1, ypos1-51.5)
        c2.s5.last_direction = 270
        CPWStraight(c2.s5, cut_y, 0, cut_x/2)

        c2.s5.last = (xpos1 - 25.5+1.75, ypos1 - 51.5)
        c2.s5.last_direction = 270
        CPWStraight(c2.s5, 1.5, 0, 4.5 / 2)

        c2.s5.last = (xpos1 - 25.5 -1.25, ypos1 - 51.5)
        c2.s5.last_direction = 270
        CPWBendNew(c2.s5, angle=90, pinw=0, gapw=1.5/2, radius=1.5/2, polyarc=1, segments=4,
                   square=square)

        # curve corners

        curve_small = 1.5
        xx = xpos1-25.5-2
        yy = ypos1-56
        curve_corner(c2.s5, xx, yy, curve_small, 1)

        xx = xpos1 - 25.5 - 2+6
        yy = ypos1 - 56
        curve_corner(c2.s5, xx, yy, curve_small, 0)

        xx = xpos1 - 25.5 - 2+6
        yy = ypos1 - 56+3
        curve_corner(c2.s5, xx, yy, curve_small, 3)



    c2.s5.last = refer
    c2.s5.last_direction = direction

    # curve flux line
    # xx = xpos1 - (fluxtapergap * 2 + ext * 2 + fluxw1) / 2 + ext
    # yy = ypos1 - linear - fluxw1
    # curve_corner(c2.s5, xx, yy, fluxw1, 1)
    #
    # xx = xx + fluxtapergap
    # yy = ypos1 - linear - fluxw1
    # curve_corner(c2.s5, xx, yy, fluxw1, 0)
    #
    # xx = xpos1 - (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
    # yy = ypos1 - linear - fluxw1
    # curve_corner(c2.s5, xx, yy, fluxw1 / 2, 3)
    #
    # xx = xpos1 + (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
    # yy = ypos1 - linear - fluxw1
    # curve_corner(c2.s5, xx, yy, fluxw1 / 2, 2)
    #
    # xx = xpos1 - (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
    # yy = ypos1 - linear - fluxw1 * 2
    # curve_corner(c2.s5, xx, yy, fluxw1 / 2, 0)
    #
    # xx = xpos1 + (fluxtapergap * 2 + ext * 2 + fluxw1) / 2
    # yy = ypos1 - linear - fluxw1 * 2
    # curve_corner(c2.s5, xx, yy, fluxw1 / 2, 1)







    # ########################################
    # # draw junction connectors
    # shape2 = {}
    # shape2['top'] = 7
    # shape2['bottom'] = 7
    # shape2['length'] = shape1['QC_Q_y']
    # shape2['width'] = 10
    # curve

    #########################################
    # Draw LC resonator
    shape_LC = {}
    shape_LC['C_x'] = 630-45-5+5
    shape_LC['C_y'] = 575-5-5+5
    shape_LC['C_width'] = 40
    shape_LC['C_round'] = 90
    shape_LC['finger_number'] = 10
    shape_LC['finger_width'] = 5
    shape_LC['finger_gap'] = 10
    shape_LC['finger_length'] = 180+20-5



    xpos1 = xpos-1300-100+70+70-70-200+250+20-30-5+2-20+5+5-5+25-5+16+30-10
    ypos1 = ypos-650-10-5-100-20-20-15-15+10+5+5+5+2.5+10+5+7.5-1.5-1.5
    Lumped_LC_modified(c2, xpos1, ypos1, shape_LC, 1)

    # Left input charge1
    padlb = 25.0 * 0.75
    padwb = 10.0
    pgapwb = 20.0
    stubwb = 2.0

    rad = 50


    c2.s5.last = (xpos1-12-2-5-4+6-1.5-2, ypos1)
    c2.s5.last_direction = 180

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    # CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
    #            square=square)
    # CPWStraight(c2.s5, 400, cpw_pinw, cpw_gapw)
    # CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
    #            square=square)
    remaining = -c2.s0.last[0] + c2.s5.last[0] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s0.last[1] - c2.s5.last[1]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    # Left output
    padlb = 180.0 * 0.65-15
    padwb = 20.0
    pgapwb = 20.0
    stubwb = 5.0


    c2.s5.last = (xpos1+300+100, ypos1-300+15-11-5-40-15-10+0.5+5+5+5+2.5+2.0-3.0-1.0)
    c2.s5.last_direction = 270

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    remaining = c2.s5.last[1] - c2.s9.last[1] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)

    remaining = -c2.s9.last[0] + c2.s5.last[0]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    shape_LC['C_x'] = 600-45-5
    shape_LC['C_y'] = 545-5-5
    shape_LC['C_width'] = 40
    shape_LC['C_round'] = 90
    shape_LC['finger_number'] = 9
    shape_LC['finger_width'] = 5
    shape_LC['finger_gap'] = 11
    shape_LC['finger_length'] = 170+20-5

    xpos1 = xpos +300+650+200-80+20+50+100-175-50+20-20+28+10+20+5-5+5-20-16-30+10+QQ_change
    ypos1 = ypos - 1000+360-15-140+15-20-20+15+10+10+1.5+5+2.5-3+7.5-1.5-1.5
    Lumped_LC_modified(c2, xpos1, ypos1, shape_LC, 2)

    # Right input charge2
    padlb = 25.0 * 0.75
    padwb = 10.0
    pgapwb = 20.0
    stubwb = 2.0

    c2.s5.last = (xpos1+12+2+5+8-4-0.5-5+1.5+2-0.5, ypos1)
    c2.s5.last_direction = 0

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    remaining = c2.s6.last[0] - c2.s5.last[0] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s6.last[1] - c2.s5.last[1]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    # Right output
    padlb = 180.0 * 0.65-15
    padwb = 20.0
    pgapwb = 20.0
    stubwb = 5.0

    c2.s5.last = (xpos1-300-60, ypos1-300+25-11-5-70+18+2.5-3.5+2.5+8+2-1.0)
    c2.s5.last_direction = 270

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    # CPWStraight(c2.s5, 100, cpw_pinw, cpw_gapw)

    remaining = c2.s5.last[1] - c2.s7.last[1] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s7.last[0] - c2.s5.last[0]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)


    ########################################
    refer = c2.s5.last  # target end position
    direction = c2.s5.last_direction
    c2.s5.last = (refer[0]-2000+30-200, refer[1]+1350+5+7-100-1)
    c2.s5.last_direction = 90

    padlb = 25.0
    padwb = 10.0
    pgapwb = 20.0
    stubwb = 2.0
    radrad = 50


    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    CPWStraight(c2.s5, 800, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s5.last[0] - c2.s1.last[0] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s1.last[1] - c2.s5.last[1]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)


    # QR2

    c2.s5.last = (refer[0] -800-200, refer[1] + 1350+7-100+5-1)
    c2.s5.last_direction = 90

    padlb = 25.0
    padwb = 10.0
    pgapwb = 20.0
    stubwb = 2.0
    radrad = 50

    CoupPad(c2.s5, padw=padwb, padl=padlb, corner_rad=2.0, connecw=stubwb, connecl=pgapwb, gapw=pgapwb,
            coupstart=1, square=square)
    CPWLinearTaper(c2.s5, 200.0, stubwb, cpw_pinw, cpw_gapw, cpw_gapw)
    CPWStraight(c2.s5, 800, cpw_pinw, cpw_gapw)
    CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s6.last[0] - c2.s5.last[0] - rad
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)

    CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=rad, polyarc=1, segments=4,
               square=square)
    remaining = c2.s1.last[1] - c2.s5.last[1]
    CPWStraight(c2.s5, remaining, cpw_pinw, cpw_gapw)



    ##########################################
    # # Coupler QR1 DC lines
    # # Now no direct charge lines but capactive coupler between qubit and resonator
    # c2.s5.last = (refer[0]-1330+200+60, refer[1]-50-135-50+5)
    # c2.s5.last_direction = 90
    # xpos1 = c2.s5.last[0]
    # ypos1 = c2.s5.last[1]
    # padlb = 25.0
    # padwb = 10.0
    # pgapwb = 20.0
    # stubwb = 2.0
    # radrad = 50
    # c2.s5.last = (xpos1, ypos1)
    # c2.s5.last_direction = 270+90
    # refer = c2.s5.last  # target end position
    # direction = c2.s5.last_direction
    # CPWLinearTaper(c2.s5, linear, start_pinw=cpw_pinw, stop_pinw=fluxw1, start_gapw=cpw_gapw,
    #                stop_gapw=fluxtapergap)
    #
    # c2.s5.last = (xpos1 + linear, ypos1 - cpw_pinw / 2 - ext)
    # c2.s5.last_direction = 270+90
    # CPWStraight(c2.s5, fluxw1, pinw=0, gapw=fluxtapergap / 2)
    #
    # c2.s5.last = (xpos1 + linear + fluxw1, ypos1)
    # c2.s5.last_direction = 270+90
    # CPWStraight(c2.s5, fluxw1, pinw=0, gapw=(fluxtapergap * 2 + ext * 2 + fluxw1) / 2)
    # refQR1 = c2.s5.last
    #
    # c2.s5.last_direction = 180
    # c2.s5.last = (xpos1, ypos1)
    # CPWStraight(c2.s5, 100, pinw=cpw_pinw, gapw=cpw_gapw)
    # CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # CPWStraight(c2.s5, 300, pinw=cpw_pinw, gapw=cpw_gapw)
    # CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # CPWStraight(c2.s5, 1300, pinw=cpw_pinw, gapw=cpw_gapw)
    # CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # CPWStraight(c2.s5, 970, pinw=cpw_pinw, gapw=cpw_gapw)
    # CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # CPWStraight(c2.s5, 530, pinw=cpw_pinw, gapw=cpw_gapw)
    # remaining = c2.s1.last[1]-c2.s5.last[1]-radrad*2
    # CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # CPWStraight(c2.s5, remaining, pinw=cpw_pinw, gapw=cpw_gapw)
    # CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # remaining = c2.s5.last[0] - c2.s1.last[0]
    # CPWStraight(c2.s5, remaining, pinw=cpw_pinw, gapw=cpw_gapw)
    #
    # #######
    # c2.s5.last = (refer[0] + 1410+370+220-50-50, refer[1]+4)
    # c2.s5.last_direction = 90
    # xpos1 = c2.s5.last[0]
    # ypos1 = c2.s5.last[1]
    # padlb = 25.0
    # padwb = 10.0
    # pgapwb = 20.0
    # stubwb = 2.0
    # radrad = 50
    # c2.s5.last = (xpos1, ypos1)
    # c2.s5.last_direction = 270 - 90
    # refer = c2.s5.last  # target end position
    # direction = c2.s5.last_direction
    # CPWLinearTaper(c2.s5, linear, start_pinw=cpw_pinw, stop_pinw=fluxw1, start_gapw=cpw_gapw,
    #                stop_gapw=fluxtapergap)
    #
    # c2.s5.last = (xpos1 - linear, ypos1 - cpw_pinw / 2 - ext)
    # c2.s5.last_direction = 270 - 90
    # CPWStraight(c2.s5, fluxw1, pinw=0, gapw=fluxtapergap / 2)
    #
    # c2.s5.last = (xpos1 - linear - fluxw1, ypos1)
    # c2.s5.last_direction = 270 - 90
    # CPWStraight(c2.s5, fluxw1, pinw=0, gapw=(fluxtapergap * 2 + ext * 2 + fluxw1) / 2)
    # refQR2 = c2.s5.last
    #
    # c2.s5.last_direction = 0
    # c2.s5.last = (xpos1, ypos1)
    #
    # CPWStraight(c2.s5, 800, pinw=cpw_pinw, gapw=cpw_gapw)
    # remaining = c2.s5.last[1] - c2.s6.last[1] - radrad * 2
    # CPWBendNew(c2.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # CPWStraight(c2.s5, remaining, pinw=cpw_pinw, gapw=cpw_gapw)
    # CPWBendNew(c2.s5, angle=90, pinw=cpw_pinw, gapw=cpw_gapw, radius=radrad, polyarc=1, segments=4,
    #            square=square)
    # remaining = c2.s6.last[0] - c2.s5.last[0]
    # CPWStraight(c2.s5, remaining, pinw=cpw_pinw, gapw=cpw_gapw)


    ############################################
    ### resonator in and out





    ########################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Draw_test_large(structure, xpos, ypos):
    c2 = structure
    ##########################################
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    pad_x = 700
    pad_y = 350
    gap = 50
    length = 200
    cpw_pinw = 10.0
    cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)
    # Default settings for junction box (together with top flux line)
    xpos1 = xpos
    ypos1 = ypos
    shape3 = {}
    shape3['curve'] = 5
    shape3['x'] = 60
    shape3['y1'] = 30
    shape3['y2'] = 30
    shape3['flux_dis'] = 2
    shape3['flux_shift'] = 0  # x position shift relative to the center
    shape3['extension'] = 100  # extending lengtth of CPW
    shift_x = [-300,-200, -100, 100, 200, 300, 0]
    for sx in shift_x:
        junctionbox_test(c2, xpos1+sx, ypos1, shape3)

    c2.s5.last_direction = 90

    for sx in shift_x:
        c2.s5.last = (xpos1+sx, ypos1 + shape3['x'] / 2 + shape3['extension'])
        CPWStraight(c2.s5, length, pinw=cpw_pinw, gapw=cpw_gapw)
        CPWStraight(c2.s5, gap, pinw=0, gapw=(cpw_pinw)/2)
    c2.s5.move(-gap)
    CPWStraight(c2.s5, gap, pinw=0, gapw=(gap * 2 + pad_x) / 2)
    CPWStraight(c2.s5, pad_y, pinw=pad_x, gapw=gap)
    CPWStraight(c2.s5, gap, pinw=0, gapw=gap + pad_x / 2)

    c2.s5.last_direction = 270
    for sx in shift_x:
        c2.s5.last = (xpos1+sx, ypos1 - shape3['x'] / 2 - shape3['extension'])
        CPWStraight(c2.s5, length, pinw=cpw_pinw, gapw=cpw_gapw)
        CPWStraight(c2.s5, gap, pinw=0, gapw=(cpw_pinw) / 2)
    c2.s5.move(-gap)
    CPWStraight(c2.s5, gap, pinw=0, gapw=(gap * 2 + pad_x ) / 2)
    CPWStraight(c2.s5, pad_y, pinw=pad_x, gapw=gap)
    CPWStraight(c2.s5, gap, pinw=0, gapw=gap + pad_x / 2)

    ########################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Draw_VSLQ_startest(structure, xpos, ypos):
    c2 = structure
    ##########################################
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    pad = 430
    gap = 50
    length = 20
    cpw_pinw = 10.0
    cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)
    # Default settings for junction box (together with top flux line)
    xpos1 = xpos
    ypos1 = ypos
    shape3 = {}
    shape3['curve'] = 5
    shape3['x'] = 60
    shape3['y1'] = 30
    shape3['y2'] = 30
    shape3['flux_dis'] = 2
    shape3['flux_shift'] = 0  # x position shift relative to the center
    shape3['extension'] = 100  # extending lengtth of CPW
    junctionbox_test(c2, xpos1, ypos1, shape3)

    c2.s5.last_direction = 90
    c2.s5.last = (xpos1, ypos1 + shape3['x'] / 2 + shape3['extension'])
    CPWStraight(c2.s5, length, pinw=cpw_pinw, gapw=cpw_gapw)
    CPWStraight(c2.s5, gap, pinw=cpw_pinw, gapw=(gap * 2 + pad - cpw_pinw) / 2)
    CPWStraight(c2.s5, pad, pinw=pad, gapw=gap)
    CPWStraight(c2.s5, gap, pinw=0, gapw=gap + pad / 2)

    c2.s5.last_direction = 270
    c2.s5.last = (xpos1, ypos1 - shape3['x'] / 2 - shape3['extension'])
    CPWStraight(c2.s5, length, pinw=cpw_pinw, gapw=cpw_gapw)
    CPWStraight(c2.s5, gap, pinw=cpw_pinw, gapw=(gap * 2 + pad - cpw_pinw) / 2)
    CPWStraight(c2.s5, pad, pinw=pad, gapw=gap)
    # CPWStraight(c2.s5, gap, pinw=0, gapw=gap + pad / 2)

    ########################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def Draw_VSLQ_startest_ground(structure, xpos, ypos):
    c2 = structure
    ##########################################
    ref_pos1 = c2.s5.last
    ref_direction = c2.s5.last_direction
    pad = 430
    gap = 50
    length = 20
    cpw_pinw = 10.0
    cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)
    # Default settings for junction box (together with top flux line)
    xpos1 = xpos
    ypos1 = ypos
    shape3 = {}
    shape3['curve'] = 5
    shape3['x'] = 60
    shape3['y1'] = 30
    shape3['y2'] = 30
    shape3['flux_dis'] = 2
    shape3['flux_shift'] = 0  # x position shift relative to the center
    shape3['extension'] = 100  # extending lengtth of CPW
    junctionbox_test(c2, xpos1, ypos1, shape3)

    c2.s5.last_direction = 90
    c2.s5.last = (xpos1, ypos1 + shape3['x'] / 2 + shape3['extension'])
    CPWStraight(c2.s5, length, pinw=cpw_pinw, gapw=cpw_gapw)
    CPWStraight(c2.s5, gap, pinw=cpw_pinw, gapw=(gap * 2 + pad - cpw_pinw) / 2)
    CPWStraight(c2.s5, pad, pinw=pad, gapw=gap)
    CPWStraight(c2.s5, gap, pinw=0, gapw=gap + pad / 2)

    c2.s5.last_direction = 270
    c2.s5.last = (xpos1, ypos1 - shape3['x'] / 2 - shape3['extension'])
    CPWStraight(c2.s5, length, pinw=cpw_pinw, gapw=cpw_gapw)
    CPWStraight(c2.s5, gap, pinw=cpw_pinw, gapw=(gap * 2 + pad/2 - cpw_pinw) / 2)
    CPWStraight(c2.s5, pad/2, pinw=pad/2, gapw=gap)
    # CPWStraight(c2.s5, gap, pinw=0, gapw=gap + pad/2)

    ########################################
    c2.s5.last_direction = ref_direction
    c2.s5.last = ref_pos1


def draw_coupler_frame(structure, xpos, ypos, direction):
    c = structure
    pin_ref = c.s2.pin_layer.last
    pin_direction = c.s2.pin_layer.last_direction
    gap_ref = c.s2.gap_layer.last
    gap_direction = c.s2.gap_layer.last_direction
    loopx = 40
    loopy = 15
    looparm = 2
    looparm_SQUID = looparm
    bar_arm = 9

    boxx = 12
    boxy = 7 + 4
    c.s2.pin_layer.last_direction = direction*180
    c.s2.pin_layer.last = (xpos, ypos)
    # SQUID loop
    CPWStraight(c.s2.pin_layer, 5, pinw=0, gapw=boxx * 4 / 2)
    # CPWStraight(c.s2.pin_layer, 0, pinw=0, gapw=bar_arm / 2)
    # CPWStraight(c.s2.pin_layer, looparm_SQUID*0, pinw=0, gapw=loopx / 2+looparm_SQUID/2)
    CPWStraight(c.s2.pin_layer, loopy - looparm_SQUID, pinw=loopx - looparm_SQUID, gapw=looparm_SQUID)
    CPWStraight(c.s2.pin_layer, looparm_SQUID, pinw=0, gapw=loopx / 2 + looparm_SQUID / 2)
    SQUIDgap = 2 + looparm_SQUID + 1.5
    CPWStraight(c.s2.pin_layer, SQUIDgap, pinw=0, gapw=bar_arm / 2)
    CPWStraight(c.s2.pin_layer, 8, pinw=0, gapw=25 / 2)
    # # junction bar
    # inducbox = 60
    # junc_bar = 75
    # junc_y = 12 - loopy + 18 + 4
    # CPWStraight(c.s2.pin_layer, looparm, pinw=0, gapw=junc_bar / 2+looparm/2)
    # CPWStraight(c.s2.pin_layer, junc_y, pinw=junc_bar - looparm, gapw=looparm)
    # # CPWStraight(c.s2.pin_layer, looparm, pinw=junc_bar - looparm, gapw=(inducbox - junc_bar + looparm) / 2)
    # # c.s2.pin_layer.move(-looparm / 2 - boxx / 2)
    # CPWStraight(c.s2.pin_layer, boxx, pinw=junc_bar-boxx, gapw=boxy-looparm/2)

    ################################################
    c.s2.pin_layer.last = pin_ref
    c.s2.gap_layer.last = gap_ref
    c.s2.pin_layer.last_direction = pin_direction
    c.s2.gap_layer.last_direction = gap_direction


def draw_junction_frame(structure, xpos, ypos, junc_para, loop):
    c = structure
    pin_ref = c.s2.pin_layer.last
    pin_direction = c.s2.pin_layer.last_direction
    gap_ref = c.s2.gap_layer.last
    gap_direction = c.s2.gap_layer.last_direction
    pinwidth = loop['pinw']
    pinlength = loop['pinl']

    boxx = loop['x']
    boxy = loop['y']
    c.s2.pin_layer.last_direction = 90
    c.s2.pin_layer.last = (xpos, ypos)
    CPWStraight(c.s2.pin_layer, pinlength/2, pinw=0, gapw=pinwidth/2)
    CPWStraight(c.s2.pin_layer, boxy, pinw=0, gapw=boxx/2)

    c.s2.pin_layer.last_direction = 270
    c.s2.pin_layer.last = (xpos, ypos)
    CPWStraight(c.s2.pin_layer, pinlength / 2, pinw=0, gapw=pinwidth / 2)
    CPWStraight(c.s2.pin_layer, boxy, pinw=0, gapw=boxx / 2)

    ################################################
    c.s2.pin_layer.last = pin_ref
    c.s2.gap_layer.last = gap_ref
    c.s2.pin_layer.last_direction = pin_direction
    c.s2.gap_layer.last_direction = gap_direction


def draw_test_frame(structure, xpos, ypos, junc_para, loop):
    c = structure
    pin_ref = c.s2.pin_layer.last
    pin_direction = c.s2.pin_layer.last_direction
    gap_ref = c.s2.gap_layer.last
    gap_direction = c.s2.gap_layer.last_direction

    c.s2.pin_layer.last = (xpos, ypos)
    arm = loop['arm']
    boxx = 20
    boxy = 20
    c.s2.pin_layer.last_direction = 90+90
    CPWStraight(c.s2.pin_layer, 6.5, pinw=0, gapw=arm / 2)
    CPWStraight(c.s2.pin_layer, boxy, pinw=0, gapw=boxx / 2)

    c.s2.pin_layer.last = (xpos, ypos)
    c.s2.pin_layer.last_direction = 270+90
    CPWStraight(c.s2.pin_layer, 6.5, pinw=0, gapw=arm / 2)
    CPWStraight(c.s2.pin_layer, boxy, pinw=0, gapw=boxx / 2)

    ################################################
    c.s2.pin_layer.last = pin_ref
    c.s2.gap_layer.last = gap_ref
    c.s2.pin_layer.last_direction = pin_direction
    c.s2.gap_layer.last_direction = gap_direction


def Draw_SIPF(structure, length, reference1):
    cpw_rad = 30
    cpw_rad1 = 215
    cpw_rad2 = cpw_rad1
    max_len = length
    cpw_pinw1 = 85
    cpw_gapw1 = 10
    cpw_pinw2 = 10
    cpw_gapw2 = 85
    taperl = 80
    square = 0

    global sign
    global draw_len

    sign = 1
    draw_len = 0

    c1 = structure

    # draw the input coupler

    save = c1.s5.last
    save_d = c1.s5.last_direction

    c1.s5.last = (c1.s6.last[0],c1.s6.last[1]+2250)
    c1.s5.last_direction = 180

    CPWStraight(c1.s5, 100.0, pinw=cpw_pinw, gapw=cpw_gapw)
    CPWBendNew(c1.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=cpw_rad, polyarc=1, segments=4,
               square=square)
    CPWStraight(c1.s5, 100.0, pinw=cpw_pinw, gapw=cpw_gapw)
    # cap_coupling_6_fingers(c1.s3, finger_cap_l, coupler_c_pad_length, cpw_pinw, cpw_pinw, cpw_gapw,
    # cpw_gapw)
    CPWLinearTaper(c1.s5, taperl, start_pinw=cpw_pinw, stop_pinw=cpw_pinw1, start_gapw=cpw_gapw,
                   stop_gapw=cpw_gapw1)

    # Section 1: low impedance
    section1 = max_len - cpw_rad - taperl
    CPWStraight(c1.s5, 100, pinw=cpw_pinw1, gapw=cpw_gapw1)
    section1 -= 100
    CPWBendNew(c1.s5, angle=-60, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi/3*cpw_rad1
    CPWStraight(c1.s5, 700, pinw=cpw_pinw1, gapw=cpw_gapw1)
    section1 -= 700
    CPWBendNew(c1.s5, angle=60, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi/3*cpw_rad1
    CPWStraight(c1.s5, 400, pinw=cpw_pinw1, gapw=cpw_gapw1)
    section1 -= 400
    CPWBendNew(c1.s5, angle=90, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi / 2 * cpw_rad1
    CPWStraight(c1.s5, section1, pinw=cpw_pinw1, gapw=cpw_gapw1)

    CPWLinearTaper(c1.s5, taperl, start_pinw=cpw_pinw1, stop_pinw=cpw_pinw2, start_gapw=cpw_gapw1,
                   stop_gapw=cpw_gapw2)

    # Section 2: high impedance
    section1 = max_len - cpw_rad - taperl
    CPWStraight(c1.s5, 1050, pinw=cpw_pinw2, gapw=cpw_gapw2)
    section1 -= 1050
    CPWBendNew(c1.s5, angle=180, pinw=cpw_pinw2, gapw=cpw_gapw2, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi * cpw_rad1
    CPWStraight(c1.s5, section1, pinw=cpw_pinw2, gapw=cpw_gapw2)
    # section1 -= 4580
    # CPWBendNew(c1.s5, angle=-180, pinw=cpw_pinw2, gapw=cpw_gapw2, radius=cpw_rad1, polyarc=1, segments=4,
    #            square=square)
    # section1 -= np.pi * cpw_rad1
    # CPWStraight(c1.s5, section1, pinw=cpw_pinw2, gapw=cpw_gapw2)
    CPWLinearTaper(c1.s5, taperl, start_pinw=cpw_pinw2, stop_pinw=cpw_pinw1, start_gapw=cpw_gapw2,
                   stop_gapw=cpw_gapw1)
    # Section 3: low impedance
    section1 = max_len - cpw_rad - taperl

    CPWStraight(c1.s5, 250, pinw=cpw_pinw1, gapw=cpw_gapw1)
    section1 -= 250
    CPWBendNew(c1.s5, angle=-180, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi * cpw_rad1
    CPWStraight(c1.s5, 4000, pinw=cpw_pinw1, gapw=cpw_gapw1)
    section1 -= 4000
    CPWBendNew(c1.s5, angle=180, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi * cpw_rad1
    CPWStraight(c1.s5, section1, pinw=cpw_pinw1, gapw=cpw_gapw1)
    # section1 -= 3070
    # CPWBendNew(c1.s5, angle=180, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
    #            square=square)
    # section1 -= np.pi * cpw_rad1
    # CPWStraight(c1.s5, section1, pinw=cpw_pinw1, gapw=cpw_gapw1)
    CPWLinearTaper(c1.s5, taperl, start_pinw=cpw_pinw1, stop_pinw=cpw_pinw2, start_gapw=cpw_gapw1,
                   stop_gapw=cpw_gapw2)

    # Section 4: high impedance
    section1 = max_len - cpw_rad - taperl
    CPWStraight(c1.s5, 2800, pinw=cpw_pinw2, gapw=cpw_gapw2)
    section1 -= 2800
    CPWBendNew(c1.s5, angle=-180, pinw=cpw_pinw2, gapw=cpw_gapw2, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi * cpw_rad1
    CPWStraight(c1.s5, section1, pinw=cpw_pinw2, gapw=cpw_gapw2)
    CPWLinearTaper(c1.s5, taperl, start_pinw=cpw_pinw2, stop_pinw=cpw_pinw1, start_gapw=cpw_gapw2,
                   stop_gapw=cpw_gapw1)

    # Section5: low impedance
    section1 = max_len - cpw_rad - taperl
    CPWStraight(c1.s5, 150, pinw=cpw_pinw1, gapw=cpw_gapw1)
    section1 -= 150
    CPWBendNew(c1.s5, angle=180, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi * cpw_rad1
    CPWStraight(c1.s5, 4000, pinw=cpw_pinw1, gapw=cpw_gapw1)
    section1 -= 4000
    CPWBendNew(c1.s5, angle=-180, pinw=cpw_pinw1, gapw=cpw_gapw1, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi * cpw_rad1

    CPWStraight(c1.s5, section1, pinw=cpw_pinw1, gapw=cpw_gapw1)

    CPWLinearTaper(c1.s5, taperl, start_pinw=cpw_pinw1, stop_pinw=cpw_pinw2, start_gapw=cpw_gapw1,
                   stop_gapw=cpw_gapw2)
    # section6: high impedance
    section1 = max_len - cpw_rad - taperl

    CPWStraight(c1.s5, 3800, pinw=cpw_pinw2, gapw=cpw_gapw2)
    section1 -= 3800
    CPWBendNew(c1.s5, angle=180, pinw=cpw_pinw2, gapw=cpw_gapw2, radius=cpw_rad1, polyarc=1, segments=4,
               square=square)
    section1 -= np.pi * (cpw_rad1)

    CPWStraight(c1.s5, section1, pinw=cpw_pinw2, gapw=cpw_gapw2)
    CPWLinearTaper(c1.s5, taperl, start_pinw=cpw_pinw2, stop_pinw=cpw_pinw, start_gapw=cpw_gapw2,
                   stop_gapw=cpw_gapw)
    target1 = reference1[0]-c1.s5.last[0]-cpw_rad
    CPWStraight(c1.s5, target1, pinw=cpw_pinw, gapw=cpw_gapw)
    CPWBendNew(c1.s5, angle=-90, pinw=cpw_pinw, gapw=cpw_gapw, radius=cpw_rad, polyarc=1, segments=4,
               square=square)

    connect = c1.s5.last[1]-reference1[1]
    CPWStraight(c1.s5, connect, pinw=cpw_pinw, gapw=cpw_gapw)

    c1.s5.last = save
    c1.s5.last_direction = save_d


def draw_junction_large(structure, xpos, ypos, junc_correction, loop, junction_number, flag):
    c = structure
    pin_ref = c.s2.pin_layer.last
    pin_direction = c.s2.pin_layer.last_direction
    gap_ref = c.s2.gap_layer.last
    gap_direction = c.s2.gap_layer.last_direction
    linear = junc_correction['junction_linear_large']
    gap_protect = junc_correction['gap_protect']
    looparm = loop['arm']
    if junction_number == 1:
        junction_width = junc_correction['junction1_length']
        junction_gap = junc_correction['junction1_gap']
    if junction_number == 2:
        junction_width = junc_correction['junction2_length']
        junction_gap = junc_correction['junction2_gap']

    junc_arm = 1
    block_length = junction_gap + linear * 2 + junc_arm * 2
    if (flag == 0) or (flag == -1):
        # Clear the junction block
        c.s2.pin_layer.last = (xpos, ypos - linear)
        c.s2.pin_layer.last_direction = 90
        CPWStraight(c.s2.pin_layer, block_length, pinw=0, gapw=looparm / 2)

    if flag == -1:
        # Draw junction
        c.s2.pin_layer.last = (xpos, ypos - linear)
        c.s2.pin_layer.last_direction = 90
        CPWLinearTaper(c.s2.pin_layer, linear, 0, 0, looparm / 2, junction_width / 2)
        CPWStraight(c.s2.pin_layer, junc_arm, pinw=0, gapw=junction_width / 2)
        c.s2.pin_layer.move(junction_gap)
        CPWStraight(c.s2.pin_layer, junc_arm, pinw=0, gapw=junction_width / 2)
        CPWLinearTaper(c.s2.pin_layer, linear, 0, 0, junction_width / 2, looparm / 2)

        # Draw gap layer
        gap_wrap = 2
        c.s2.gap_layer.last = (xpos, ypos - linear - gap_wrap)
        c.s2.gap_layer.last_direction = 90
        CPWStraight(c.s2.gap_layer, gap_wrap, pinw=looparm, gapw=gap_protect)
        CPWLinearTaper(c.s2.gap_layer, linear, looparm, junction_width, gap_protect, gap_protect)
        CPWStraight(c.s2.gap_layer, junc_arm, pinw=junction_width, gapw=gap_protect)
        CPWStraight(c.s2.gap_layer, junction_gap, pinw=0, gapw=junction_width / 2 + gap_protect)
        CPWStraight(c.s2.gap_layer, junc_arm, pinw=junction_width, gapw=gap_protect)
        CPWLinearTaper(c.s2.gap_layer, linear, junction_width, looparm, gap_protect, gap_protect)
        CPWStraight(c.s2.gap_layer, gap_wrap, pinw=looparm, gapw=gap_protect)

    ################################################
    c.s2.pin_layer.last = pin_ref
    c.s2.gap_layer.last = gap_ref
    c.s2.pin_layer.last_direction = pin_direction
    c.s2.gap_layer.last_direction = gap_direction


def draw_junction_small(structure, xpos, ypos, junc_correction, loop, junction_number, flag):
    c = structure
    pin_ref = c.s2.pin_layer.last
    pin_direction = c.s2.pin_layer.last_direction
    gap_ref = c.s2.gap_layer.last
    gap_direction = c.s2.gap_layer.last_direction
    linear = junc_correction['junction_linear']
    gap_protect = junc_correction['gap_protect']
    junc_arm = junc_correction['junc_arm']
    looparm = loop['arm']
    if junction_number == 3:
        junction_width = junc_correction['junction3_length']
        junction_gap = junc_correction['junction3_gap']
    if junction_number == 4:
        junction_width = junc_correction['junction4_length']
        junction_gap = junc_correction['junction4_gap']
    if junction_number == 5:
        junction_width = junc_correction['junction5_length']
        junction_gap = junc_correction['junction5_gap']
    if junction_number == 6:
        junction_width = junc_correction['junction6_length']
        junction_gap = junc_correction['junction6_gap']
    if junction_number == 7:
        junction_width = junc_correction['junction7_length']
        junction_gap = junc_correction['junction7_gap']
    if junction_number == 8:
        junction_width = junc_correction['junction8_length']
        junction_gap = junc_correction['junction8_gap']

    block_length = junction_gap + junc_arm + linear
    if (flag == 0) or (flag == -1):
        # Clear the junction block
        c.s2.pin_layer.last = (xpos, ypos)
        c.s2.pin_layer.last_direction = 90+90
        CPWStraight(c.s2.pin_layer, block_length, pinw=0, gapw=looparm / 2)
    if flag == -1:
        # Draw junction
        c.s2.pin_layer.last = (xpos - junction_gap, ypos)
        c.s2.pin_layer.last_direction = 90+90
        CPWStraight(c.s2.pin_layer, junc_arm, pinw=0, gapw=junction_width / 2)
        CPWLinearTaper(c.s2.pin_layer, linear, 0, 0, junction_width / 2, looparm / 2)
        # Draw gap layer
        gap_wrap = 3
        c.s2.gap_layer.last = (xpos + gap_wrap, ypos)
        c.s2.gap_layer.last_direction = 90+90
        CPWStraight(c.s2.gap_layer, gap_wrap, pinw=looparm, gapw=gap_protect)
        CPWStraight(c.s2.gap_layer, junction_gap, pinw=0, gapw=looparm / 2 + gap_protect)
        CPWStraight(c.s2.gap_layer, junc_arm, pinw=junction_width, gapw=gap_protect)
        CPWLinearTaper(c.s2.gap_layer, linear, junction_width, looparm, gap_protect, gap_protect)
        CPWStraight(c.s2.gap_layer, gap_wrap, pinw=looparm, gapw=gap_protect)

    ################################################
    c.s2.pin_layer.last = pin_ref
    c.s2.gap_layer.last = gap_ref
    c.s2.pin_layer.last_direction = pin_direction
    c.s2.gap_layer.last_direction = gap_direction


def draw_SIPF(structure, d, length):
    c = structure
    ## alignment boxes for e-beam
    if (draw_layer1 == True) and (draw_layer2 == False):
        draw_launchers(c, d, exclude=[0, 1, 2, 4, 5, 6, 7, 9])
        draw_square_alignment_marks(c)
        Draw_SIPF(c, length, c.s8.last)
    else:
        draw_launchers(c, d, exclude=[0, 1, 2, 4, 5, 6, 7, 9])
        draw_launchers(c, d, exclude=[0, 1, 2, 4, 5, 6, 7, 9])
        draw_square_alignment_marks(c)


def draw_bridge_junction(structure, d, junc_correction, flux_bias):
    c = structure
    ## alignment boxes for e-beam
    if (draw_layer1 == True) and (draw_layer2 == False):
        draw_launchers(c, d, exclude=[2, 3, 8])
        draw_square_alignment_marks(c)
    else:
        draw_launchers(c, d, exclude=[2, 3, 8])
        draw_launchers(c, d, exclude=[2, 3, 8])
        draw_square_alignment_marks(c)
    ## Junction parameters

    xpos = (c.s1.last[0] + c.s5.last[0]) / 2.
    ypos = (c.s1.last[1] + c.s0.last[1]) / 2.
    # Draw VSLQ test structure
    xlist = [1450, 1450, 2100, 2100]
    ylist = [4250, 5600, 4250, 5600]
    if draw_layer1 == True:
        # Draw VSLQ star pad
        Draw_VSLQ_star(c, xpos, ypos-800+150, flux_bias, junc_correction)

        Draw_VSLQ_startest_ground(c, xlist[0], ylist[0])
        Draw_VSLQ_startest_ground(c, xlist[1], ylist[1])
        Draw_VSLQ_startest_ground(c, xlist[2], ylist[2])
        Draw_VSLQ_startest_ground(c, xlist[3], ylist[3])
        if perf:
            perforate(c, 50, 50)
    pin_length = 0
    if draw_layer2 == True:
        # xpos = 400
        # ypos = 400
        # c.s2.gap_layer.last = (xpos, ypos)
        # c.s2.gap_layer.last_direction = 90
        # ll = [0.15, 6.3, 7.5]
        # gg = [0.14, 0.16, 0.19, 0.21]
        # movex = 200
        # movey = 200
        # fx = 0
        # fy = 0
        # for yy in ll:
        #     fy +=1
        #     fx = 0
        #     for xx in gg:
        #         fx += 1
        #         c.s2.gap_layer.last = (xpos+fx*movex, ypos+fy*movey)
        #         c.s2.gap_layer.last_direction = 90
        #         CPWStraight(c.s2.gap_layer, yy, pinw=0, gapw=1)
        #
        #         c.s2.gap_layer.last = (xpos + fx * movex+xx+2, ypos + fy * movey)
        #         c.s2.gap_layer.last_direction = 90
        #         CPWStraight(c.s2.gap_layer, yy, pinw=0, gapw=1)
        #
        # fx = 0
        # fy = 0
        # for yy in ll:
        #     fy +=1
        #     fx = 0
        #     for xx in gg:
        #         fx += 1
        #         c.s2.gap_layer.last = (xpos+fx*movex+2000, ypos+fy*movey)
        #         c.s2.gap_layer.last_direction = 90
        #         CPWStraight(c.s2.gap_layer, yy, pinw=0, gapw=xx/2)
        #
        #         c.s2.gap_layer.last = (xpos + fx * movex+xx*2+2000, ypos + fy * movey)
        #         c.s2.gap_layer.last_direction = 90
        #         CPWStraight(c.s2.gap_layer, yy, pinw=0, gapw=xx/2)
        #
        #         c.s2.gap_layer.last = (xpos + fx * movex + xx*4 + 2000, ypos + fy * movey)
        #         c.s2.gap_layer.last_direction = 90
        #         CPWStraight(c.s2.gap_layer, yy, pinw=0, gapw=xx / 2)
        #
        #         c.s2.gap_layer.last = (xpos + fx * movex + xx*6 + 2000, ypos + fy * movey)
        #         c.s2.gap_layer.last_direction = 90
        #         CPWStraight(c.s2.gap_layer, yy, pinw=0, gapw=xx / 2)
        if flux_bias:
            large_corr = -8-2-2.5
            pin_length = 8.5
        else:
            large_corr=0
            pin_length = 16.5

        # in total four junctions
        junc_para = {}
        # 3 left junction, 4 right junction
        junc_para['junction1_length'] = junc_correction['1_junc']
        junc_para['junction2_length'] = junc_correction['2_junc']
        junc_para['junction3_length'] = junc_correction['3_junc']
        junc_para['junction4_length'] = junc_correction['4_junc']

        junc_para['junction1_gap'] = junc_correction['1_gap']
        junc_para['junction2_gap'] = junc_correction['2_gap']
        junc_para['junction3_gap'] = junc_correction['3_gap']
        junc_para['junction4_gap'] = junc_correction['4_gap']

        junc_para['junction5_length'] = junc_correction['5_junc']
        junc_para['junction6_length'] = junc_correction['6_junc']
        junc_para['junction7_length'] = junc_correction['7_junc']
        junc_para['junction8_length'] = junc_correction['8_junc']

        junc_para['junction5_gap'] = junc_correction['5_gap']
        junc_para['junction6_gap'] = junc_correction['6_gap']
        junc_para['junction7_gap'] = junc_correction['7_gap']
        junc_para['junction8_gap'] = junc_correction['8_gap']

        junc_para['junction_linear'] = 3
        junc_para['junction_linear_large'] = 2

        junc_para['gap_protect'] = 0.2
        junc_para['junc_arm'] = 0.5

        # define loop parameter
        loop = {}

        loop['pinw'] = 2
        loop['arm'] = 2
        loop['y'] = 10
        loop['x'] = 12
        loop['pinl'] = 13

        # draw test part

        xlist = [3577.479, 3577.479+6000]
        ylist = [1100, 1100]
        draw_test_frame(structure, xlist[0], ylist[0], junc_para, loop)
        draw_junction_small(structure, xlist[0]+1.5, ylist[0], junc_para, loop, 3, -1)
        draw_test_frame(structure, xlist[1], ylist[1], junc_para, loop)
        draw_junction_small(structure, xlist[1]+1.5, ylist[1], junc_para, loop, 4, -1)



def draw_test_structure(structure, d, junc_correction, flux_bias):
    c = structure
    ## alignment boxes for e-beam
    if (draw_layer1 == True) and (draw_layer2 == False):
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_square_alignment_marks(c)
    else:
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_square_alignment_marks(c)
    ## Junction parameters
    junc_length = junc_correction['s_length']
    junc_gap = junc_correction['s_gap']
    large_length = junc_correction['l_length']
    large_gap = junc_correction['l_gap']
    length_step = junc_correction['length_step']
    length_step_large = junc_correction['length_step_large']

    xpos = (c.s1.last[0] + c.s5.last[0]) / 2.
    ypos = (c.s3.last[1] + c.s8.last[1]) / 2.
    # Draw VSLQ test structure
    ylist = [1200 - 40, 2650 - 40, 4100 - 40, 5540 - 40]
    xlist = [770, 1340, 1910, 2480, 3050, 3620, 4190, 4760, 5330, 5900]
    if draw_layer1 == True:

        for i in range(len(xlist)):
            for j in range(len(ylist)):
                Draw_VSLQ_startest(c, xlist[i], ylist[j])
    if draw_layer2 == True:
        # in total four junctions
        junc_para = {}

        junc_para['junction_linear'] = 3
        junc_para['junction_linear_large'] = 2

        junc_para['gap_protect'] = 0.2
        junc_para['junc_arm'] = 0.5

        # define loop parameter
        loop = {}
        loop['x'] = 15
        loop['y'] = 15
        # position of the SQUID junctions (ratio)
        loop['position'] = 0.5
        loop['arm'] = 2

        # draw test part
        for i in range(len(xlist)):
            junc_para['junction1_length'] = large_length + i * length_step_large
            junc_para['junction3_length'] = junc_length + i * length_step

            junc_para['junction1_gap'] = large_gap
            junc_para['junction3_gap'] = junc_gap
            if i < len(xlist) - 1:
                ff = -1
            else:
                ff = 1
            draw_test_frame(structure, xlist[i], ylist[0], junc_para, loop)
            draw_junction_small(structure, xlist[i], ylist[0], junc_para, loop, 3, ff)
            draw_test_frame(structure, xlist[i], ylist[1], junc_para, loop)
            draw_junction_small(structure, xlist[i], ylist[1], junc_para, loop, 3, ff)
            draw_test_frame(structure, xlist[i], ylist[2], junc_para, loop)
            draw_junction_small(structure, xlist[i], ylist[2], junc_para, loop, 3, ff)
            draw_test_frame(structure, xlist[i], ylist[3], junc_para, loop)
            draw_junction_large(structure, xlist[i], ylist[3], junc_para, loop, 1, ff)



def draw_large_junction_test(structure, d, junc_correction):
    c = structure
    ## alignment boxes for e-beam
    if (draw_layer1 == True) and (draw_layer2 == False):
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_square_alignment_marks(c)
    else:
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_launchers(c, d, exclude=[2, 4, 8])
        draw_square_alignment_marks(c)
    ## Junction parameters
    junc_length = junc_correction['s_length']
    junc_gap = junc_correction['s_gap']
    large_length = junc_correction['l_length']
    large_gap = junc_correction['l_gap']
    length_step = junc_correction['length_step']
    length_step_large = junc_correction['length_step_large']

    xpos = (c.s1.last[0] + c.s5.last[0]) / 2.
    ypos = (c.s3.last[1] + c.s8.last[1]) / 2.
    # Draw VSLQ test structure
    ylist = [1500, 3400, 5300]
    xlist = [770, 1910, 3050, 4190,  5330]
    if draw_layer1 == True:

        for i in range(len(xlist)):
            for j in range(len(ylist)):
                Draw_test_large(c, xlist[i], ylist[j])
    if draw_layer2 == True:
        # in total four junctions
        junc_para = {}

        junc_para['junction_linear'] = 3
        junc_para['junction_linear_large'] = 2

        junc_para['gap_protect'] = 0.2
        junc_para['junc_arm'] = 0.5

        # define loop parameter
        loop = {}
        loop['x'] = 15
        loop['y'] = 15
        # position of the SQUID junctions (ratio)
        loop['position'] = 0.5
        loop['arm'] = 2

        # draw test part
        single = [-300, -200, -100, 100, 200, 300, 0]
        for i in range(len(xlist)):
            junc_para['junction1_length'] = large_length + i * length_step_large
            junc_para['junction3_length'] = junc_length + i * length_step

            junc_para['junction1_gap'] = large_gap
            junc_para['junction3_gap'] = junc_gap
            if i < len(xlist) - 1:
                ff = -1
            else:
                ff = 1
            for j in range(len(ylist)):
                for k in single:
                    draw_test_frame(structure, xlist[i]+k, ylist[j], junc_para, loop)
                    draw_junction_large(structure, xlist[i]+k, ylist[j], junc_para, loop, 1, ff)


def output_wafer():
    # Meant for writing junctions on a wafer with metallic base layer

    m = WaferMask(MaskName, diameter=70800., flat_angle=270., flat_distance=24100., wafer_padding=2500,
                  chip_size=(12800, 1800),
                  dicing_border=400, etchtype=False, wafer_edge=False,
                  dashed_dicing_border=50, ndashes=0, dice_corner=True, square_arr=True)

    # 4in wafer -> diameter=101600, flat_distance=48200
    # 3in wafer -> diameter=76200., flat_distance=37100.
    # 2in wafer -> diameter=50800., flat_distance=24100.

    points = [(-24000., -4000.), (-24000., 4000.), (24000., -4000.), (24000., 4000.)]
    points_medium = [(-24000. + 1200, -4000.), (-24000. + 1200, 4000.), (24000. - 1200, -4000.), (24000. - 1200, 4000.)]
    points_small = [(-24000. + 2000, -4000.), (-24000. + 2000, 4000.), (24000. - 2000, -4000.), (24000. - 2000, 4000.)]

    # Create the alignment crosses on the wafer. NOTE: currently only works for solid = True setting.
    # Something goes wrong with the layers cause that's built in otherwise. Hacky solution:
    if solid:
        if draw_layer1 == 2:
            AlignmentCross(m, linewidth=50, size=(1000, 1000), solid=solid, points=points, layer=None, name='cross')
            AlignmentCross(m, linewidth=25, size=(200, 200), solid=solid, points=points_medium, layer=None,
                           name='cross_medium')
            AlignmentCross(m, linewidth=5, size=(20, 20), solid=solid, points=points_small, layer=None,
                           name='cross_small')


    else:
        if draw_layer1 == 2:
            AlignmentCross(m, linewidth=50, size=(1000, 1000), solid=False, points=points, layer='0', name='cross')
            AlignmentCross(m, linewidth=25, size=(200, 200), solid=False, points=points_medium, layer='0',
                           name='cross_medium')
            AlignmentCross(m, linewidth=5, size=(20, 20), solid=False, points=points_small, layer='0',
                           name='cross_small')

    d = set_mask_init()

    # --------------------------#

    junc_correction = {'1_junc': 7.0, '1_gap': 0.14, '2_junc': 7.0, '2_gap': 0.14,
                       '3_junc': 0.35, '3_gap': 0.17, '4_junc': 0.32, '4_gap': 0.17, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':1, 'QQ_move':0}  ## (1 top, 2 middle, 3 left, 4 right)
    CHIPNAME = 'VSTA7A'
    flux_bias = False
    c0 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c0, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.2, '1_gap': 0.14, '2_junc': 7.2, '2_gap': 0.14,
                       '3_junc': 0.35, '3_gap': 0.18, '4_junc': 0.32, '4_gap': 0.18, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':2, 'QQ_move':0 }  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    CHIPNAME = 'VSTA7B'
    c1 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c1, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.9, '1_gap': 0.14, '2_junc': 6.9, '2_gap': 0.14,
                       '3_junc': 0.35, '3_gap': 0.19, '4_junc': 0.32, '4_gap': 0.19, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':3, 'QQ_move':0}  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    SIPF_correction = 8200
    CHIPNAME = 'VSTA7C'
    c2 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    # draw_bridge_junction(c2, d, junc_correction)
    draw_bridge_junction(c2, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.6, '1_gap': 0.14, '2_junc': 6.6, '2_gap': 0.14,
                       '3_junc': 0.32, '3_gap': 0.17, '4_junc': 0.29, '4_gap': 0.17, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':3, 'QQ_move':0}  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    CHIPNAME = 'VSTA7D'
    c3 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c3, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.3, '1_gap': 0.14, '2_junc': 6.3, '2_gap': 0.14,
                       '3_junc': 0.32, '3_gap': 0.18, '4_junc': 0.29, '4_gap': 0.18, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':4, 'QQ_move':0}  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    CHIPNAME = 'VSTA7E'
    c4 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c4, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.2, '1_gap': 0.14, '2_junc': 7.2, '2_gap': 0.14,
                       '3_junc': 0.32, '3_gap': 0.19, '4_junc': 0.29, '4_gap': 0.19, '5_junc': 0.145, '5_gap': 0.24,
                       '6_junc': 0.135, '6_gap': 0.24, '7_junc': 0.135, '7_gap': 0.24, '8_junc': 0.125,
                       '8_gap': 0.24, 'large_move':0, 'QQ_move':10}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7F'
    c5 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c5, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.0, '1_gap': 0.14, '2_junc': 7.0, '2_gap': 0.14,
                       '3_junc': 0.29, '3_gap': 0.17, '4_junc': 0.26, '4_gap': 0.17, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move': 1, 'QQ_move': 0}  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    CHIPNAME = 'VSTA7G'
    c6 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c6, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.8, '1_gap': 0.14, '2_junc': 6.8, '2_gap': 0.14,
                       '3_junc': 0.29, '3_gap': 0.18, '4_junc': 0.26, '4_gap': 0.18, '5_junc': 0.12, '5_gap': 0.22,
                       '6_junc': 0.11, '6_gap': 0.22, '7_junc': 0.11, '7_gap': 0.22, '8_junc': 0.1,
                       '8_gap': 0.22, 'large_move':0, 'QQ_move':10}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7H'
    c7 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c7, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.0, '1_gap': 0.14, '2_junc': 7.0, '2_gap': 0.14,
                       '3_junc': 0.29, '3_gap': 0.19, '4_junc': 0.26, '4_gap': 0.19, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move': 1, 'QQ_move': 0}  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    CHIPNAME = 'VSTA7I'
    c8 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c8, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.4, '1_gap': 0.14, '2_junc': 6.4, '2_gap': 0.14,
                       '3_junc': 0.26, '3_gap': 0.17, '4_junc': 0.24, '4_gap': 0.17, '5_junc': 0.12, '5_gap': 0.22,
                       '6_junc': 0.11, '6_gap': 0.22, '7_junc': 0.11, '7_gap': 0.22, '8_junc': 0.1,
                       '8_gap': 0.22, 'large_move':0, 'QQ_move':10}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7J'
    c9 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c9, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.5, '1_gap': 0.15, '2_junc': 7.5, '2_gap': 0.15,
                       '3_junc': 0.26, '3_gap': 0.18, '4_junc': 0.24, '4_gap': 0.18, '5_junc': 0.12, '5_gap': 0.22,
                       '6_junc': 0.11, '6_gap': 0.22, '7_junc': 0.11, '7_gap': 0.22, '8_junc': 0.1,
                       '8_gap': 0.22, 'large_move':1, 'QQ_move':-5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7K'
    SIPF_correction = 8100
    c10 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c10, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.2, '1_gap': 0.15, '2_junc': 7.2, '2_gap': 0.15,
                       '3_junc': 0.26, '3_gap': 0.19, '4_junc': 0.24, '4_gap': 0.19, '5_junc': 0.12, '5_gap': 0.24,
                       '6_junc': 0.11, '6_gap': 0.24, '7_junc': 0.11, '7_gap': 0.24, '8_junc': 0.1,
                       '8_gap': 0.24, 'large_move':2, 'QQ_move':-5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7L'
    c11 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c11, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.9, '1_gap': 0.15, '2_junc': 6.9, '2_gap': 0.15,
                       '3_junc': 0.23, '3_gap': 0.17, '4_junc': 0.21, '4_gap': 0.17, '5_junc': 0.12, '5_gap': 0.24,
                       '6_junc': 0.11, '6_gap': 0.24, '7_junc': 0.11, '7_gap': 0.24, '8_junc': 0.1,
                       '8_gap': 0.24, 'large_move':3, 'QQ_move':-5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7M'
    c12 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c12, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.6, '1_gap': 0.15, '2_junc': 6.6, '2_gap': 0.15,
                       '3_junc': 0.23, '3_gap': 0.18, '4_junc': 0.21, '4_gap': 0.18, '5_junc': 0.12, '5_gap': 0.24,
                       '6_junc': 0.11, '6_gap': 0.24, '7_junc': 0.11, '7_gap': 0.24, '8_junc': 0.1,
                       '8_gap': 0.24, 'large_move':3, 'QQ_move':-5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7N'
    c13 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c13, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.3, '1_gap': 0.15, '2_junc': 6.3, '2_gap': 0.15,
                       '3_junc': 0.23, '3_gap': 0.19, '4_junc': 0.21, '4_gap': 0.19, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':4, 'QQ_move':-5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7O'
    SIPF_correction = 8300
    c14 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c14, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.2, '1_gap': 0.16, '2_junc': 7.2, '2_gap': 0.16,
                       '3_junc': 0.2, '3_gap': 0.17, '4_junc': 0.18, '4_gap': 0.17, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':0, 'QQ_move':-10}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7P'
    c15 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c15, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.0, '1_gap': 0.14, '2_junc': 7.0, '2_gap': 0.14,
                       '3_junc': 0.2, '3_gap': 0.18, '4_junc': 0.18, '4_gap': 0.18, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move': 1, 'QQ_move': 0}  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    CHIPNAME = 'VSTA7Q'
    c16 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c16, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.8, '1_gap': 0.16, '2_junc': 6.8, '2_gap': 0.16,
                       '3_junc': 0.2, '3_gap': 0.19, '4_junc': 0.18, '4_gap': 0.19, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move':0, 'QQ_move':-10}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7R'
    c17 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c17, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.0, '1_gap': 0.14, '2_junc': 7.0, '2_gap': 0.14,
                       '3_junc': 0.17, '3_gap': 0.17, '4_junc': 0.15, '4_gap': 0.17, '5_junc': 0.11, '5_gap': 0.22,
                       '6_junc': 0.10, '6_gap': 0.22, '7_junc': 0.10, '7_gap': 0.22, '8_junc': 0.095,
                       '8_gap': 0.22, 'large_move': 1, 'QQ_move': 0}  ## (1 top, 2 middle, 3 left, 4 right)
    flux_bias = False
    CHIPNAME = 'VSTA7S'
    c18 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c18, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.4, '1_gap': 0.16, '2_junc': 6.4, '2_gap': 0.16,
                       '3_junc': 0.17, '3_gap': 0.18, '4_junc': 0.15, '4_gap': 0.18, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move':0, 'QQ_move':-10}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7T'
    c19 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c19, d, junc_correction, flux_bias)

    # --------------------------#

    junc_correction = {'1_junc': 7.5, '1_gap': 0.16, '2_junc': 7.5, '2_gap': 0.16,
                       '3_junc': 0.17, '3_gap': 0.19, '4_junc': 0.15, '4_gap': 0.19, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move':1, 'QQ_move':5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7U'
    c20 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c20, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 7.2, '1_gap': 0.16, '2_junc': 7.2, '2_gap': 0.16,
                       '3_junc': 0.14, '3_gap': 0.17, '4_junc': 0.12, '4_gap': 0.17, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move':2, 'QQ_move':5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7V'
    c21 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c21, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.9, '1_gap': 0.16, '2_junc': 6.9, '2_gap': 0.16,
                       '3_junc': 0.14, '3_gap': 0.18, '4_junc': 0.12, '4_gap': 0.18, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move':3, 'QQ_move':5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7W'
    SIPF_correction = 8150
    c22 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c22, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.6, '1_gap': 0.16, '2_junc': 6.6, '2_gap': 0.16,
                       '3_junc': 0.14, '3_gap': 0.19, '4_junc': 0.12, '4_gap': 0.19, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move':3, 'QQ_move':5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7X'
    c23 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c23, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.3, '1_gap': 0.16, '2_junc': 6.3, '2_gap': 0.16,
                       '3_junc': 0.11, '3_gap': 0.17, '4_junc': 0.1, '4_gap': 0.17, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move':4, 'QQ_move':5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7Y'
    c24 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c24, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.3, '1_gap': 0.16, '2_junc': 6.3, '2_gap': 0.16,
                       '3_junc': 0.11, '3_gap': 0.18, '4_junc': 0.1, '4_gap': 0.18, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move': 4,
                       'QQ_move': 5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA7Z'
    c25 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c25, d, junc_correction, flux_bias)

    # --------------------------#
    junc_correction = {'1_junc': 6.3, '1_gap': 0.16, '2_junc': 6.3, '2_gap': 0.16,
                       '3_junc': 0.11, '3_gap': 0.19, '4_junc': 0.1, '4_gap': 0.19, '5_junc': 0.11, '5_gap': 0.24,
                       '6_junc': 0.10, '6_gap': 0.24, '7_junc': 0.10, '7_gap': 0.24, '8_junc': 0.095,
                       '8_gap': 0.24, 'large_move': 4,
                       'QQ_move': 5}  ## (1 large1, 2 large2, 3 Q1, 4 Q2, 5 QR11, 6 QR12, 7 QR21, 8 QR22)
    flux_bias = False
    CHIPNAME = 'VSTA8A'
    c26= Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    draw_bridge_junction(c26, d, junc_correction, flux_bias)

    # --------------------------#
    junc_l = 4.9
    CHIPNAME = '4900'
    c27 = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
               chip_id_loc=(200, 100), textsize=(70, 70), two_layer=two_layer, solid=solid)
    cap_top_x = 5
    draw_on_chip(c27, d, junc_l, cap_top_x)

    ### ===================== ###
    # Last row: JPA transformers
    ### --------------------- ###
    #####################################
    global sign
    global draw_len
    # common features for eps = 10.4, 7 GHz transformers
    cpw_rad1 = 400
    cpw_rad2 = 1.0 * cpw_rad1

    cpw_pinw = 10.0
    eps_eff = (1. + 10.4) / 2.
    cpw_gapw = calculate_gap_width(eps_eff, 50, cpw_pinw)
    cpw_pinw1 = 54.2
    cpw_gapw1 = 10.2
    cpw_pinw2 = 10.0
    cpw_gapw2 = 10.2
    max_len = 3200
    lambda2_len = 9000
    lambda4_len = 4500

    # --------------------------------#
    # 7GHz, eps = 10.4
    junc_l = 2.1
    CHIPNAME = 'ZQL'
    ct = Chip(CHIPNAME, author=author, size=m.chip_size, mask_id_loc=(5800, 6430),
              chip_id_loc=(300, 100), textsize=(70, 70), two_layer=two_layer, solid=solid, layer='0')
    # draw_launchers(ct, d, exclude=[0, 1, 2, 4, 5, 6, 7, 9])
    # draw_square_alignment_marks(ct, d)
    #
    # draw_test_full_transformer(ct, cpw_pinw, cpw_gapw, cpw_pinw1, cpw_pinw2, cpw_gapw1, cpw_gapw2, cpw_rad1, cpw_rad2,
    #                       lambda4_len, lambda2_len, max_len)
    # --------------------------------#

    if draw_layer1 == 0 and draw_layer2 == 1:
        label = False
    else:
        label = True

    # m.add_chip(ct, 5, label=label)
    m.add_chip(c0, 1, label=label)
    # m.add_chip(c1, 1, label=label)
    # m.add_chip(c2, 1, label=label)
    # m.add_chip(c3, 1, label=label)
    # m.add_chip(c4, 1, label=label)
    # m.add_chip(c5, 1, label=label)
    # m.add_chip(c6, 1, label=label)
    # m.add_chip(c7, 1, label=label)
    # m.add_chip(c8, 1, label=label)
    # m.add_chip(c9, 1, label=label)
    # m.add_chip(c10, 1, label=label)
    # m.add_chip(c11, 1, label=label)
    # m.add_chip(c12, 1, label=label)
    # m.add_chip(c13, 1, label=label)
    # m.add_chip(c14, 1, label=label)
    # m.add_chip(c15, 1, label=label)
    # m.add_chip(c16, 1, label=label)
    # m.add_chip(c17, 1, label=label)
    # m.add_chip(c18, 1, label=label)
    # m.add_chip(c19, 1, label=label)
    # m.add_chip(c20, 1, label=label)
    # m.add_chip(c21, 1, label=label)
    # m.add_chip(c22, 1, label=label)
    # m.add_chip(c23, 1, label=label)
    # m.add_chip(c24, 1, label=label)
    # m.add_chip(c25, 1, label=label)
    # m.add_chip(c26, 1, label=label)
    # m.add_chip(c27, 1, label=label)

    return m


if __name__ == "__main__":

    m = output_wafer()
    m.save()

    print("\n\n Chip names are:")
    print("_____________________")
    for name in chip_names:
        print(name)
    print("_____________________\n\n")

    sleep(.1)

    # if show_structure:
    #     if open_dwgviewer:
    #         subprocess.Popen(
    #             r'"C:\Program Files\Autodesk\DWG TrueView 2019 - English\dwgviewr.exe" "' + os.getcwd() + '\\' + MaskName + '-' + '6000' + '.dxf" ')
    #     if open_klayout:
    #         subprocess.Popen(
    #             r'"C:\Users\slab\AppData\Roaming\KLayout\klayout_app.exe" "' + os.getcwd() + '\\' + MaskName + '-' + '6000' + '.dxf" -e')  # editor mode
    # elif show_wafer:
    #     if open_dwgviewer:
    #         subprocess.Popen(
    #             r'"C:\Program Files\Autodesk\DWG TrueView 2019 - English\dwgviewr.exe" "' + os.getcwd() + '\\' + MaskName + '.dxf" ')
    #     if open_klayout:
    #         subprocess.Popen(
    #             r'"C:\Users\slab\AppData\Roaming\KLayout\klayout_app.exe" "' + os.getcwd() + '\\' + MaskName + '.dxf" -e')

    try:
        # save a text file with the dimensions
        text = "Specs for %s created at %s at %s\n\nTapered: \t\t%s\nTotal length: \t\t%s um\nTotal width: \t\t%s um\nFinger length: \t\t%s um\nFinger width: \t\t%s um\nFinger separation: \t%s um\nNumber of fingers: \t%s\nTaper length: \t\t%s um\nCPW length: \t\t%s um\nCPW center pin: \t%s um\nCPW gap width: \t\t%s um" \
               % (MaskName + '-' + c.name, today, time.strftime("%H:%M:%S"), str(taper), c.total_size, c.total_width,
                  finger_length, finger_width, finger_spacing, noof_fingers, taper_length, cpw_length, cpw_pinw,
                  cpw_pinw)

        text_file = open(MaskName + '-' + c.name + '-specs.txt', "w")
        text_file.write(text)
        text_file.close()

        print("\nFinished creating capacitor with following parameters:")
        print(text)
    except:
        pass