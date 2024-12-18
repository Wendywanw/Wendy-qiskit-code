import numpy as np
import astropy.units as u
from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary.core import QComponent

# to use the airbridge component, you need to add the following lines into qiskit-metal/qiskit_metal/qlibrary/tlines/anchored_path.py
# line 190:
# elif 'air' in component:
#                continue
# NOTE: the name of your airbridge component must contain 'air' in it.


def equals(a,b):
    ''' Check if two numbers are equal within 1e-6 tolerance. '''
    return abs(a-b)<1e-6
def find_line_direction(p1,p2):
    ''' Find the direction of a line from p1 to p2.'''
    x1,y1 = p1
    x2,y2 = p2
    if x1 == x2:
        if y1>y2:
            return 270
        elif y1<y2:
            return 90
        else:
            return 0
    elif equals(y1, y2):
        if x1>x2:
            return 180
        elif x1<x2:
            return 0
        else: return 0
    else:
        return ((np.arctan((y2-y1)/(x2-x1))*180/np.pi)+360)%360
def find_segment_length(p1,p2, type):
    ''' Find the length of a line from p1 to p2. 
    when the type is arc, it calculates the arc length'''
    x1,y1 = p1
    x2,y2 = p2
    d1 = np.absolute(x2-x1)
    d2 = np.absolute(y2-y1)
    if type == 'straight':
        return np.sqrt(d1**2+d2**2)
    elif equals(d1, d2) and (type == 'arc'):
        # print('arc!')
        return d1*np.pi/2
    else:
        r = max(d1, d2)
        r_min = min(d1, d2)
        theta = np.arctan(r_min/r)
        return d1*theta/2
def find_coordinates(coordinates, r):
    ''' Breaks the coordinates of cpw into segments and find the start, end, length, angle, type of each segment.'''
    segment_start = []
    segment_end = []
    segment_type = []
    segment_angle = []
    segment_length = []
    seg_all = []
    clockwise = []

    cor = np.array(coordinates)
    if np.all(cor[:,1] == cor[:,1][0]) or np.all(cor[:,0] == cor[:,0][0]):
        segment_start = [coordinates[0]]
        segment_end = [coordinates[-1]]
        segment_type = ['straight']
        segment_angle = [find_line_direction(coordinates[0],coordinates[-1])]
        segment_length = [find_segment_length(coordinates[0],coordinates[-1], type = 'straight')]
        clockwise = [0]
        segment = {}
        segment['start'] = segment_start
        segment['end'] = segment_end
        segment['angle'] = segment_angle
        segment['length'] = segment_length
        segment['type'] = segment_type
        segment['clockwise'] = clockwise
        return segment


    for i, cords in enumerate(coordinates):
        
        if i ==0:
            seg_all.append(coordinates[i])
            segment_start.append(coordinates[i])
            continue
        if i == len(coordinates)-1:
            if len(segment_start)==1:
                seg_all.append(coordinates[i])
            # seg_all.append(coordinates[i-1])
            else:
                seg_all.append(coordinates[i])
                segment_start.append(segment_end[-1])
            segment_end.append(coordinates[i])
            segment_type.append('straight')
            angle = find_line_direction(coordinates[i-1],coordinates[i])
            length = find_segment_length(coordinates[i-1],coordinates[i], type = 'straight')
            segment_length.append(length)
            segment_angle.append(angle)
            clockwise.append(0)
            break
        angle = find_line_direction(coordinates[i-1],cords)
        next_angle = find_line_direction(cords,coordinates[i+1])
        # print(angle, next_angle, coordinates[i-1], cords, coordinates[i+1])
        # print(angle, next_angle)
        # print(np.absolute(angle-next_angle))
        if angle == next_angle:
            continue
        elif np.absolute(angle-next_angle)%90==0:
            x, y = cords
            x0,y0 = coordinates[i-1]
            x_modi = x - np.sign(x - x0)*r
            y_modi = y - np.sign(y - y0)*r
            if i == 1:
                pass
            else:
                segment_start.append(segment_end[-1])
            segment_end.append((x_modi,y_modi))
            segment_type.append('straight')
            segment_angle.append(angle)
            length = find_segment_length(segment_start[-1],segment_end[-1], type = 'straight')
            segment_length.append(length)
            clockwise.append(0)


            x1,y1 = coordinates[i+1]
            x1_modi = x + np.sign(x1 - x)*r
            y1_modi = y + np.sign(y1 - y)*r
            segment_start.append((x_modi,y_modi))
            segment_end.append((x1_modi,y1_modi))
            segment_type.append('arc')
            c = -np.sign(x1_modi-x_modi)*np.sign(y1_modi-y_modi)*(-1)**(angle//90)
            clockwise.append(c)
            angle = (angle-c*45+360)%360
            segment_angle.append(angle)
            length = find_segment_length(segment_start[-1],segment_end[-1], type = 'arc')
            segment_length.append(length)

            # seg_all.append(coordinates[i-1])
            seg_all.append((x_modi,y_modi))
            seg_all.append((x1_modi,y1_modi))
    segment = {}
    segment['start'] = segment_start
    segment['end'] = segment_end
    segment['angle'] = segment_angle
    segment['length'] = segment_length
    segment['type'] = segment_type
    segment['clockwise'] = clockwise

    return segment    
def make_ab_element(design,cpw,arc_bridge = False):
    ''' Make the airbridge element using the cpw parameters.'''
    r = design.parse_value(cpw.options.fillet)
    center_pin = design.parse_value(cpw.options.trace_width)
    gap_w = design.parse_value(cpw.options.trace_gap)

    xover_len = center_pin + 2.1*gap_w
    box_side = 0
    xover_width = 0
    box_height = 0
    if 0.05<=xover_len<=0.016:
        xover_width = 0.005
        box_side = xover_width+0.0005
        box_height = box_side-0.0005
    elif 0.016<xover_len<=0.027:
        xover_width = 0.0075
        box_side = xover_width+0.003
        box_height = box_side-0.0005
    elif 0.027<xover_len<=0.032:
        xover_width = 0.01
        box_side = xover_width+0.0005
        box_height = box_side-0.0005
    else:
        print('error!!!')
    out_box_len = box_side + 0.0015*2
    out_box_height = box_height + 0.0015*2
    r_in = r-center_pin/2-gap_w
    if r_in < out_box_len:
        # print('error!!!')
        pass
    else:
        ab_inside_extend = r_in - np.sqrt(r_in**2 - out_box_len**2)

        
    square_in = draw.rectangle(box_height, box_side)
    square_out = draw.rectangle(out_box_height, out_box_len)
    squares = [square_in, square_out]
    sq_in_left, sq_out_left = draw.translate(squares,-xover_len/2-out_box_height/2,0)
    sq_in_right, sq_out_right = draw.translate(squares,xover_len/2+out_box_height/2,0)
    
    if arc_bridge == True:
        xover_rec = draw.rectangle(xover_len+ ab_inside_extend, xover_width )
        sq_in_right, sq_out_right = draw.translate([sq_in_right, sq_out_right],
                                                ab_inside_extend/2,0)
        base = draw.shapely.unary_union((sq_out_left, xover_rec, sq_out_right))
    else:
        xover_rec = draw.rectangle(xover_len, xover_width)
        base = draw.shapely.unary_union((sq_out_left, xover_rec, sq_out_right))

    top = draw.shapely.unary_union((sq_in_left, sq_in_right))
    return top, base, xover_len, out_box_len

def find_next_ab(segment_all, distance, ab_all, cpw_turn_radi, start_early, start_early_buffer = 0.0005, clockwise = 1):
    ''' Find the next airbridge coordinate on the CPW given a previous one.'''
    last_pt = ab_all['coord'][-1]
    last_len = ab_all['length_remain'][-1]
    seg_num = ab_all['seg_num'][-1]
    smaller = True
    last_angle = segment_all['angle'][seg_num]
    if start_early:
        if segment_all['type'][seg_num+1]=='arc':
            seg_num += 1
        angle = segment_all['angle'][seg_num+1]/180*np.pi
        x, y  = segment_all['start'][seg_num+1]
        x += np.cos(angle)*start_early_buffer
        y += np.sin(angle)*start_early_buffer
        ab_all['coord'].append((x,y))
        ab_all['length_remain'].append(segment_all['length'][seg_num+1]-start_early_buffer)
        ab_all['seg_num'].append(seg_num+1)
        clockwise = segment_all['clockwise'][seg_num]
        ab_all['angle'].append(segment_all['angle'][seg_num+1])#+180*clockwise)
        ab_all['inside_extend'].append(False)
        return ab_all, True, False
    if last_len >= (distance):
        if (last_len-distance)<start_early_buffer*2:
            # ab_all['seg_num'][-1] = seg_num
            # print(seg_num<len(segment_all['angle']))
            return ab_all, seg_num<(len(segment_all['angle'])-1), True
        ab_all['length_remain'].append(last_len-distance)
        ab_all['seg_num'].append(seg_num)
        x,y = last_pt
        if segment_all['type'][seg_num] == 'straight':
            angle = last_angle/180*np.pi
            x_new = x + distance*np.cos(angle)
            y_new = y + distance*np.sin(angle)
            
            angle = angle*180/np.pi
            ab_all['angle'].append(angle)
            ab_all['inside_extend'].append(False)
            start_x, start_y = segment_all['start'][seg_num]
            actual_start_x = start_x + np.cos(np.radians(last_angle))*start_early_buffer
            actual_start_y = start_y + np.sin(np.radians(last_angle))*start_early_buffer

            end_x, end_y = segment_all['end'][seg_num]
            actual_end_x = end_x - np.cos(np.radians(last_angle))*start_early_buffer
            actual_end_y = end_y - np.sin(np.radians(last_angle))*start_early_buffer
            if actual_start_x<=x_new<end_x or actual_start_x>=x_new>end_x:
                if actual_start_y<y_new<end_y or actual_start_y>y_new>end_y:
                    pass
                elif actual_start_y<=y_new<start_y or actual_start_y>=y_new>start_y:
                    y_new = actual_start_y
                elif actual_end_y<=y_new<end_y or actual_end_y>=y_new>end_y:
                    y_new = actual_end_y
            elif actual_start_y<=y_new<end_y or actual_start_y>=y_new>end_y:
                if actual_start_x<=x_new<start_x or actual_start_x>=x_new>start_x:
                    x_new = actual_start_x
                elif actual_end_x<=x_new<end_x or actual_end_x>=x_new>end_x:
                    x_new = actual_end_x
            ab_all['coord'].append((x_new,y_new))
            return ab_all, True, False
        else:
            ab_all['length_remain'][-1] = 0
            ab_all['seg_num'][-1] = seg_num
            start_early = True
            return ab_all, True, True
    elif int(seg_num) == int(len(segment_all['type'])-1):
        return ab_all, False, False
        
    else:
        # print(segment_all, seg_num)
        smaller = True
        len_needed = distance-last_len+0.1
        while smaller:
            # print(seg_num, len_needed)
            seg_num += 1
            next_len = segment_all['length'][seg_num]
            if next_len >= len_needed:
                break
            elif (next_len < len_needed) and (seg_num == len(segment_all['type'])-1):
                # print(ab_all, segment_all)
                return ab_all, False, False
            else:
                len_needed -= next_len
        if (next_len-len_needed)<start_early_buffer:
            # print(seg_num<len(segment_all['angle']))
            return ab_all, seg_num<(len(segment_all['angle'])-1), True
        ab_all['seg_num'].append(seg_num)
        ab_all['length_remain'].append(next_len-len_needed)
        # print(next_len-len_needed,seg_num)
        x0, y0 = segment_all['start'][seg_num]
        last_angle = segment_all['angle'][seg_num]
        if segment_all['type'][seg_num] == 'straight':
            angle = last_angle/180*np.pi
            x_new = x0 + len_needed*np.cos(angle)+start_early_buffer*np.cos(angle)
            y_new = y0 + len_needed*np.sin(angle)+start_early_buffer*np.sin(angle)
            
            angle = angle*180/np.pi
            ab_all['angle'].append(angle)
            ab_all['inside_extend'].append(False)

            start_x, start_y = segment_all['start'][seg_num]
            actual_start_x = start_x + np.cos(np.radians(last_angle))*start_early_buffer
            actual_start_y = start_y + np.sin(np.radians(last_angle))*start_early_buffer

            end_x, end_y = segment_all['end'][seg_num]
            actual_end_x = end_x - np.cos(np.radians(last_angle))*start_early_buffer
            actual_end_y = end_y - np.sin(np.radians(last_angle))*start_early_buffer
            if actual_start_x<=x_new<end_x or actual_start_x>=x_new>end_x:
                if actual_start_y<=y_new<=actual_end_y or actual_start_y>=y_new>=actual_end_y:
                    pass
                elif actual_start_y<y_new<start_y or actual_start_y>y_new>start_y:
                    y_new = actual_start_y
                elif actual_end_y<y_new<end_y or actual_end_y>y_new>end_y:
                    y_new = actual_end_y
            elif actual_start_y<=y_new<=actual_end_y or actual_start_y>=y_new>=actual_end_y:
                if actual_start_x<x_new<start_x or actual_start_x>x_new>start_x:
                    x_new = actual_start_x
                elif actual_end_x<x_new<end_x or actual_end_x>x_new>end_x:
                    x_new = actual_end_x
            ab_all['coord'].append((x_new,y_new))
            return ab_all, True, False
        else:
            ab_all['length_remain'][-1] = 0
            ab_all['seg_num'][-1] = seg_num
            start_early = True
            # print(ab_all)

            return ab_all, True, True
def ab_placement(top, base, coord, angle):
    ''' Place the airbridge on the CPW.'''
    angle_in_data = angle
    base_new = base
    top_new = top

    pos = coord
    x, y = pos
    base_new = draw.translate(base_new, x, y, overwrite=False)
    top_new = draw.translate(top_new, x, y, overwrite=False)

    rotation_angle = -(90-angle_in_data)
    base_new = draw.rotate(base_new, rotation_angle, overwrite=False)
    top_new = draw.rotate(top_new, rotation_angle, overwrite=False)

    
    return top_new, base_new
def anti_collision(ab, box_side, xover_len, coord_all,start_early_buffer):
    ''' Check if the airbridge is too close to the CPW and adjust the position.'''
    min_distance = 0.01
    x,y = ab['coord'][-1]
    angle = ab['angle'][-1]
    seg_num = ab['seg_num'][-1]
    along_diff = box_side*2 + xover_len + min_distance
    side_diff = box_side + min_distance
    if angle%180==0:
        bol = [(i % 180 == 0) for i in ab['angle']]
        coords = np.array(ab['coord'])[bol]
        for xy in coords:
            x0 = xy[0]
            y0 = xy[1]
            
            if equals(x,x0):
                continue
            elif np.absolute(y-y0)>along_diff:
                continue
            elif np.absolute(x-x0)>side_diff:
                continue
            else:
                # print('changex!')
                # print(np.absolute(y-y0), np.absolute(x-x0))
                df = x-x0
                change_needed = np.absolute(side_diff) - np.absolute(df)
                x += change_needed*np.sign(df)
                x_start, y_start = coord_all['start'][seg_num]
                seg_angle = coord_all['angle'][seg_num]
                x_start += np.cos(np.radians(seg_angle))*box_side
                x_end, y_end = coord_all['end'][seg_num]
                x_end -= np.cos(np.radians(seg_angle))*box_side
                if x_start<x<x_end or x_end<x<x_start:
                    ab['length_remain'][-1] -= change_needed*2
                    ab['coord'][-1] = (x,y)
                    # print(x,y)
                    return ab, True, False
                elif x_start<x_end<x or x_start>x_end>x:
                    ab['coord'] = ab['coord'][:-1]
                    ab['length_remain'] = ab['length_remain'][:-1]
                    ab['angle'] = ab['angle'][:-1]
                    ab['seg_num'] = ab['seg_num'][:-1]
                    ab['inside_extend'] = ab['inside_extend'][:-1]
                    
                    if (seg_num+1)>len(coord_all['length']):
                        return ab, False, False
                    else:
                        return ab, True, True
                else:
                    x_new = x0+np.cos(seg_angle)*box_side
                    len_remain = coord_all['length'][seg_num]-np.absolute(coord_all['start'][seg_num][0] - x_new)
                    ab['coord'].append((x_new, y))
                    ab['length_remain'].append(len_remain)
                    ab['angle'].append(seg_angle)
                    ab['seg_num'].append(seg_num)
                    ab['inside_extend'].append(False)
                    return ab, True, False

    else:
        bol = [(i % 180 != 0) for i in ab['angle']]
        coords = np.array(ab['coord'])[bol]
        a = x
        x = y
        y = a
        for xy in coords:
            x0 = xy[1]
            y0 = xy[0]
            if equals(x,x0) or equals(y,y0):
                continue
            elif np.absolute(y-y0)>along_diff:
                continue
            elif np.absolute(x-x0)>side_diff:
                continue
            else:
                df = x-x0
                # print(df)
                # print('y',x,'y0',x0, side_diff)
                change_needed = np.absolute(side_diff) - np.absolute(df)
                # print('change needed', change_needed)
                x += change_needed*np.sign(df)
                y_start, x_start = coord_all['start'][seg_num]
                seg_angle = coord_all['angle'][seg_num]
                x_start += np.sin(np.radians(seg_angle))*box_side
                y_end, x_end = coord_all['end'][seg_num]
                x_end -= np.sin(np.radians(seg_angle))*box_side
                if x_start<x<x_end or x_end<x<x_start:
                    ab['length_remain'][-1] -= change_needed
                    ab['coord'][-1] = (y,x)
                    # print(y,x, change_needed)
                    return ab, True, False
                elif x_start<x_end<x or x_start>x_end>x:
                    
                    ab['coord'] = ab['coord'][:-1]
                    ab['length_remain'] = ab['length_remain'][:-1]
                    ab['angle'] = ab['angle'][:-1]
                    ab['seg_num'] = ab['seg_num'][:-1]
                    ab['inside_extend'] = ab['inside_extend'][:-1]
                    if (seg_num+1)>len(coord_all['length']):
                        return ab, False, False
                    else:
                        return ab, True, True
                else:
                    x_new = x0+np.cos(seg_angle)*box_side
                    len_remain = coord_all['length'][seg_num]-np.absolute(coord_all['start'][seg_num][0] - x_new)
                    ab['coord'].append((y, x_new))
                    ab['length_remain'].append(len_remain)
                    ab['angle'].append(seg_angle)
                    ab['seg_num'].append(seg_num)
                    ab['inside_extend'].append(False)
                    return ab, True, False
    return ab, True, False




class airbridges(QComponent):
    ''' A components that draws airbridges on the CPW.
    
    Inherits QComponent class.

    Default Options:
        cpw_name = 'cpw_1', -- name of the cpw to draw airbridges on
        distance = '70um', -- distance between airbridges
        layer_ab_square = '5', -- layer of the square part of the airbridge
        layer_ab = '4', -- layer of the airbridge
        chip = 'main', 
        seg_num = '0', -- segment number of the cpw to start drawing airbridges
        dis = '5um', -- Minimum distance between airbridges
        
        '''
    default_options = Dict(
        cpw_name = 'cpw_1',
        distance = '70um',
        layer_ab_square = '5',
        layer_ab = '4',
        chip = 'main', 
        seg_num = '0',
        dis = '5um',)
    component_metadata = Dict(short_name='Airbridge',
                              _qgeometry_table_path='True',
                              _qgeometry_table_poly='True',
                              _qgeometry_table_junction='False')
    TOOLTIP = """Airbridges for cpws. """
 
    def make(self):
        p = self.p
        dis = p.distance
        d = p.dis
        design = self.design
        cpw = self.design.components[p.cpw_name]
        path = cpw.qgeometry_table('path')['geometry'].values[0]
        coordinates = path.coords[:]
        ab_top, ab_bot, xover_len, box_side = make_ab_element(design,cpw)
        r = design.parse_value(cpw.options.fillet)

        #specify the first airbridge coordinate on the CPW
        ab = {}
        x0, y0 = coordinates[0]
        
        seg_num = int(p.seg_num)
        ab['seg_num'] = [seg_num]
        segment = find_coordinates(coordinates, r)
        angle = segment['angle'][seg_num]
        if segment['type'][seg_num] == 'straight':
            ab['angle'] = [angle]
            flag = False
        else:
            ab['angle'] = [angle-45+(d/r)*180/np.pi]
            flag = True
        length_remaining = segment['length'][seg_num] - d
        if length_remaining<0:
            pass
        ab['length_remain'] = [length_remaining]
        ab['inside_extend'] = [flag]
        x0 += d*np.cos(angle/180*np.pi)
        y0 += d*np.sin(angle/180*np.pi)
        ab['coord'] = [(x0,y0)]


        #get all the airbridge coordinates
        test = True
        start_early = False
        while test:
            
            ab, test, start_early = find_next_ab(segment, dis, ab, r, start_early, start_early_buffer = box_side/2)
            if not (test):
                break
            elif start_early:
                continue
            else:
                
                cc= anti_collision(ab,box_side,xover_len, segment,box_side)
                # print(cc,' a')
                ab, test,start_early  = cc

        #remove bridges that is placed outside of the CPW
        cor = np.array(coordinates)
        max_x = max(cor[:,0])
        min_x = min(cor[:,0])
        max_y = max(cor[:,1])
        min_y = min(cor[:,1])

        for i in range(len(ab['coord'])):
            x, y = ab['coord'][i]
            if x>max_x or x<min_x or y>max_y or y<min_y:
                ab['coord'][i] = None
                ab['length_remain'][i] = None
                ab['angle'][i] = None
                ab['seg_num'][i] = None
                ab['inside_extend'][i] = None


        #place the airbridges:
        for i in range(len(ab['coord'])):
            if ab['coord'][i] == None:
                continue
            angle = ab['angle'][i]
            coord = ab['coord'][i]
            if ab['inside_extend'][i]:
                pass
            else:
                top, base = ab_placement(ab_top, ab_bot, coord, angle)
            if i==0:
                top_all = top
                base_all = base
            else:
                top_all = draw.shapely.unary_union((top_all, top))
                base_all = draw.shapely.unary_union((base, base_all))


        #draw the airbridges
        self.add_qgeometry('poly',
                           dict(top_j=top_all),
                           chip=p.chip, layer = p.layer_ab_square)
        self.add_qgeometry('poly',
                           dict(bot_j=base_all),
                           chip=p.chip, layer = p.layer_ab)

        