#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:29:41 2021

@author: sasha

Generating file for wafer including:
    - 6 xmon chip with lambda/4 resonators
    - etch test chips with junction area arrays

Changes (xmon chip):
    - continue to have inverted 
    - increase coupler length, and move 
    - decrease bottom finger overlap
Changes (jarray chip)
    - increase junction range
    - swap dolan junctions back to manhattan
"""

import maskLib.MaskLib as m
from maskLib.dcLib import Rbar
from maskLib.microwaveLib import *
from maskLib.Entities import SolidPline, SkewRect, CurveRect, InsideCurve
import numpy as np
import ezdxf
from dxfwrite import DXFEngine as dxf
from dxfwrite import const
from dxfwrite.entities import *
from dxfwrite.vector2d import vadd

from maskLib.utilities import doMirrored
from maskLib.markerLib import MarkerSquare, MarkerCross
from maskLib.junctionLib import DolanJunction, JContact_tab, ManhattanJunction, JcalcTabDims, JContact_slot, JContact_tab, JSingleProbePad, JProbePads


from maskLib.resonatorLib import JellyfishResonator,CingularResonator
#from maskLib.qubitLib import Xmon

# ===============================================================================
# wafer setup
# ===============================================================================

w = m.Wafer('NANSi01','',7000,7000,padding=500,waferDiameter=100000,sawWidth=200,#m.sawL_ws['8A'],
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
    ['DICEGRID',3],
    ['MARKERS',2],
    ['LYR1',7],#target for XOR operations
    ['LYR2',3], #target for XOR operations
    ['outercut',8]])


#initialize the wafer
w.init()

#do dicing border
w.DicingBorder()
    
curve_pts = 30  #point resolution of all curves
    
def overlap_junction_bilayer(chip,structure,jjw = 0.5, length=300,pad=300,gap=30,width=80,jsep=30,taperl=4,fingerw=0,
                             finger2w=None,leadw=None,offset=0,overlap=7,cdbias=0.0,secondlayer='SECONDLAYER', uc_width=0.7):   
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
    # CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    #overlap part
    # chip.add(dxf.rectangle(struct().getPos((-overlap/2,-offset+leadw/2)),finger2w,offset-leadw/2-fingerw/2,rotation=struct().direction,layer=secondlayer))
    # chip.add(dxf.rectangle(struct().getPos((-overlap/2-cdbias,-fingerw/2)),finger2w+2*cdbias,fingerw,rotation=struct().direction,layer=secondlayer))
    # chip.add(dxf.rectangle(struct().getPos((-overlap/2,fingerw/2)),finger2w,overlap-(offset-leadw/2-fingerw/2),rotation=struct().direction,layer=secondlayer))
    overhang = 5
    jpadw = 15
    jarmw = 3
    jtaperl=2-1.36-0.140
    jfingerl=1.36
    struct().translatePos((gap/2,0))
    DolanJunction(chip, struct(), junctionl=gap, 
                  jpadoverhang = overhang, 
                  jfingerw = jjw + uc_width*1.5,
                  jpadw=jpadw,
                  JLAYER = secondlayer,
                  ULAYER  = secondlayer,
                  jarmw = jarmw + uc_width*2,
                  jtaperl=jtaperl,
                  jfingerl= jfingerl)
    struct().translatePos((-gap/2-overhang*2,0))
    DolanJunction(chip, struct(), junctionl=gap, jpadoverhang = overhang, jfingerw = jjw , jpadw = jpadw)
    # struct().translatePos((-gap/2,0))
    
    struct().translatePos((-overhang*2,0))
    sl2 = struct().cloneAlong((0,0))

    CPW_taper(chip,struct(),taperl,s0=gap+width/2-fingerw/2,w0=fingerw,w1=width,offset=(0,-offset/2))
    
    CPW_straight(chip,struct(), length/2-gap-jsep, w=width)
    
    # CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    CPW_stub_short(chip,struct(),flipped=True,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
    CPW_straight(chip,struct(),pad)
    CPW_stub_open(chip,struct(),flipped=False)

    Strip_straight(chip,sl2, -gap, w=width+2*gap)
    # Strip_taper(chip,sl2,taperl,w0=leadw,w1=width)
    # Strip_straight(chip,sl2,length/2-jsep,w=width)
    # Strip_straight(chip,sl2,pad,w=pad)
    
    # Strip_straight(chip,struct(), length/2-gap-jsep/2, w=width+2*gap)
    # Strip_stub_open(chip,struct(),flipped=True,w=pad+2*gap)
    # Strip_straight(chip,struct(),pad,w=pad+2*gap)
    # Strip_stub_open(chip,struct(),w=pad+2*gap)

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
    # CPW_straight(chip,struct(), length/2-gap-jsep, w=width)
    # CPW_taper(chip,struct(),taperl,s1=gap+width/2-fingerw/2,w1=fingerw,w0=width)
    # CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    #struct().translatePos((0,-offset))
    sl2 = struct().cloneAlong((-overlap,-fingerw/2-leadw/2+overlap))



    Strip_straight(chip,sl2, jsep/2-taperl+overlap, w=leadw)
    Strip_taper(chip,sl2,taperl,w0=leadw,w1=width,offset=(0,fingerw/2+leadw/2-overlap))
    Strip_straight(chip,sl2,length/2-jsep,w=width,)
    Strip_straight(chip,sl2,pad,w=pad,)
    
    Strip_straight(chip,struct(), length/2-gap-jsep/2, w=width+2*gap)
    Strip_stub_open(chip,struct(),flipped=True,w=pad+2*gap)
    Strip_straight(chip,struct(),pad,w=pad+2*gap)
    Strip_stub_open(chip,struct(),w=pad+2*gap)

'''
        #qubit parameters
        w_qubit = 30
        s_qubit = 30
        q_sep = 12
        q_length = 224
        q_overlap = 200
        #r_qubit = 24
        #junction parameters
        leadw=4.0
        finger2w=0.7
        joverlap=8.0
        taper_l = 4
        cdbias=0.2
'''


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



#=============================
class EtchTestChip(m.Chip7mm):
    def __init__(self,wafer,chipID,layer):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':20, 's':10, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        #DICING GRID SQUARE TO COVER WHOLE CHIP
        self.add(dxf.rectangle(self.center,6200,6200,halign=const.CENTER,valign=const.MIDDLE,layer='DICEGRID',bgcolor=self.wafer.bg('DICEGRID')))
        
        #optical markers
        doMirrored(MarkerSquare, self, (2900,2900),linewidth=1, chipCentered=True,layer='MARKERS')
        
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
        finger2w=2 #change this if 1st layer succeeds
        joverlap=6.0#8.0
        joverlap2=8.0
        taper_l = 4
        cdbias=0.0
        
        #junction contacts
        for q in range(5):    
            spacing = 460
            labelPos = (-40,-130)
            # labelPos2 = (-40,-150)
            #bottom left, upper right:
            for xy in [(250+q*spacing,100),(-250+(-4+q)*spacing,-400)]:
                sq1=m.Structure(self,self.centered(xy),direction=90)
                
                jjw =np.round(0.1+0.05*q,3)
                pad_len = 200
                pad = 150
                gap = 30
                length = 100

                sq1.defaults['w']=pad
                sq1.defaults['s']=gap
                sq1.defaults['r_out']=gap
                CPW_stub_open(self,sq1,flipped=True)
                CPW_straight(self,sq1,pad_len)
                CPW_stub_open(self,sq1,flipped=False)
    
                self.add(dxf.text(str(jjw),sq1.getLastPos(labelPos),height=60,layer='MARKERS'))
                overhang = 5
                sq1.shiftPos(-gap/2)
                DolanJunction(self, sq1, junctionl=gap, jpadoverhang = overhang, jfingerw = jjw )
                 #end qubit
                
            #bottom right, upper left
            for xy in [(-250+(-4+q)*spacing,100),(250+q*spacing,-400)]:
                sq1=m.Structure(self,self.centered(xy),direction=90)
                
                jjw =np.round(0.1+0.05*q,3)
                pad_len = 200
                pad = 150
                gap = 30
                length = 100

                sq1.defaults['w']=pad
                sq1.defaults['s']=gap
                sq1.defaults['r_out']=gap
                CPW_stub_open(self,sq1,flipped=True)
                CPW_straight(self,sq1,pad_len)
                CPW_stub_open(self,sq1,flipped=False)
    
                self.add(dxf.text(str(jjw),sq1.getLastPos(labelPos),height=60,layer='MARKERS'))
                overhang = 5
                sq1.shiftPos(-gap/2)
                DolanJunction(self, sq1, junctionl=gap, jpadoverhang = overhang, jfingerw = jjw )
                #end qubit
            
            gap = 30
            fingerw = 2
            #upper row
            s2=m.Structure(self,self.centered((250+q*spacing,1000)),direction=90)
            jjw =np.round(0.1+0.05*q,3)
            self.add(dxf.text(str(jjw)+'.',s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30, jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            s2=m.Structure(self,self.centered((-250-q*spacing,1000)),direction=90)
            
            
            jjw =np.round(0.2+0.05*q,3)
            self.add(dxf.text(str(jjw)+'.',s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30, jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            #bottom row
            
            jjw =np.round(0.3+0.05*q,3)
            s2=m.Structure(self,self.centered((250+q*spacing,-1000)),direction=90)
            self.add(dxf.text(str(jjw),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30, jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            s2=m.Structure(self,self.centered((-250-q*spacing,-1000)),direction=90)
            
            
            jjw =np.round(0.4+0.05*q,3)
            self.add(dxf.text(str(jjw),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30,    jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            
            
            
        
        #lines
        for j in range(28):
            #lower
            self.add(dxf.rectangle(self.centered((0,-1600-14*j)),600,4.3,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((0,-1600-14*j-3)),600,2,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((0,-1600-14*j-6)),600,2.4,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((0,-1600-14*j-9)),600,2,layer='JUNCTION'))
            upper
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j)),6000,4.3))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-3)),6000,2))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-6)),6000,2.4))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-9)),6000,2))
            
        lines
        for j in range(28):
            #bottom
            self.add(dxf.rectangle(self.centered((0+14*j,-3000)),2,600,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((0+14*j+3,-3000)),2.4,600,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((0+14*j+6,-3000)),2,600,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((0+14*j+9,-3000)),4.3,600,layer='JUNCTION'))
            
            self.add(dxf.rectangle(self.centered((2500-14*j,-3000)),2,1000,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((2500-14*j-3,-3000)),2.4,1000,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((2500-14*j-6,-3000)),2,1000,layer='JUNCTION'))
            self.add(dxf.rectangle(self.centered((2500-14*j-9,-3000)),4.3,1000,layer='JUNCTION'))
            top
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
        
        # for y in [-2500,2500]:
        #     srBar=m.Structure(self,self.centered((-pad_sep/2-pad/3-(N-1)*pad_sep/2,y)),defaults={'w':pad,'s':gap,'r_ins':50})
        #     Strip_stub_open(self,srBar,flipped=True,w=total_width,r_out=pad/3,length=pad_sep/2+pad/3)
        #     srBar2 = srBar.cloneAlong((0,total_width/2-gap),newDirection=-90)
        #     srBar2.defaults['r_out']=50
        #     srBar.translatePos((pad/2+gap,-total_width/2),90)
        #     for i in range(N):
        #         CPW_pad(self,srBar,pad,padw=pad,pads=gap,w=leadw,r_out=0,l_lead=(total_width/2-pad-gap-offset-leadw/2))
        #         CPW_straight(self, srBar, leadw, w=pad_sep/2+overlap,s=pad_sep/4-overlap/2)
        #         CPW_straight(self,srBar.cloneAlongLast(),leadw-fingerw,w=pad_sep/2-overlap,s=overlap)
        #         Strip_straight(self, srBar, total_width/2+offset-leadw/2, w=pad_sep)
        #         srBar.translatePos((-total_width,-pad_sep))
        #     srBar.translatePos((total_width/2,pad/2+gap),-90)
        #     Strip_stub_open(self,srBar,w=total_width,r_out=pad/3,length=pad_sep/2+pad/3)
        #     for i in range(N+1):
        #         Strip_pad(self,srBar2,pad,padw=pad,layer='SECONDLAYER')
        #         Strip_straight(self,srBar2,(total_width/2-pad-gap-offset-leadw/2),w=leadw,layer='SECONDLAYER')
        #         Strip_straight(self, srBar2, leadw, w=pad_sep/2,layer='SECONDLAYER')
        #         CPW_straight(self, srBar2, offset+overlap/2, w=pad_sep/2-2*fingerw,s=fingerw,layer='SECONDLAYER')
        #         srBar2.translatePos((-offset-overlap/2-leadw-(total_width/2-pad-gap-offset-leadw/2)-pad,pad_sep))
                
        #resistance bar
        gap=50
        pad=600
        length=1500
        width=40
        
        #top
        srBar=m.Structure(self,self.centered((2700,-length/2-pad-gap)),direction=90,defaults={'w':pad,'s':gap,'r_out':gap})
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        srBar2 = srBar.cloneAlong()
        Strip_straight(self,srBar,pad,w=pad+2*gap, )
        Strip_stub_open(self,srBar,flipped=False,w=pad+2*gap)
        Strip_straight(self, srBar, length-2*gap, w=width+2*gap)
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        Strip_straight(self,srBar,pad,w=pad+2*gap)
        Strip_stub_open(self,srBar,w=pad+2*gap)
        
        Strip_straight(self,srBar2,pad,w=pad,layer='JUNCTION2')
        Strip_straight(self, srBar2, length, w=width,layer='JUNCTION2')
        Strip_straight(self,srBar2,pad,w=pad,layer='JUNCTION2')

        
        #bottom
        srBar=m.Structure(self,self.centered((-2700,-length/2-pad-gap)),direction=90,defaults={'w':pad,'s':gap,'r_out':gap})
        CPW_stub_open(self,srBar,flipped=True)
        CPW_straight(self,srBar,pad)
        CPW_stub_short(self,srBar,flipped=False,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self, srBar, length-2*gap, w=width)
        CPW_stub_short(self,srBar,flipped=True,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self,srBar,pad)
        CPW_stub_open(self,srBar)
        
        
        
        #================== SECOND LAYER =========================
        
        #horizontal lines
        # for j in range(20):
        #     #bottom
        #     self.add(dxf.rectangle(self.centered((0,-3000+24*j+3)),400,1,layer='UNDERCUT'))
        #     self.add(dxf.rectangle(self.centered((0,-3000+24*j+12)),400,2,layer='UNDERCUT'))
            
            # self.add(dxf.rectangle(self.centered((2600,-3000+24*j+3)),-1000,1,layer='UNDERCUT'))
            # self.add(dxf.rectangle(self.centered((2600,-3000+24*j+12)),-1000,2,layer='UNDERCUT'))
            # #top
            # self.add(dxf.rectangle(self.centered((-2600,3000-24*j-3)),1000,-1,layer='UNDERCUT'))
            # self.add(dxf.rectangle(self.centered((-2600,3000-24*j-12)),1000,-2,layer='UNDERCUT'))
            
            
        # #vertical lines
        # for j in range(25):
        #     #bottom
        #     self.add(dxf.rectangle(self.centered((0+24*j+3,-1590)),1,-400,layer='UNDERCUT'))
        #     self.add(dxf.rectangle(self.centered((0+24*j+12,-1590)),2,-400,layer='UNDERCUT'))
            # #top
            # self.add(dxf.rectangle(self.centered((-3000+24*j+3,1590)),1,400,layer='UNDERCUT'))
            # self.add(dxf.rectangle(self.centered((-3000+24*j+12,1590)),2,400,layer='UNDERCUT'))

class QSearchChip6(m.Chip7mm):
    def __init__(self,wafer,chipID,layer,
                 total_lengths = [4100,4000,3900,3800,3700,3600],#total cpw length (lo to high freq)
                 seps =       [10+4]*6,#distance to cpw
                 fingerws =   [0.45,0.5,0.55,0.6,0.65,0.7],
                 joverlaps =  [4,4,4,4,4.5,5],
                 indices =    [2,1,4,3,0,5],
                 cd_bias = 0,
                 res_spacing=1300):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':10, 's':6, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        for s in self.structures:
            s.shiftPos(340)
        
        #DICING GRID SQUARE TO COVER WHOLE CHIP
        self.add(dxf.rectangle(self.center,6200,6600,halign=const.CENTER,valign=const.MIDDLE,layer='DICEGRID',bgcolor=self.wafer.bg('DICEGRID')))
        
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
        q_sep = 12
        q_length = 242    #282
        q_overlap = 180   #200
        
        #junction parameters
        joverlap=6.0#8.0
        joverlap2=8.0#8.0
        
        
        #CPW resonator parameters
        coupler_length=190  #length of inductive coupler overlap
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
            CPW_pincer(self,s1,pincer_w=w_qubit+2*s_qubit+2*q_sep,pincer_l=q_overlap,pincer_padw=35,pincer_tee_r=pincer_tee_r,pad_r=30)
            s1.shiftPos(q_sep)
            #Xmon(self,s1,xmonw=w_qubit,xmon_gapw=s_qubit,xmon_gapl=s_qubit,jpadr=2,xmonl=q_length)
            XmonTrilayer(self,s1,q_length,w_qubit=w_qubit,s_qubit=s_qubit,r_qubit=14,fingerw=fingerws[i],finger2w=fingerws[i],leadw=10,leadw2=5,jsep=8,joverlap=joverlaps[i],joverlap2=joverlaps[i]+2)
            self.add(dxf.text(str(i),s1.getPos((0,200)),height=64,layer='FRAME'))

        #junction contacts
        for q in range(2):
            spacing = 420
            labelPos = (-40,-130)

            #upper row
            s2=m.Structure(self,self.centered((-2200-q*spacing,2400)),direction=90)
            self.add(dxf.text(str(np.round(0.7+0.2*q,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=0.7+0.2*q,finger2w=0.7,leadw=4.0,pad=250,overlap=5)
            #bottom row
            s2=m.Structure(self,self.centered((2200+q*spacing,-2400)),direction=90)
            self.add(dxf.text(str(np.round(.5+0.1*q,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=.5+0.1*q,finger2w=0.7,leadw=4.0,pad=250,overlap=5)
            s2=m.Structure(self,self.centered((-2200-q*spacing,-2400)),direction=90)
            self.add(dxf.text(str(np.round(0.8+0.2*q,2)),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=0.8+0.2*q,finger2w=0.7,leadw=4.0,pad=250,overlap=5)
        
        
        #resistance bar
        gap=50
        pad=600
        length=1500
        width=40
        
        #top
        srBar=m.Structure(self,self.centered((-length/2-pad-gap,3000)),defaults={'w':pad,'s':gap,'r_out':gap})
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        srBar2 = srBar.cloneAlong()
        Strip_straight(self,srBar,pad,w=pad+2*gap)
        Strip_stub_open(self,srBar,flipped=False,w=pad+2*gap)
        Strip_straight(self, srBar, length-2*gap, w=width+2*gap)
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        Strip_straight(self,srBar,pad,w=pad+2*gap)
        Strip_stub_open(self,srBar,w=pad+2*gap)
        
        Strip_straight(self,srBar2,pad,w=pad,layer='SECONDLAYER')
        Strip_straight(self, srBar2, length, w=width,layer='SECONDLAYER')
        Strip_straight(self,srBar2,pad,w=pad,layer='SECONDLAYER')
        
        #bottom
        srBar=m.Structure(self,self.centered((-length/2-pad-gap,-3000)),defaults={'w':pad,'s':gap,'r_out':gap})
        CPW_stub_open(self,srBar,flipped=True)
        CPW_straight(self,srBar,pad)
        CPW_stub_short(self,srBar,flipped=False,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self, srBar, length-2*gap, w=width)
        CPW_stub_short(self,srBar,flipped=True,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self,srBar,pad)
        CPW_stub_open(self,srBar)
        
class InverseQSearchChip6(m.Chip7mm):
    def __init__(self,wafer,chipID,layer,
                 total_lengths = [4200,4100,4000,3900,3800,3700],#total cpw length (lo to high freq)
                 seps =       [10+4]*6,#distance to cpw
                 fingerws =   [0.6,0.75,0.9,1.05,1.2,1.35],
                 joverlaps =  [4,4,4.5,5,5.5,6],
                 indices =    [2,1,4,3,0,5],#[2,5,1,4,0,3],
                 cd_bias = 0,
                 res_spacing=1300):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':10, 's':6, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        for s in self.structures:
            s.shiftPos(340)
        
        #DICING GRID SQUARE TO COVER WHOLE CHIP
        self.add(dxf.rectangle(self.center,6200,6600,halign=const.CENTER,valign=const.MIDDLE,layer='DICEGRID',bgcolor=self.wafer.bg('DICEGRID')))
        
        
        #XOR square to cover whole chip-- first layer
        self.add(dxf.rectangle(self.center,6700,5000,halign=const.CENTER,valign=const.MIDDLE,layer='BASEMETAL',bgcolor=self.wafer.bg('BASEMETAL')))
        self.add(dxf.rectangle(self.centered((-900/2,5000/2)),5400-900,850,halign=const.CENTER,valign=const.TOP,layer='BASEMETAL',bgcolor=self.wafer.bg('BASEMETAL')))
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
        q_length = 202
        q_overlap = 160
        #r_qubit = 24
        #junction parameters
        joverlap=6.0#8.0
        joverlap2=8.0#8.0
        
        
        #CPW resonator parameters
        coupler_length=190  #length of inductive coupler overlap
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
            CPW_pincer(self,s1,pincer_w=w_qubit+2*s_qubit+2*q_sep,pincer_l=q_overlap,pincer_padw=35,pincer_tee_r=pincer_tee_r,pad_r=30)
            s1.shiftPos(q_sep)
            #Xmon(self,s1,xmonw=w_qubit,xmon_gapw=s_qubit,xmon_gapl=s_qubit,jpadr=2,xmonl=q_length)
            XmonTrilayer(self,s1,q_length,w_qubit=w_qubit,s_qubit=s_qubit,r_qubit=14,fingerw=fingerws[i],finger2w=fingerws[i],leadw=10,leadw2=5,jsep=8,joverlap=joverlaps[i],joverlap2=joverlaps[i]+2,secondlayer='XOR')
            self.add(dxf.text(str(i),s1.getPos((0,200)),height=64,layer='FRAME'))

        #resistance bar
        gap=50
        pad=600
        length=1500
        width=40
        
        #top
        srBar=m.Structure(self,self.centered((-length/2-pad-gap,3000)),defaults={'w':pad,'s':gap,'r_out':gap})
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        srBar2 = srBar.cloneAlong()
        Strip_straight(self,srBar,pad,w=pad+2*gap)
        Strip_stub_open(self,srBar,flipped=False,w=pad+2*gap)
        Strip_straight(self, srBar, length-2*gap, w=width+2*gap)
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        Strip_straight(self,srBar,pad,w=pad+2*gap)
        Strip_stub_open(self,srBar,w=pad+2*gap)
        
        Strip_straight(self,srBar2,pad,w=pad,layer='XOR')
        Strip_straight(self, srBar2, length, w=width,layer='XOR')
        Strip_straight(self,srBar2,pad,w=pad,layer='XOR')
        
        #bottom
        srBar=m.Structure(self,self.centered((-length/2-pad-gap,-3000)),defaults={'w':pad,'s':gap,'r_out':gap})
        CPW_stub_open(self,srBar,flipped=True)
        CPW_straight(self,srBar,pad)
        CPW_stub_short(self,srBar,flipped=False,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self, srBar, length-2*gap, w=width)
        CPW_stub_short(self,srBar,flipped=True,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self,srBar,pad)
        CPW_stub_open(self,srBar)

class ResonatorChip(m.Chip7mm):
    def __init__(self,wafer,chipID,layer,file_name = 'resonators.dxf'):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':20, 's':10, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        #DICING GRID SQUARE TO COVER WHOLE CHIP
        self.add(dxf.rectangle(self.center,6200,6200,halign=const.CENTER,valign=const.MIDDLE,layer='DICEGRID',bgcolor=self.wafer.bg('DICEGRID')))
        
        #optical markers
        doMirrored(MarkerSquare, self, (2900,2900),linewidth=1, chipCentered=True,layer='MARKERS')
        
        for s in self.structures:
            s.shiftPos(340)

        doc = ezdxf.readfile(file_name)
        doc.header['$INSUNITS'] = 13 
        msp = doc.modelspace()

        entities = []
        for entity in msp:
            if entity.dxftype() == 'LINE':
                entities.append({
                    'type': 'line',
                    'start': entity.dxf.start,
                    'end': entity.dxf.end,
                    'color': entity.dxf.color,
                    'layer': entity.dxf.layer
                })
            elif entity.dxftype() == 'CIRCLE':
                entities.append({
                    'type': 'circle',
                    'center': entity.dxf.center,
                    'radius': entity.dxf.radius,
                    'color': entity.dxf.color,
                    'layer': entity.dxf.layer
                })
            elif entity.dxftype() == 'POLYLINE':
                pts = list(entity.points())
                pts.append(pts[0])
                entities.append({
                    'type': 'polyline',
                    'points': pts,
                    'color': entity.dxf.color,
                    'layer': entity.dxf.layer
                })
                print(entity.points())
        

        # new_drawing = dxf.drawing('new_output.dxf')

        # Add entities to the new drawing based on extracted data
        for entity in entities:
            if entity['type'] == 'line':
                self.add(dxf.line(
                    start=entity['start'],
                    end=entity['end'],
                    color=entity['color'],
                    layer=entity.dxf.layer
                ))
                
            elif entity['type'] == 'circle':
                self.add(dxf.circle(
                    center=entity['center'],
                    radius=entity['radius'],
                    color=entity['color'],
                    layer=entity.dxf.layer
                ))
            elif entity['type'] == 'polyline':
                layer = entity['layer']
                if layer == 'outercut':
                    layer = 'XOR'
                poly = dxf.polyline(
                    points=entity['points'],
                    color=entity['color'],
                    layer=layer,
                    bgcolor=self.wafer.bg(layer)
                )
                poly.POLYLINE_CLOSED = True
                poly.close()

                self.add(poly)

# Save the new drawing
        # new_drawing.save()

        


        
            # Add more types as needed

  
def overlap_junction_bilayer(chip,structure,jjw = 0.5, length=300,pad=300,gap=30,width=80,jsep=30,taperl=4,fingerw=0,
                             finger2w=None,leadw=None,offset=0,overlap=7,cdbias=0.0,secondlayer='SECONDLAYER', uc_width=0.7):   
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
    # CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    #overlap part
    # chip.add(dxf.rectangle(struct().getPos((-overlap/2,-offset+leadw/2)),finger2w,offset-leadw/2-fingerw/2,rotation=struct().direction,layer=secondlayer))
    # chip.add(dxf.rectangle(struct().getPos((-overlap/2-cdbias,-fingerw/2)),finger2w+2*cdbias,fingerw,rotation=struct().direction,layer=secondlayer))
    # chip.add(dxf.rectangle(struct().getPos((-overlap/2,fingerw/2)),finger2w,overlap-(offset-leadw/2-fingerw/2),rotation=struct().direction,layer=secondlayer))
    overhang = 5
    jpadw = 15
    jarmw = 3
    jtaperl=2-1.36-0.140
    jfingerl=1.36
    jgap = 0.2
    vshift = uc_width
    finger_diff = uc_width*5/4
    struct().translatePos((gap/2,0))
    DolanJunction(chip, struct(), junctionl=gap+uc_width, 
                  jpadoverhang = overhang, 
                  jfingerw = jjw + uc_width*1,
                  jfingerl = jfingerl,
                  jpadw=jpadw+uc_width*2,
                  JLAYER = secondlayer,
                  ULAYER  = secondlayer,
                  jarmw = jarmw + uc_width*2,
                  jtaperl=jtaperl+uc_width/2,
                  jgap = jgap,
                  vshift = -vshift,
                  finger_diff=finger_diff,
                  vert_offset=0)
    struct().translatePos((-gap/2-overhang*2-uc_width*3/2,0))
    DolanJunction(chip, struct(), junctionl=gap,
                  jgap = jgap, 
                  jpadoverhang = overhang, 
                  jfingerw = jjw , 
                  jpadw = jpadw,
                  jfingerl = jfingerl-uc_width,
                  jtaperl = jtaperl,
                  )
    # struct().translatePos((-gap/2,0))
    
    struct().translatePos((-overhang*2,0))
    sl2 = struct().cloneAlong((0,0))

    CPW_taper(chip,struct(),taperl,s0=gap+width/2-fingerw/2,w0=fingerw,w1=width,offset=(0,-offset/2))
    
    CPW_straight(chip,struct(), length/2-gap-jsep, w=width)
    
    # CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    CPW_stub_short(chip,struct(),flipped=True,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
    CPW_straight(chip,struct(),pad)
    CPW_stub_open(chip,struct(),flipped=False)

    Strip_straight(chip,sl2, -gap, w=width+2*gap)
    # Strip_taper(chip,sl2,taperl,w0=leadw,w1=width)
    # Strip_straight(chip,sl2,length/2-jsep,w=width)
    # Strip_straight(chip,sl2,pad,w=pad)
    
    # Strip_straight(chip,struct(), length/2-gap-jsep/2, w=width+2*gap)
    # Strip_stub_open(chip,struct(),flipped=True,w=pad+2*gap)
    # Strip_straight(chip,struct(),pad,w=pad+2*gap)
    # Strip_stub_open(chip,struct(),w=pad+2*gap)

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
    # CPW_straight(chip,struct(), length/2-gap-jsep, w=width)
    # CPW_taper(chip,struct(),taperl,s1=gap+width/2-fingerw/2,w1=fingerw,w0=width)
    # CPW_straight(chip,struct(),jsep/2-taperl+overlap/2,w=fingerw,s=gap+width/2-fingerw/2)
    #struct().translatePos((0,-offset))
    sl2 = struct().cloneAlong((-overlap,-fingerw/2-leadw/2+overlap))



    Strip_straight(chip,sl2, jsep/2-taperl+overlap, w=leadw)
    Strip_taper(chip,sl2,taperl,w0=leadw,w1=width,offset=(0,fingerw/2+leadw/2-overlap))
    Strip_straight(chip,sl2,length/2-jsep,w=width,)
    Strip_straight(chip,sl2,pad,w=pad,)
    
    Strip_straight(chip,struct(), length/2-gap-jsep/2, w=width+2*gap)
    Strip_stub_open(chip,struct(),flipped=True,w=pad+2*gap)
    Strip_straight(chip,struct(),pad,w=pad+2*gap)
    Strip_stub_open(chip,struct(),w=pad+2*gap)

'''
        #qubit parameters
        w_qubit = 30
        s_qubit = 30
        q_sep = 12
        q_length = 224
        q_overlap = 200
        #r_qubit = 24
        #junction parameters
        leadw=4.0
        finger2w=0.7
        joverlap=8.0
        taper_l = 4
        cdbias=0.2
'''


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


#=============================

class EtchTestChip(m.Chip7mm):
    def __init__(self,wafer,chipID,layer):
        m.Chip7mm.__init__(self,wafer,chipID,layer,defaults={'w':20, 's':10, 'radius':300,'r_out':10,'r_ins':10,'curve_pts':30})
        
        #DICING GRID SQUARE TO COVER WHOLE CHIP
        self.add(dxf.rectangle(self.center,6200,6200,halign=const.CENTER,valign=const.MIDDLE,layer='DICEGRID',bgcolor=self.wafer.bg('DICEGRID')))
        
        #optical markers
        doMirrored(MarkerSquare, self, (2900,2900),linewidth=1, chipCentered=True,layer='MARKERS')
        
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
        finger2w=2 #change this if 1st layer succeeds
        joverlap=6.0#8.0
        joverlap2=8.0
        taper_l = 4
        cdbias=0.0
        
        #junction contacts
        for q in range(5):    
            spacing = 460
            labelPos = (-40,-130)
            # labelPos2 = (-40,-150)
            #bottom left, upper right:
            for xy in [(250+q*spacing,100),(-250+(-4+q)*spacing,-400)]:
                sq1=m.Structure(self,self.centered(xy),direction=90)
                
                jjw =np.round(0.1+0.05*q,3)
                pad_len = 200
                pad = 150
                gap = 30
                length = 100

                sq1.defaults['w']=pad
                sq1.defaults['s']=gap
                sq1.defaults['r_out']=gap
                CPW_stub_open(self,sq1,flipped=True)
                CPW_straight(self,sq1,pad_len)
                CPW_stub_open(self,sq1,flipped=False)
    
                self.add(dxf.text(str(jjw),sq1.getLastPos(labelPos),height=60,layer='MARKERS'))
                overhang = 5
                sq1.shiftPos(-gap/2)
                DolanJunction(self, sq1, junctionl=gap, jpadoverhang = overhang, jfingerw = jjw )
                 #end qubit
                
            #bottom right, upper left
            for xy in [(-250+(-4+q)*spacing,100),(250+q*spacing,-400)]:
                sq1=m.Structure(self,self.centered(xy),direction=90)
                
                jjw =np.round(0.1+0.05*q,3)
                pad_len = 200
                pad = 150
                gap = 30
                length = 100

                sq1.defaults['w']=pad
                sq1.defaults['s']=gap
                sq1.defaults['r_out']=gap
                CPW_stub_open(self,sq1,flipped=True)
                CPW_straight(self,sq1,pad_len)
                CPW_stub_open(self,sq1,flipped=False)
    
                self.add(dxf.text(str(jjw),sq1.getLastPos(labelPos),height=60,layer='MARKERS'))
                overhang = 5
                sq1.shiftPos(-gap/2)
                DolanJunction(self, sq1, junctionl=gap, jpadoverhang = overhang, jfingerw = jjw )
                #end qubit
            
            gap = 30
            fingerw = 2
            #upper row
            s2=m.Structure(self,self.centered((250+q*spacing,1000)),direction=90)
            jjw =np.round(0.1+0.05*q,3)
            self.add(dxf.text(str(jjw)+'.',s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30, jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            s2=m.Structure(self,self.centered((-250-q*spacing,1000)),direction=90)
            
            
            jjw =np.round(0.2+0.05*q,3)
            self.add(dxf.text(str(jjw)+'.',s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30, jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            #bottom row
            
            jjw =np.round(0.3+0.05*q,3)
            s2=m.Structure(self,self.centered((250+q*spacing,-1000)),direction=90)
            self.add(dxf.text(str(jjw),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30, jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            s2=m.Structure(self,self.centered((-250-q*spacing,-1000)),direction=90)
            
            
            jjw =np.round(0.4+0.05*q,3)
            self.add(dxf.text(str(jjw),s2.getLastPos(labelPos),height=60,layer='MARKERS'))
            overlap_junction_bilayer(self,s2,fingerw=fingerw,finger2w=0,leadw=0,overlap=0, gap = 30,    jjw = jjw)
            # self.add(dxf.rectangle(s2.getLastPos((0,0)), 100, 100, layer='MARKERS'))
            
            
            
        
        #lines
        for j in range(28):
            #lower
            # self.add(dxf.rectangle(self.centered((0,-1600-14*j)),600,4.3,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((0,-1600-14*j-3)),600,2,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((0,-1600-14*j-6)),600,2.4,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((0,-1600-14*j-9)),600,2,layer='JUNCTION'))
            # upper
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j)),6000,4.3))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-3)),6000,2))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-6)),6000,2.4))
            self.add(dxf.rectangle(self.centered((-3000,1600+14*j-9)),6000,2))
            
        # lines
        for j in range(28):
            #bottom
            # self.add(dxf.rectangle(self.centered((0+14*j,-3000)),2,600,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((0+14*j+3,-3000)),2.4,600,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((0+14*j+6,-3000)),2,600,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((0+14*j+9,-3000)),4.3,600,layer='JUNCTION'))
            
            # self.add(dxf.rectangle(self.centered((2500-14*j,-3000)),2,1000,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((2500-14*j-3,-3000)),2.4,1000,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((2500-14*j-6,-3000)),2,1000,layer='JUNCTION'))
            # self.add(dxf.rectangle(self.centered((2500-14*j-9,-3000)),4.3,1000,layer='JUNCTION'))
            # top
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
        
        # for y in [-2500,2500]:
        #     srBar=m.Structure(self,self.centered((-pad_sep/2-pad/3-(N-1)*pad_sep/2,y)),defaults={'w':pad,'s':gap,'r_ins':50})
        #     Strip_stub_open(self,srBar,flipped=True,w=total_width,r_out=pad/3,length=pad_sep/2+pad/3)
        #     srBar2 = srBar.cloneAlong((0,total_width/2-gap),newDirection=-90)
        #     srBar2.defaults['r_out']=50
        #     srBar.translatePos((pad/2+gap,-total_width/2),90)
        #     for i in range(N):
        #         CPW_pad(self,srBar,pad,padw=pad,pads=gap,w=leadw,r_out=0,l_lead=(total_width/2-pad-gap-offset-leadw/2))
        #         CPW_straight(self, srBar, leadw, w=pad_sep/2+overlap,s=pad_sep/4-overlap/2)
        #         CPW_straight(self,srBar.cloneAlongLast(),leadw-fingerw,w=pad_sep/2-overlap,s=overlap)
        #         Strip_straight(self, srBar, total_width/2+offset-leadw/2, w=pad_sep)
        #         srBar.translatePos((-total_width,-pad_sep))
        #     srBar.translatePos((total_width/2,pad/2+gap),-90)
        #     Strip_stub_open(self,srBar,w=total_width,r_out=pad/3,length=pad_sep/2+pad/3)
        #     for i in range(N+1):
        #         Strip_pad(self,srBar2,pad,padw=pad,layer='SECONDLAYER')
        #         Strip_straight(self,srBar2,(total_width/2-pad-gap-offset-leadw/2),w=leadw,layer='SECONDLAYER')
        #         Strip_straight(self, srBar2, leadw, w=pad_sep/2,layer='SECONDLAYER')
        #         CPW_straight(self, srBar2, offset+overlap/2, w=pad_sep/2-2*fingerw,s=fingerw,layer='SECONDLAYER')
        #         srBar2.translatePos((-offset-overlap/2-leadw-(total_width/2-pad-gap-offset-leadw/2)-pad,pad_sep))
                
        #resistance bar
        gap=50
        pad=600
        length=1500
        width=40
        
        #top
        srBar=m.Structure(self,self.centered((2700,-length/2-pad-gap)),direction=90,defaults={'w':pad,'s':gap,'r_out':gap})
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        srBar2 = srBar.cloneAlong()
        Strip_straight(self,srBar,pad,w=pad+2*gap, )
        Strip_stub_open(self,srBar,flipped=False,w=pad+2*gap)
        Strip_straight(self, srBar, length-2*gap, w=width+2*gap)
        Strip_stub_open(self,srBar,flipped=True,w=pad+2*gap)
        Strip_straight(self,srBar,pad,w=pad+2*gap)
        Strip_stub_open(self,srBar,w=pad+2*gap)
        
        Strip_straight(self,srBar2,pad,w=pad,layer='JUNCTION2')
        Strip_straight(self, srBar2, length, w=width,layer='JUNCTION2')
        Strip_straight(self,srBar2,pad,w=pad,layer='JUNCTION2')

        
        #bottom
        srBar=m.Structure(self,self.centered((-2700,-length/2-pad-gap)),direction=90,defaults={'w':pad,'s':gap,'r_out':gap})
        CPW_stub_open(self,srBar,flipped=True)
        CPW_straight(self,srBar,pad)
        CPW_stub_short(self,srBar,flipped=False,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self, srBar, length-2*gap, w=width)
        CPW_stub_short(self,srBar,flipped=True,w=width,s=(pad+2*gap-width)/2,curve_ins=False)
        CPW_straight(self,srBar,pad)
        CPW_stub_open(self,srBar)
        
        
        
        #================== SECOND LAYER =========================
        
        #horizontal lines
        # for j in range(20):
        #     #bottom
        #     self.add(dxf.rectangle(self.centered((0,-3000+24*j+3)),400,1,layer='UNDERCUT'))
        #     self.add(dxf.rectangle(self.centered((0,-3000+24*j+12)),400,2,layer='UNDERCUT'))
            
            # self.add(dxf.rectangle(self.centered((2600,-3000+24*j+3)),-1000,1,layer='UNDERCUT'))
            # self.add(dxf.rectangle(self.centered((2600,-3000+24*j+12)),-1000,2,layer='UNDERCUT'))
            # #top
            # self.add(dxf.rectangle(self.centered((-2600,3000-24*j-3)),1000,-1,layer='UNDERCUT'))
            # self.add(dxf.rectangle(self.centered((-2600,3000-24*j-12)),1000,-2,layer='UNDERCUT'))
            
            
        # #vertical lines
        # for j in range(25):
        #     #bottom
        #     self.add(dxf.rectangle(self.centered((0+24*j+3,-1590)),1,-400,layer='UNDERCUT'))
        #     self.add(dxf.rectangle(self.centered((0+24*j+12,-1590)),2,-400,layer='UNDERCUT'))
            # #top
            # self.add(dxf.rectangle(self.centered((-3000+24*j+3,1590)),1,400,layer='UNDERCUT'))
            # self.add(dxf.rectangle(self.centered((-3000+24*j+12,1590)),2,400,layer='UNDERCUT'))


  

jarrayChip2 = EtchTestChip(w,'JARRAY','BASEMETAL')
jarrayChip2.save(w,drawCopyDXF=True,dicingBorder=False)

file_name = 'resonators.dxf'
    
jarrayChip1 = EtchTestChip(w,'JARRAY','BASEMETAL',)
waffle(jarrayChip1, 100, width=20,bleedRadius=1,padx=700,layer='MARKERS', exclude=['BASEMETAL','SECONDLAYER'])
jarrayChip1.save(w,drawCopyDXF=True,dicingBorder=False)

ResonatorChip1 = ResonatorChip(w,'XOR','XOR', file_name = 'resonators.dxf')
# ResonatorChip1 = waffle(ResonatorChip1, 100, width=20,bleedRadius=1,padx=700,layer='MARKERS', exclude=['DICEGRID'])
ResonatorChip1.save(w,drawCopyDXF=True,dicingBorder=False)


# sqr = ResonatorChip(w,'XOR1','XOR1', file_name = 'sqr.dxf')
# sqr.save(w,drawCopyDXF=True,dicingBorder=False)

# zql = ResonatorChip(w,'XOR2','XOR2', file_name = '/Users/wendy/Desktop/masklib code/ Ziqian_pixel.dxf')
# zql.save(w,drawCopyDXF=True,dicingBorder=False)


XSearchChip = QSearchChip6(w,'XSEARCH','BASEMETAL')
XSearchChip = waffle(XSearchChip, 500, width=100,bleedRadius=1,padx=700,layer='MARKERS', exclude=['FRAME','DICEGRID'])
XSearchChip.save(w,drawCopyDXF=True,dicingBorder=False,center=True)

#XInverseChip = InverseQSearchChip6(w,'XINVERSE','XOR2')
#waffle(XInverseChip, 100, width=20,bleedRadius=1,padx=700,layer='XOR2',exclude=['BASEMETAL','SECONDLAYER'])
#XInverseChip.save(w,drawCopyDXF=True,dicingBorder=False,center=True)

#optical markers
doMirrored(MarkerSquare, w, (15000,15000), layer='MARKERS')
doMirrored(MarkerSquare, w, (16000,15000), layer='MARKERS')


for i in range(len(w.chips)):
    x,y = w.chipPts[i]
    if i in [0,6,14]:
        # w.chips[i]=zql
        pass
    elif i in [84,96,106]:
        # w.chips[i]=sqr
        pass
    elif i %2 == 0:
        w.chips[i]=ResonatorChip1
    elif i %2 == 1:
        w.chips[i]=jarrayChip1
    
    else:
        w.chips[i]=XSearchChip
    w.add(dxf.text(str(i),vadd(w.chipPts[i],(5400,6100)),height=600,layer='MARKERS'))
    w.add(dxf.text('NbSi1',vadd(w.chipPts[i],(1200,6600)),height=600,layer='LABEL1'))
        # w.add(dxf.text('NANJ02',vadd(w.chipPts[i],(1200,6600)),height=600,layer='LABEL2'))





# for i in [5,12,19,26]:
#     w.chips[i]=XSearchChip
    

# write all chips
w.populate()
w.save()