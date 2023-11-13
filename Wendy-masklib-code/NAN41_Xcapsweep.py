#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:29:41 2021

@author: sasha

Generating file for wafer including:
    - 6 xmon chip with lambda/4 resonators
    - etch test chips with junction area arrays

Goal: Recreate results from most successful chip (28P I1)
"""

import maskLib.MaskLib as m
from maskLib.dcLib import Rbar
from maskLib.microwaveLib import *
from maskLib.Entities import SolidPline, SkewRect, CurveRect, InsideCurve
import numpy as np
from dxfwrite import DXFEngine as dxf
from dxfwrite import const
from dxfwrite.entities import *
from dxfwrite.vector2d import vadd

from maskLib.utilities import doMirrored
from maskLib.markerLib import MarkerSquare, MarkerCross
from maskLib.resonatorLib import JellyfishResonator

from maskLib.dcLib import ResistanceBar, ResistanceBarBilayer, ResistanceBarNegative

#from maskLib.resonatorLib import JellyfishResonator,CingularResonator
#from maskLib.qubitLib import Xmon

# ===============================================================================
# wafer setup
# ===============================================================================

w = m.Wafer('NAN41_XCapSweep_v1','DXF/',7000,7000,padding=500,waferDiameter=55000,sawWidth=200,#m.sawL_ws['8A'],
                frame=1,solid=0,multiLayer=1)
#set wafer properties
# w.frame: draw frame layer?
# w.solid: draw things solid?
# w.multiLayer: draw in multiple layers?

w.SetupLayers([
    ['BASEMETAL',4],
    ['BUSMAIN',3],
    ['XOR',1],
    ['XOR2',3],
    ['SECONDLAYER',6],
    ['MARKERS',2],
    ['LYR1',7],#target for XOR operations
    ['LYR2',3], #target for XOR operations
    ['EBEAM',2]
    ])


#initialize the wafer
w.init()

#do dicing border
w.DicingBorder()
    
curve_pts = 30  #point resolution of all curves
    
def overlap_junction_bilayer(chip,structure,length=300,pad=300,gap=20,width=80,jsep=16,taperl=4,fingerw=1,finger2w=None,leadw=None,offset=5,overlap=7,cdbias=0.0,secondlayer='SECONDLAYER'):
    def struct():
        if isinstance(structure,m.Structure):
            return structure
        elif isinstance(structure,tuple):
            return m.Structure(chip,structure)
        else:
            return chip.structure(structure)
        
    if leadw is None:
        leadw=fingerw
    if finger2w is None:
        finger2w=fingerw
    struct().shiftPos(-length/2-pad-gap)
    struct().defaults['w']=pad
    struct().defaults['s']=gap
    struct().defaults['r_out']=gap
    
    CPW_stub_open(chip,struct(),flipped=True)
    CPW_straight(chip,struct(),pad)
    CPW_stub_short(chip,struct(),flipped=False,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
    CPW_straight(chip,struct(), length/2-gap-jsep, w=width)
    CPW_taper(chip,struct(),taperl,s1=gap+width/2-fingerw/2,w1=fingerw,w0=width,offset=(0,offset/2))
    CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    #overlap part
    chip.add(dxf.rectangle(struct().getPos((-overlap/2,-offset+leadw/2)),finger2w,offset-leadw/2-fingerw/2,rotation=struct().direction,layer=secondlayer))
    chip.add(dxf.rectangle(struct().getPos((-overlap/2-cdbias,-fingerw/2)),finger2w+2*cdbias,fingerw,rotation=struct().direction,layer=secondlayer))
    chip.add(dxf.rectangle(struct().getPos((-overlap/2,fingerw/2)),finger2w,overlap-(offset-leadw/2-fingerw/2),rotation=struct().direction,layer=secondlayer))
    struct().translatePos((0,-offset))
    sl2 = struct().cloneAlong((-overlap/2,0))
    Strip_straight(chip,sl2, jsep/2-taperl+overlap/2, w=leadw,layer=secondlayer)
    Strip_taper(chip,sl2,taperl,w0=leadw,w1=width,layer=secondlayer)
    Strip_straight(chip,sl2,length/2-jsep,w=width,layer=secondlayer)
    Strip_straight(chip,sl2,pad,w=pad,layer=secondlayer)
    
    Strip_straight(chip,struct(), length/2-gap-jsep/2, w=width+2*gap)
    Strip_stub_open(chip,struct(),flipped=True,w=pad+2*gap)
    Strip_straight(chip,struct(),pad,w=pad+2*gap)
    Strip_stub_open(chip,struct(),w=pad+2*gap)

def quasidolan_junction_bilayer(chip,structure,length=300,pad=300,gap=20,width=80,jsep=16,taperl=4,fingerw=8,leadw=None,overlap=0.8):
    def struct():
        if isinstance(structure,m.Structure):
            return structure
        elif isinstance(structure,tuple):
            return m.Structure(chip,structure)
        else:
            return chip.structure(structure)
        
    if leadw is None:
        leadw=fingerw
    struct().shiftPos(-length/2-pad-gap)
    struct().defaults['w']=pad
    struct().defaults['s']=gap
    struct().defaults['r_out']=gap
    
    CPW_stub_open(chip,struct(),flipped=True)
    CPW_straight(chip,struct(),pad)
    CPW_stub_short(chip,struct(),flipped=False,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
    CPW_straight(chip,struct(), length/2-gap-jsep, w=width)
    CPW_taper(chip,struct(),taperl,s1=gap+width/2-fingerw/2,w1=fingerw,w0=width)
    CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    #struct().translatePos((0,-offset))
    sl2 = struct().cloneAlong((-overlap,-fingerw/2-leadw/2+overlap))
    Strip_straight(chip,sl2, jsep/2-taperl+overlap, w=leadw,layer='SECONDLAYER')
    Strip_taper(chip,sl2,taperl,w0=leadw,w1=width,layer='SECONDLAYER',offset=(0,fingerw/2+leadw/2-overlap))
    Strip_straight(chip,sl2,length/2-jsep,w=width,layer='SECONDLAYER')
    Strip_straight(chip,sl2,pad,w=pad,layer='SECONDLAYER')
    
    Strip_straight(chip,struct(), length/2-gap-jsep/2, w=width+2*gap)
    Strip_stub_open(chip,struct(),flipped=True,w=pad+2*gap)
    Strip_straight(chip,struct(),pad,w=pad+2*gap)
    Strip_stub_open(chip,struct(),w=pad+2*gap)
    
def overlap_junction_dolan(chip,structure,length=300,pad=300,gap=20,width=80,jsep=16,taperl=4,fingerw=1,finger2w=None,leadw=None,leadw2=None,overlap=7,cdbias=0.0,secondlayer='SECONDLAYER',eBeam=True):
    def struct():
        if isinstance(structure,m.Structure):
            return structure
        elif isinstance(structure,tuple):
            return m.Structure(chip,structure)
        else:
            return chip.structure(structure)
        
    if leadw is None:
        leadw=fingerw
    if finger2w is None:
        finger2w=fingerw
    if leadw2 is None:
        leadw2=leadw
    struct().shiftPos(-length/2-pad-gap)
    struct().defaults['w']=pad
    struct().defaults['s']=gap
    struct().defaults['r_out']=gap
    
    CPW_stub_open(chip,struct(),flipped=True)
    CPW_straight(chip,struct(),pad)
    CPW_stub_short(chip,struct(),flipped=False,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
    CPW_straight(chip,struct(), length/2-gap-jsep, w=width)
    CPW_taper(chip,struct(),taperl,s1=gap+width/2-fingerw/2,w1=leadw2,w0=width)
    CPW_straight(chip,struct(),jsep/2-taperl+finger2w/2,w=leadw2,s=gap+width/2-leadw2/2)
    if eBeam:
        #ebeam part
        struct().shiftPos(-overlap*0.6 -finger2w/2)
        CPW_straight(chip,struct(),overlap*1.2,w=fingerw,s=leadw-fingerw/2,layer='EBEAM')
        struct().shiftPos(-overlap*0.6 + finger2w/2)
        #continue
    #overlap part
    sl2 = struct().cloneAlong((-finger2w,0))
    if not eBeam:
        leadw=fingerw
    Strip_straight(chip,sl2, jsep/2-taperl+finger2w/2, w=leadw,layer=secondlayer)
    Strip_taper(chip,sl2,taperl,w0=leadw,w1=width,layer=secondlayer)
    Strip_straight(chip,sl2,length/2-jsep,w=width,layer=secondlayer)
    Strip_straight(chip,sl2,pad,w=pad,layer=secondlayer)
    
    Strip_straight(chip,struct(), length/2-gap-jsep/2, w=width+2*gap)
    Strip_stub_open(chip,struct(),flipped=True,w=pad+2*gap)
    Strip_straight(chip,struct(),pad,w=pad+2*gap)
    Strip_stub_open(chip,struct(),w=pad+2*gap)


def XmonTrilayer(chip,structure,length,r_qubit=None,w_qubit=None,s_qubit=None,
         jsep=None,taper_l=4,fingerw=1,finger2w=None,leadw=None,leadw2=None,joverlap=8,joverlap2=None,cdbias=0.0,secondlayer='SECONDLAYER'):
    def struct():
        if isinstance(structure,m.Structure):
            return structure
        elif isinstance(structure,tuple):
            return m.Structure(chip,structure)
        else:
            return chip.structure(structure)
    if w_qubit is None:
        try:
            w_qubit = struct().defaults['w']
        except KeyError:
            print('\x1b[33ms not defined in ',chip.chipID,'!\x1b[0m')
    if s_qubit is None:
        try:
            s_qubit = struct().defaults['s']
        except KeyError:
            print('\x1b[33ms not defined in ',chip.chipID,'!\x1b[0m')
    if r_qubit is None:
        try:
            r_qubit = struct().defaults['r_ins']
        except KeyError:
            print('\x1b[33mr_ins not defined in ',chip.chipID,'!\x1b[0m')
            r_qubit=0
    #allow customizeable lengths which fall back to defaults
    if leadw is None:
        leadw=fingerw
    if leadw2 is None:
        leadw2=leadw
    if finger2w is None:
        finger2w=fingerw
    if jsep is None:
        jsep = s_qubit/2
    if joverlap2 is None:
        joverlap2 = joverlap
    #since length is the length of each arm,
    #define q_height as length from end to end of qubit ground plane slot
    q_height=length*2+s_qubit*2
        
    chip.add(RoundRect(struct().start,q_height-s_qubit-r_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[1,0,0,1],rotation=struct().direction,valign=const.MIDDLE),struct(),q_height-s_qubit-r_qubit)
    #left and right arms
    sr=struct().cloneAlongLast((q_height/2,w_qubit/2+s_qubit),newDirection=90)
    sl=struct().cloneAlongLast((q_height/2,-w_qubit/2-s_qubit),newDirection=-90)
    
    Strip_stub_short(chip,sr,r_ins=r_qubit,w=w_qubit+2*s_qubit,flipped=True)
    Strip_stub_short(chip,sl,r_ins=r_qubit,w=w_qubit+2*s_qubit,flipped=True)
    chip.add(RoundRect(sr.start,q_height/2-w_qubit/2-s_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[0,1,1,0],rotation=sr.direction,valign=const.MIDDLE))
    chip.add(RoundRect(sl.start,q_height/2-w_qubit/2-s_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[0,1,1,0],rotation=sl.direction,valign=const.MIDDLE))
    sr.shiftPos(-s_qubit)
    sl.shiftPos(-s_qubit)
    #second layer
    Strip_stub_short(chip,sr,r_ins=r_qubit+s_qubit,w=w_qubit,flipped=True,layer=secondlayer)
    Strip_stub_short(chip,sl,r_ins=r_qubit+s_qubit,w=w_qubit,flipped=True,layer=secondlayer)
    chip.add(RoundRect(sr.start,q_height/2-w_qubit/2-s_qubit, w_qubit, r_qubit,roundCorners=[0,1,1,0],rotation=sr.direction,valign=const.MIDDLE,layer=secondlayer))
    chip.add(RoundRect(sl.start,q_height/2-w_qubit/2-s_qubit, w_qubit, r_qubit,roundCorners=[0,1,1,0],rotation=sl.direction,valign=const.MIDDLE,layer=secondlayer))
    
    
    
    CPW_stub_short(chip, struct(),curve_ins=False,r_out=r_qubit+s_qubit,r_ins=0,w=leadw,s=s_qubit+w_qubit/2-leadw/2)
    struct().shiftPos(-s_qubit-r_qubit)
    Strip_straight(chip, struct(), jsep-joverlap/2+r_qubit,w=leadw)
    CPW_straight(chip, struct(), joverlap, w=fingerw,s=leadw/2-fingerw/2)
    CPW_taper(chip, struct(), taper_l,w0=fingerw,s0=leadw/2-fingerw/2,w1=leadw,s1=0)
    struct().shiftPos(-taper_l-joverlap/2,angle=180)
    chip.add(dxf.rectangle(struct().getPos((0,-fingerw/2)), finger2w, (joverlap2-leadw2/2-fingerw)/2, valign=const.BOTTOM,halign=const.CENTER,rotation=struct().direction,bgcolor=chip.bg(secondlayer),layer=secondlayer))
    chip.add(dxf.rectangle(struct().start, finger2w+2*cdbias, fingerw, valign=const.MIDDLE,halign=const.CENTER,rotation=struct().direction,bgcolor=chip.bg(secondlayer),layer=secondlayer))
    chip.add(dxf.rectangle(struct().getPos((0,fingerw/2)), finger2w, (joverlap2-leadw2/2-fingerw)/2, valign=const.TOP,halign=const.CENTER,rotation=struct().direction,bgcolor=chip.bg(secondlayer),layer=secondlayer))
    chip.add(dxf.rectangle(struct().getPos((-finger2w/2,joverlap2/2-leadw2/4)), jsep+finger2w/2, leadw2, rotation=struct().direction,bgcolor=chip.bg(secondlayer),layer=secondlayer),struct(),jsep)
    Strip_pad(chip, struct(), q_height-2*s_qubit, w=w_qubit, r_out=r_qubit,layer=secondlayer)
    
def XmonTrilayerDolan(chip,structure,length,r_qubit=None,w_qubit=None,s_qubit=None,
         jsep=None,taper_l=4,fingerw=1,finger2w=None,leadw=None,leadw2=None,joverlap=8,joverlap2=None,cdbias=0.0,secondlayer='SECONDLAYER',eBeam=True):
    def struct():
        if isinstance(structure,m.Structure):
            return structure
        elif isinstance(structure,tuple):
            return m.Structure(chip,structure)
        else:
            return chip.structure(structure)
    if w_qubit is None:
        try:
            w_qubit = struct().defaults['w']
        except KeyError:
            print('\x1b[33ms not defined in ',chip.chipID,'!\x1b[0m')
    if s_qubit is None:
        try:
            s_qubit = struct().defaults['s']
        except KeyError:
            print('\x1b[33ms not defined in ',chip.chipID,'!\x1b[0m')
    if r_qubit is None:
        try:
            r_qubit = struct().defaults['r_ins']
        except KeyError:
            print('\x1b[33mr_ins not defined in ',chip.chipID,'!\x1b[0m')
            r_qubit=0
    #allow customizeable lengths which fall back to defaults
    if leadw is None:
        leadw=fingerw
    if leadw2 is None:
        leadw2=leadw
    if finger2w is None:
        finger2w=fingerw
    if jsep is None:
        jsep = s_qubit/2
    if joverlap2 is None:
        joverlap2 = joverlap
    #since length is the length of each arm,
    #define q_height as length from end to end of qubit ground plane slot
    q_height=length*2+s_qubit*2
        
    chip.add(RoundRect(struct().start,q_height-s_qubit-r_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[1,0,0,1],rotation=struct().direction,valign=const.MIDDLE),struct(),q_height-s_qubit-r_qubit)
    #left and right arms
    sr=struct().cloneAlongLast((q_height/2,w_qubit/2+s_qubit),newDirection=90)
    sl=struct().cloneAlongLast((q_height/2,-w_qubit/2-s_qubit),newDirection=-90)
    
    Strip_stub_short(chip,sr,r_ins=r_qubit,w=w_qubit+2*s_qubit,flipped=True)
    Strip_stub_short(chip,sl,r_ins=r_qubit,w=w_qubit+2*s_qubit,flipped=True)
    chip.add(RoundRect(sr.start,q_height/2-w_qubit/2-s_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[0,1,1,0],rotation=sr.direction,valign=const.MIDDLE))
    chip.add(RoundRect(sl.start,q_height/2-w_qubit/2-s_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[0,1,1,0],rotation=sl.direction,valign=const.MIDDLE))
    sr.shiftPos(-s_qubit)
    sl.shiftPos(-s_qubit)
    #second layer
    Strip_stub_short(chip,sr,r_ins=r_qubit+s_qubit,w=w_qubit,flipped=True,layer=secondlayer)
    Strip_stub_short(chip,sl,r_ins=r_qubit+s_qubit,w=w_qubit,flipped=True,layer=secondlayer)
    chip.add(RoundRect(sr.start,q_height/2-w_qubit/2-s_qubit, w_qubit, r_qubit,roundCorners=[0,1,1,0],rotation=sr.direction,valign=const.MIDDLE,layer=secondlayer))
    chip.add(RoundRect(sl.start,q_height/2-w_qubit/2-s_qubit, w_qubit, r_qubit,roundCorners=[0,1,1,0],rotation=sl.direction,valign=const.MIDDLE,layer=secondlayer))
    
    
    
    CPW_stub_short(chip, struct(),curve_ins=False,r_out=r_qubit+s_qubit,r_ins=0,w=leadw,s=s_qubit+w_qubit/2-leadw/2)
    struct().shiftPos(-s_qubit-r_qubit)
    #switch leadw2 to be original leadw
    Strip_straight(chip, struct(), jsep+r_qubit,w=leadw)
    if eBeam:
        #ebeam part
        struct().shiftPos(-joverlap*0.6)
        CPW_straight(chip,struct(),joverlap*1.2,w=fingerw,s=leadw-fingerw/2,layer='EBEAM')
        struct().shiftPos(-joverlap*0.6)
        #continue
    CPW_straight(chip, struct(), joverlap/2, w=leadw2,s=leadw/2-leadw2/2)
    CPW_taper(chip, struct(), taper_l,w0=leadw2,s0=leadw/2-leadw2/2,w1=leadw,s1=0)
    struct().shiftPos(-taper_l-joverlap/2,angle=180)
    if eBeam:
        chip.add(dxf.rectangle(struct().getPos((-finger2w,0)), jsep+finger2w, leadw, valign=const.MIDDLE, rotation=struct().direction,bgcolor=chip.bg(secondlayer),layer=secondlayer),struct(),jsep)
    else:
        chip.add(dxf.rectangle(struct().getPos((-finger2w,0)), jsep+finger2w-taper_l, fingerw, valign=const.MIDDLE, rotation=struct().direction,bgcolor=chip.bg(secondlayer),layer=secondlayer),struct(),jsep-taper_l)
        Strip_taper(chip,struct(),taper_l,fingerw,leadw,layer=secondlayer)
    Strip_pad(chip, struct(), q_height-2*s_qubit, w=w_qubit, r_out=r_qubit,layer=secondlayer)
    



#=============================
class EtchTestChip(m.Chip7mm):
    def __init__(self,wafer,chipID,layer):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':20, 's':10, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        #optical markers
        doMirrored(MarkerCross, self, (2900,2900),linewidth=1, chipCentered=True,layer='MARKERS')
        
        for s in self.structures:
            s.shiftPos(340)
        
        #qubit parameters
        w_qubit = 200
        s_qubit = 16
        q_sep = 8
        q_height = 262#300
        q_overlap = 160
        r_qubit = 24
        #junction parameters
        leadw=10.0
        finger2w=0.7 #change this if 1st layer succeeds
        joverlap=6.0#8.0
        joverlap2=8.0
        taper_l = 4
        cdbias=0.0
        
        #junction contacts
        for q in range(5):    
            spacing = 460
            labelPos = (-40,-130)
            #bottom left, upper right:
            for xy in [(250+q*spacing,100),(-250+(-4+q)*spacing,-400)]:
                sq1=m.Structure(self,self.centered(xy),direction=90)
                
                fingerw0=0.4+0.1*q
                
                self.add(dxf.text(str(np.round(fingerw0,2)),sq1.getLastPos(labelPos),height=60,layer='MARKERS'))
                fingerw=5
                
                #begin qubit (DOLAN)
                self.add(RoundRect(sq1.start,q_height-s_qubit-r_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[1,0,0,1],rotation=sq1.direction,valign=const.MIDDLE),sq1,q_height-s_qubit-r_qubit)
                CPW_stub_short(self, sq1,curve_ins=False,r_out=r_qubit+s_qubit,r_ins=0,w=leadw,s=s_qubit+w_qubit/2-leadw/2)
                sq1.shiftPos(-s_qubit-r_qubit)
                Strip_straight(self, sq1, s_qubit/2+r_qubit,w=leadw)
                CPW_straight(self, sq1, joverlap/2, w=fingerw,s=leadw/2-fingerw/2)
                CPW_taper(self, sq1, taper_l,w0=fingerw,s0=leadw/2-fingerw/2,w1=leadw,s1=0)
                sq1.shiftPos(-taper_l-joverlap/2,angle=180)
                #redefine finger for 2nd layer
                fingerw=fingerw0
                finger2w=fingerw*2
                self.add(dxf.rectangle(sq1.getPos((-finger2w,0)), joverlap/2+finger2w, fingerw, rotation=sq1.direction,valign=const.MIDDLE,bgcolor=self.bg('SECONDLAYER'),layer='SECONDLAYER'),sq1,joverlap/2)
                Strip_taper(self, sq1, s_qubit/2-taper_l,w0=fingerw,w1=leadw,layer='SECONDLAYER')
                Strip_pad(self, sq1, q_height-2*s_qubit, w=w_qubit, r_out=r_qubit,layer='SECONDLAYER')
                #end qubit
                
            #bottom right, upper left
            for xy in [(-250+(-4+q)*spacing,100),(250+q*spacing,-400)]:
                sq1=m.Structure(self,self.centered(xy),direction=90)
                
                fingerw0=0.65+0.1*q
                self.add(dxf.text(str(np.round(fingerw0,2)),sq1.getLastPos(labelPos),height=60,layer='MARKERS'))
                fingerw=5
                
                #begin qubit (DOLAN)
                self.add(RoundRect(sq1.start,q_height-s_qubit-r_qubit, w_qubit+2*s_qubit, r_qubit+s_qubit,roundCorners=[1,0,0,1],rotation=sq1.direction,valign=const.MIDDLE),sq1,q_height-s_qubit-r_qubit)
                CPW_stub_short(self, sq1,curve_ins=False,r_out=r_qubit+s_qubit,r_ins=0,w=leadw,s=s_qubit+w_qubit/2-leadw/2)
                sq1.shiftPos(-s_qubit-r_qubit)
                Strip_straight(self, sq1, s_qubit/2+r_qubit,w=leadw)
                CPW_straight(self, sq1, joverlap/2, w=fingerw,s=leadw/2-fingerw/2)
                CPW_taper(self, sq1, taper_l,w0=fingerw,s0=leadw/2-fingerw/2,w1=leadw,s1=0)
                sq1.shiftPos(-taper_l-joverlap/2,angle=180)
                #redefine finger for 2nd layer
                fingerw=fingerw0
                finger2w=fingerw*2
                self.add(dxf.rectangle(sq1.getPos((-finger2w,0)), joverlap/2+finger2w, fingerw, rotation=sq1.direction,valign=const.MIDDLE,bgcolor=self.bg('SECONDLAYER'),layer='SECONDLAYER'),sq1,joverlap/2)
                Strip_taper(self, sq1, s_qubit/2-taper_l,w0=fingerw,w1=leadw,layer='SECONDLAYER')
                Strip_pad(self, sq1, q_height-2*s_qubit, w=w_qubit, r_out=r_qubit,layer='SECONDLAYER')
                #end qubit
            
            
            #upper row (DOLAN)
            s2=m.Structure(self,self.centered((250+q*spacing,1000)),direction=90)
            fingerw=np.round(0.4+0.1*q,2)
            self.add(dxf.text(str(fingerw)+'x',s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_dolan(self,s2,fingerw=fingerw,finger2w=2*fingerw,leadw=4.0,leadw2=6,overlap=2,eBeam=False)
            s2=m.Structure(self,self.centered((-250-q*spacing,1000)),direction=90)
            fingerw=np.round(0.4+0.1*q,2)
            self.add(dxf.text(str(fingerw)+'=',s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_dolan(self,s2,fingerw=fingerw,finger2w=fingerw,leadw=4.0,leadw2=6,overlap=2,eBeam=False)
            
            #bottom row (normal)
            fingerw=.4+0.2*q
            s2=m.Structure(self,self.centered((250+q*spacing,-1000)),direction=90)
            self.add(dxf.text(str(np.round(fingerw,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0.7,leadw=4.0,overlap=5)
            s2=m.Structure(self,self.centered((-250-q*spacing,-1000)),direction=90)
            fingerw=.5+0.5*q
            self.add(dxf.text(str(np.round(fingerw,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0.7,leadw=4.0,overlap=5)
            
            
              
        #lines
        for j in range(28):
            #lower
            self.add(dxf.rectangle(self.centered((-3000,-1600-14*j)),6000,4.3))
            self.add(dxf.rectangle(self.centered((-3000,-1600-14*j-3)),6000,2))
            self.add(dxf.rectangle(self.centered((-3000,-1600-14*j-6)),6000,2.4))
            self.add(dxf.rectangle(self.centered((-3000,-1600-14*j-9)),6000,2))
            #upper
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j)),6000,4.3))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-3)),6000,2))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-6)),6000,2.4))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-9)),6000,2))
            
        #lines
        for j in range(56):
            #bottom
            self.add(dxf.rectangle(self.centered((-2500+14*j,-3000)),2,1000))
            self.add(dxf.rectangle(self.centered((-2500+14*j+3,-3000)),2.4,1000))
            self.add(dxf.rectangle(self.centered((-2500+14*j+6,-3000)),2,1000))
            self.add(dxf.rectangle(self.centered((-2500+14*j+9,-3000)),4.3,1000))
            
            self.add(dxf.rectangle(self.centered((2500-14*j,-3000)),2,1000))
            self.add(dxf.rectangle(self.centered((2500-14*j-3,-3000)),2.4,1000))
            self.add(dxf.rectangle(self.centered((2500-14*j-6,-3000)),2,1000))
            self.add(dxf.rectangle(self.centered((2500-14*j-9,-3000)),4.3,1000))
            #top
            self.add(dxf.rectangle(self.centered((-2500+14*j,3000)),2,-1000))
            self.add(dxf.rectangle(self.centered((-2500+14*j+3,3000)),2.4,-1000))
            self.add(dxf.rectangle(self.centered((-2500+14*j+6,3000)),2,-1000))
            self.add(dxf.rectangle(self.centered((-2500+14*j+9,3000)),4.3,-1000))
        
        
        #resistance alternating structures
        pad=300
        pad_sep=400
        w_channel=200
        gap=(pad_sep-pad)/2
        total_width=2*pad+2*gap+w_channel
        leadw=20
        offset=20
        overlap=40
        fingerw=4
        N=6
        
        for y in [-2500,2500]:
            srBar=m.Structure(self,self.centered((-pad_sep/2-pad/3-(N-1)*pad_sep/2,y)),defaults={'w':pad,'s':gap,'r_ins':50})
            Strip_stub_open(self,srBar,flipped=True,w=total_width,r_out=pad/3,length=pad_sep/2+pad/3)
            srBar2 = srBar.cloneAlong((0,total_width/2-gap),newDirection=-90)
            srBar2.defaults['r_out']=50
            srBar.translatePos((pad/2+gap,-total_width/2),90)
            for i in range(N):
                CPW_pad(self,srBar,pad,padw=pad,pads=gap,w=leadw,r_out=0,l_lead=(total_width/2-pad-gap-offset-leadw/2))
                CPW_straight(self, srBar, leadw, w=pad_sep/2+overlap,s=pad_sep/4-overlap/2)
                CPW_straight(self,srBar.cloneAlongLast(),leadw-fingerw,w=pad_sep/2-overlap,s=overlap)
                Strip_straight(self, srBar, total_width/2+offset-leadw/2, w=pad_sep)
                srBar.translatePos((-total_width,-pad_sep))
            srBar.translatePos((total_width/2,pad/2+gap),-90)
            Strip_stub_open(self,srBar,w=total_width,r_out=pad/3,length=pad_sep/2+pad/3)
            for i in range(N+1):
                Strip_pad(self,srBar2,pad,padw=pad,layer='SECONDLAYER')
                Strip_straight(self,srBar2,(total_width/2-pad-gap-offset-leadw/2),w=leadw,layer='SECONDLAYER')
                Strip_straight(self, srBar2, leadw, w=pad_sep/2,layer='SECONDLAYER')
                CPW_straight(self, srBar2, offset+overlap/2, w=pad_sep/2-2*fingerw,s=fingerw,layer='SECONDLAYER')
                srBar2.translatePos((-offset-overlap/2-leadw-(total_width/2-pad-gap-offset-leadw/2)-pad,pad_sep))

        # Resistance Bars (left and right)
                
        ResistanceBarBilayer(self, m.Structure(self,self.centered((2700,0)),direction=90),secondlayer='SECONDLAYER')
        ResistanceBarNegative(self, m.Structure(self,self.centered((-2700,0)),direction=90))

        #================== SECOND LAYER =========================
        
        #horizontal lines
        for j in range(42):
            #bottom
            self.add(dxf.rectangle(self.centered((-2600,-3000+24*j+3)),1000,1,layer='SECONDLAYER'))
            self.add(dxf.rectangle(self.centered((-2600,-3000+24*j+12)),1000,2,layer='SECONDLAYER'))
            
            self.add(dxf.rectangle(self.centered((2600,-3000+24*j+3)),-1000,1,layer='SECONDLAYER'))
            self.add(dxf.rectangle(self.centered((2600,-3000+24*j+12)),-1000,2,layer='SECONDLAYER'))
            #top
            self.add(dxf.rectangle(self.centered((-2600,3000-24*j-3)),1000,-1,layer='SECONDLAYER'))
            self.add(dxf.rectangle(self.centered((-2600,3000-24*j-12)),1000,-2,layer='SECONDLAYER'))
            
            
        #vertical lines
        for j in range(250):
            #bottom
            self.add(dxf.rectangle(self.centered((-3000+24*j+3,-1590)),1,-400,layer='SECONDLAYER'))
            self.add(dxf.rectangle(self.centered((-3000+24*j+12,-1590)),2,-400,layer='SECONDLAYER'))
            #top
            self.add(dxf.rectangle(self.centered((-3000+24*j+3,1590)),1,400,layer='SECONDLAYER'))
            self.add(dxf.rectangle(self.centered((-3000+24*j+12,1590)),2,400,layer='SECONDLAYER'))

class QSearchChip6(m.Chip7mm):
    # all optical junctions
    # recreate qubits 
    def __init__(self,wafer,chipID,layer,
                 total_lengths = [4100,4000,3900,3800,3700,3600],#total cpw length (lo to high freq)
                 seps =       [7+4]*6,#distance to cpw
                 coupler_length=180,
                 fingerws =   [0.8,0.95,1.1,1.25,1.4,1.6],
                 finger2ws =   [0.8,0.8,0.85,0.9,0.95,0.95],
                 joverlaps =  [4,4,4,4.5,5,5.5],
                 q_lengths = [282,262,242,222,202,182],
                 q_overlaps = [200,180,160,140,120,100],
                 indices =    [2,1,4,3,0,5],
                 cd_bias = 0,
                 res_spacing=1300):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':10, 's':6, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        for s in self.structures:
            s.shiftPos(340)
            
        #optical markers
        doMirrored(MarkerCross, self, (2900,2900),linewidth=1, chipCentered=True,layer='MARKERS')
        
        #second layer extent markers
        doMirrored(MarkerSquare, self, (3200,3200),width=100, chipCentered=True,layer='SECONDLAYER')
        
        half_trace = self.defaults['w']/2 + self.defaults['s']
                
        CPW_launcher(self,0,padw=250,pads=80,r_ins=30,r_out=30,l_taper=400,layer='BUSMAIN')
        CPW_launcher(self,5,padw=250,pads=80,r_ins=30,r_out=30,l_taper=400,layer='BUSMAIN')        
        
        #calculate separation
        xdist = self.structures[5].start[0] - self.structures[0].start[0]
        CPW_straight(self,0,xdist,layer='BUSMAIN')
        
        #make local copy of s0
        s0  = self.structures[0]
        
        #qubit parameters
        w_qubit = 40
        s_qubit = 20
        r_qubit = 14
        q_sep = 12
        #q_length = 282
        #q_overlap = 200
        
        #junction parameters
        joverlap=10.0#8.0
        joverlap2=8.0#8.0
                
        #CPW resonator parameters
        straight_length=62  #length of straight cpw before meanders start
        straight_length2=94 #length of straight cpw after meanders
        pincer_tee_r=5        
        
        #inductively coupled hanger resonators
        for i in range(6):
            s1 = s0.cloneAlongLast((xdist/2 + res_spacing*(-1+indices[i]//2)-coupler_length/2,pow(-1,indices[i])*(half_trace + seps[i] + half_trace)))
            s1.defaults['s']=10
            s1.defaults['radius']=50
            s1.defaults['r_ins']=10
            s1.defaults['r_out']=20
            CPW_stub_short(self, s1, flipped=True)
            CPW_straight(self, s1, coupler_length)
            CPW_bend(self, s1, CCW=indices[i]%2)
            CPW_straight(self,s1,straight_length)
            CPW_bend(self,s1,CCW=indices[i]%2)
            CPW_straight(self,s1,coupler_length/2)#unsure the length here
            CPW_wiggles(self, s1, length=total_lengths[i]-1.5*coupler_length-straight_length - straight_length2-np.pi*s1.defaults['radius'], nTurns=4,start_bend=False,CCW=indices[i]%2)
            CPW_straight(self,s1,straight_length2-pincer_tee_r)
            
            #qubit
            CPW_pincer(self,s1,pincer_w=w_qubit+2*s_qubit+2*q_sep,pincer_l=q_overlaps[i],pincer_padw=35,pincer_tee_r=pincer_tee_r,pad_r=30)
            s1.shiftPos(q_sep)
            #XmonTrilayerDolan(self,s1,q_length,w_qubit=w_qubit,s_qubit=s_qubit,r_qubit=r_qubit,fingerw=fingerws[i],finger2w=1.75*fingerws[i],leadw=10,leadw2=4,jsep=8,taper_l=6,joverlap=joverlap,joverlap2=joverlap2,secondlayer='SECONDLAYER',eBeam=False)
            XmonTrilayer(self,s1,q_lengths[i],w_qubit=w_qubit,s_qubit=s_qubit,r_qubit=r_qubit,fingerw=fingerws[i],finger2w=finger2ws[i],leadw=10,leadw2=5,joverlap=joverlaps[i],joverlap2=joverlaps[i]+2)
            self.add(dxf.text(str(i),s1.getPos((0,200)),height=64,layer='FRAME'))

        #junction contacts
        for q in range(2):
            spacing = 420
            labelPos = (-40,-130)

            #upper row
            s2=m.Structure(self,self.centered((-2200-q*spacing,2400)),direction=90)
            self.add(dxf.text(str(np.round(0.7+0.2*q,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=0.7+0.2*q,finger2w=0.7+0.2*q,leadw=4.0,pad=250,overlap=5)
            #bottom row
            s2=m.Structure(self,self.centered((2200+q*spacing,-2400)),direction=90)
            self.add(dxf.text(str(np.round(.5+0.1*q,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=.5+0.1*q,finger2w=0.7,leadw=4.0,pad=250,overlap=5)
            s2=m.Structure(self,self.centered((-2200-q*spacing,-2400)),direction=90)
            self.add(dxf.text(str(np.round(0.8+0.2*q,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=0.8+0.2*q,finger2w=0.8+2*q,leadw=4.0,pad=250,overlap=5)
        
        
        #resistance bars
        #are these causing modes? get rid of them for now
        #ResistanceBarBilayer(self,m.Structure(self,self.centered((0,3000))),secondlayer='SECONDLAYER')
        #ResistanceBarNegative(self,m.Structure(self,self.centered((0,-3000))))
        
        
class InverseQSearchChip6(m.Chip7mm):
    #start with replicating Q5 from 39P
    #reduce capacitor with qubit freqency (as junction capacitance is increasing)
    #constrain second finger to be 0.8um, the largest finger we know that gives good Q
    def __init__(self,wafer,chipID,layer,
                 total_lengths = [4100,4000,3900,3800,3700,3600],#total cpw length (lo to high freq)
                 seps =       [7+4]*6,#distance to cpw
                 coupler_length=180,
                 fingerws =   [0.8,0.95,1.1,1.25,1.4,1.6],
                 finger2ws =   [0.8]*6,
                 joverlaps =  [4,4,4,4.5,5,5.5],
                 q_lengths = [282,262,242,222,202,182],
                 q_overlaps = [200,180,160,140,120,100],
                 indices =    [2,1,4,3,0,5],
                 cd_bias = 0,
                 res_spacing=1300):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':10, 's':6, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        for s in self.structures:
            s.shiftPos(340)
            
        #XOR square to cover whole chip-- first layer
        self.add(dxf.rectangle(self.center,6700,5000,halign=const.CENTER,valign=const.MIDDLE,layer='BASEMETAL',bgcolor=self.wafer.bg('BASEMETAL')))
        self.add(dxf.rectangle(self.centered((0,5000/2)),5400-2*900,850,halign=const.CENTER,valign=const.TOP,layer='BASEMETAL',bgcolor=self.wafer.bg('BASEMETAL')))
        self.add(dxf.rectangle(self.centered((0,-5000/2)),5400,850,halign=const.CENTER,valign=const.BOTTOM,layer='BASEMETAL',bgcolor=self.wafer.bg('BASEMETAL')))
        
        #XOR square to cover whole chip-- second layer
        self.add(dxf.rectangle(self.center,6800,6800,halign=const.CENTER,valign=const.MIDDLE,layer='SECONDLAYER',bgcolor=self.wafer.bg('SECONDLAYER')))
        
        #optical markers
        doMirrored(MarkerCross, self, (2900,2900),linewidth=1, chipCentered=True,layer='MARKERS')
        
        #second layer extent markers.... but actually this means first layer
        #doMirrored(MarkerSquare, self, (3200,3200),width=100, chipCentered=True,layer='XOR')
        
        half_trace = self.defaults['w']/2 + self.defaults['s']
                
        CPW_launcher(self,0,padw=250,pads=80,r_ins=30,r_out=30,l_taper=400,layer='XOR2')
        CPW_launcher(self,5,padw=250,pads=80,r_ins=30,r_out=30,l_taper=400,layer='XOR2')        
        
        #calculate separation
        xdist = self.structures[5].start[0] - self.structures[0].start[0]
        CPW_straight(self,0,xdist,layer='XOR2')
        
        #make local copy of s0
        s0  = self.structures[0]
        
        #qubit parameters
        w_qubit = 40
        s_qubit = 20
        q_sep = 12
        #q_length = 282
        #q_overlap = 200
        r_qubit = 14
        
        #junction parameters
        joverlap=10.0#8.0
        joverlap2=8.0#8.0
        
        
        #CPW resonator parameters
        #(define in function)coupler_length=180  #length of inductive coupler overlap
        straight_length=62  #length of straight cpw before meanders start
        straight_length2=94 #length of straight cpw after meanders
        pincer_tee_r=5
        
        
        #inductively coupled hanger resonators
        for i in range(6):
            s1 = s0.cloneAlongLast((xdist/2 + res_spacing*(-1+indices[i]//2)-coupler_length/2,pow(-1,indices[i])*(half_trace + seps[i] + half_trace)))
            s1.defaults['s']=10
            s1.defaults['radius']=50
            s1.defaults['r_ins']=10
            s1.defaults['r_out']=20
            CPW_stub_short(self, s1, flipped=True)
            CPW_straight(self, s1, coupler_length)
            CPW_bend(self, s1, CCW=indices[i]%2)
            CPW_straight(self,s1,straight_length)
            CPW_bend(self,s1,CCW=indices[i]%2)
            CPW_straight(self,s1,coupler_length/2)#unsure the length here
            CPW_wiggles(self, s1, length=total_lengths[i]-1.5*coupler_length-straight_length - straight_length2-np.pi*s1.defaults['radius'], nTurns=4,start_bend=False,CCW=indices[i]%2)
            CPW_straight(self,s1,straight_length2-pincer_tee_r)
            
            #qubit
            CPW_pincer(self,s1,pincer_w=w_qubit+2*s_qubit+2*q_sep,pincer_l=q_overlaps[i],pincer_padw=35,pincer_tee_r=pincer_tee_r,pad_r=30)
            s1.shiftPos(q_sep)
            XmonTrilayer(self,s1,q_lengths[i],w_qubit=w_qubit,s_qubit=s_qubit,r_qubit=r_qubit,fingerw=fingerws[i],finger2w=finger2ws[i],leadw=10,leadw2=5,joverlap=joverlaps[i],joverlap2=joverlaps[i]+2,secondlayer='XOR')
            #XmonTrilayerDolan(self,s1,q_length,w_qubit=w_qubit,s_qubit=s_qubit,r_qubit=r_qubit,fingerw=fingerws[i],finger2w=fingerws[i],leadw=10,leadw2=5,jsep=8,taper_l=6,joverlap=joverlap,joverlap2=joverlap2,secondlayer='XOR',eBeam=False)
            self.add(dxf.text(str(i),s1.getPos((0,200)),height=64,layer='FRAME'))

        #resistance bars
        #are these causing modes? get rid of them for now
        #ResistanceBarBilayer(self,m.Structure(self,self.centered((0,3000))),secondlayer='XOR')
        #ResistanceBarNegative(self,m.Structure(self,self.centered((0,-3000))))

class ResonatorChip6(m.Chip7mm):
    def __init__(self,wafer,chipID,layer,
                 L_ws =       [320,305,290,280,265,250], #Lw the wiggle length of each resonator (sets the resonator frequency) (lo to high freq)
                 seps =       [200, 220,240,220,260,280],#resonator distance to cpw (sets each resonator's coupling)
                 indices =    [2,0,5,3,1,4], #these indices are chosen so no two adjacent resonators are close in frequency (to limit crosstalk)
                 res_spacing=1200 # how far apart the resonators are
                 ):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':10, 's':6, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        for s in self.structures:
            #move away from edge of chip
            s.shiftPos(340)
            
        #optical markers
        doMirrored(MarkerCross, self, (2900,2900),linewidth=5, chipCentered=True,layer='MARKERS')
        
        half_trace = self.defaults['w']/2 + self.defaults['s']
                
        CPW_launcher(self,0,padw=250,pads=80,r_ins=30,r_out=30,l_taper=400,layer='BUSMAIN')
        CPW_launcher(self,5,padw=250,pads=80,r_ins=30,r_out=30,l_taper=400,layer='BUSMAIN')        
        
        #calculate separation between the two structures
        xdist = self.structures[5].start[0] - self.structures[0].start[0]
        CPW_straight(self,0,xdist,layer='BUSMAIN')
        
        #make local copy of s0
        s0  = self.structures[0]
        
        #write the resonators
        for i in range(6):
            # make a clone of s0 at varying distances along the main bus, some distance off to the side. 
            # alternate offseting left and right of the bus, and set the new direction to point away from the main bus
            s1 = s0.cloneAlongLast((xdist/2 + res_spacing*(-1.25+0.5*indices[i]),pow(-1,indices[i])*(half_trace + seps[i])),newDirection=(90+180*indices[i])%360)
            # this forms the jellyfish resonator. the capacitor is defined by w_cap and s_cap, similar to a cpw
            # the first two arguments are the width and height of the resonator. Weird things happen if the width is too small or height too short...
            # we specify the width of the inductor, and instead of giving a overall wire length, we set the number of turns, and the max wiggle length
            # wiggle length is half the distance from the the edge of one bend to the opposite side
            # we also want the wiggles to bunch near the capacitor (ialign) although this doesn't matter since we chose the height of the resonator to be exact
            JellyfishResonator(self,s1,500,412,None,r_ind=4,w_ind=3,w_cap=40,s_cap=20,maxWidth=L_ws[i]/2.,nTurns=19,ialign=const.TOP)
            #label the resonator for debugging
            self.add(dxf.text(str(i),vadd(s1.start,(360,80)),height=48,layer='FRAME'))
        
        #resistance bars on unused area of chip
        ResistanceBarNegative(self,m.Structure(self,self.centered((0,-3000))))
        ResistanceBarNegative(self,m.Structure(self,self.centered((0,3000))))
        
jelly6 = ResonatorChip6(w,'JELLY6','BASEMETAL')
waffle(jelly6, 100, width=20,bleedRadius=1,padx=700,layer='MARKERS')
jelly6.save(w)

jarrayChip1 = EtchTestChip(w,'JARRAY','BASEMETAL')
jarrayChip1.save(w,drawCopyDXF=False,dicingBorder=False)

XSearchChip = QSearchChip6(w,'XSEARCH','BASEMETAL')
waffle(XSearchChip, 100, width=20,bleedRadius=1,padx=700,layer='MARKERS')
XSearchChip.save(w,drawCopyDXF=False,dicingBorder=False,center=True)

XInverseChip = InverseQSearchChip6(w,'XINVERSE','XOR2')
waffle(XInverseChip, 100, width=20,bleedRadius=1,padx=700,layer='XOR2',exclude=['BASEMETAL','SECONDLAYER'])
XInverseChip.save(w,drawCopyDXF=False,dicingBorder=False,center=True)

#optical markers
doMirrored(MarkerSquare, w, (15000,15000), width=20, layer='MARKERS')
doMirrored(MarkerSquare, w, (16000,15000), layer='MARKERS')

doMirrored(MarkerCross, w, (16000,16000),linewidth=1, layer='MARKERS')


for i in range(len(w.chips)):
    #populate with jarray
    w.chips[i]=jarrayChip1
    #identifying marks
    w.add(dxf.text(str(i),vadd(w.chipPts[i],(5400,6100)),height=600,layer='MARKERS'))
    w.add(dxf.text('41X',vadd(w.chipPts[i],(1200,6600)),height=240,layer='MARKERS'))

for i in [1,2,5,6,7,8,14,19,20,21]:
    w.chips[i]=XInverseChip
for i in [11,15,17,23,24,25,26,29,30]:
    w.chips[i]=XSearchChip
for i in [12,18]:
    w.setChipBuffer(jelly6, i)
    

# write all chips
w.populate()
w.save()