import sys
sys.path.append('Customized_Components')

from rounded_single_pad import Round_TransmonPocket_Single

from qiskit_metal.qlibrary.couplers.coupled_line_tee import CoupledLineTee

from qiskit_metal.qlibrary.tlines.mixed_path import RouteMixed

from qiskit_metal.qlibrary.tlines.anchored_path import RouteAnchors

from short_line_Segment import ShortRoute

from qiskit_metal.qlibrary.terminations.launchpad_wb import LaunchpadWirebond

from dolan_junction import DolanJunction

from Airbridge import airbridges

from qiskit_metal import designs, MetalGUI

design = designs.DesignPlanar()

gui = MetalGUI(design)


wb_left0 = LaunchpadWirebond(
design,
name='wb_left0',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 270,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-3.4mm',
 'pos_y': '4.8mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left1 = LaunchpadWirebond(
design,
name='wb_left1',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '3.4mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left2 = LaunchpadWirebond(
design,
name='wb_left2',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '2.55mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left3 = LaunchpadWirebond(
design,
name='wb_left3',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '1.6999999999999997mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left4 = LaunchpadWirebond(
design,
name='wb_left4',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '0.8499999999999998mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left5 = LaunchpadWirebond(
design,
name='wb_left5',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '-2.220446049250313e-16mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left6 = LaunchpadWirebond(
design,
name='wb_left6',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '-0.8500000000000002mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left7 = LaunchpadWirebond(
design,
name='wb_left7',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '-1.7000000000000002mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left8 = LaunchpadWirebond(
design,
name='wb_left8',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '-2.5500000000000003mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_left9 = LaunchpadWirebond(
design,
name='wb_left9',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 0,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '-4.8mm',
 'pos_y': '-3.4000000000000004mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right0 = LaunchpadWirebond(
design,
name='wb_right0',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 270,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '3.4mm',
 'pos_y': '4.8mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right1 = LaunchpadWirebond(
design,
name='wb_right1',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '3.4mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right2 = LaunchpadWirebond(
design,
name='wb_right2',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '2.55mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right3 = LaunchpadWirebond(
design,
name='wb_right3',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '1.6999999999999997mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right4 = LaunchpadWirebond(
design,
name='wb_right4',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '0.8499999999999998mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right5 = LaunchpadWirebond(
design,
name='wb_right5',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '-2.220446049250313e-16mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right6 = LaunchpadWirebond(
design,
name='wb_right6',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '-0.8500000000000002mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right7 = LaunchpadWirebond(
design,
name='wb_right7',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '-1.7000000000000002mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right8 = LaunchpadWirebond(
design,
name='wb_right8',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '-2.5500000000000003mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




wb_right9 = LaunchpadWirebond(
design,
name='wb_right9',
options={'layer': '5',
 'lead_length': '8um',
 'orientation': 180,
 'pad_gap': '50um',
 'pad_height': '100um',
 'pad_width': '200um',
 'pos_x': '4.8mm',
 'pos_y': '-3.4000000000000004mm',
 'taper_height': '50um',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad922 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad922',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': -90,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-4.34',
 'pos_y': '4.5',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction846 = DolanJunction(
design,
name='dolan_junction846',
options={'Lj': '8',
 'layer': 2,
 'orientation': -90,
 'pos_x': -4.463,
 'pos_y': 4.5},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee232 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee232',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': -90,
 'pos_x': '-3.9',
 'pos_y': '4.171',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path626 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path626',
options={'_actual_length': '3.6146211184307715 '
                   'mm',
 'anchors': {0: (-4.091, 4.251),
             1: (-4.5889999999999995,
                 4.251),
             2: (-4.5889999999999995,
                 4.749),
             3: (-4.091, 4.749),
             4: (-4.035, 4.195),
             5: (-4.59, 4.195),
             6: (-4.59,
                 4.111000000000001),
             7: (-4.035,
                 4.111000000000001)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge819 = airbridges(
design,
name='Airbridge819',
options={'cpw_name': 'cpw_(0,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad796 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad796',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-3.1',
 'pos_y': '4.3',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction188 = DolanJunction(
design,
name='dolan_junction188',
options={'layer': 2,
 'orientation': -180,
 'pos_x': -3.1,
 'pos_y': 4.4425},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee440 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee440',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '-3.4675000000000002',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path77 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path77',
options={'_actual_length': '4.167421118430774 '
                   'mm',
 'anchors': {0: (-3.3875, 4.0125),
             1: (-3.3875,
                 4.5874999999999995),
             2: (-2.8125,
                 4.5874999999999995),
             3: (-2.8125, 4.0125),
             4: (-3.4435000000000002,
                 3.9565),
             5: (-3.4435000000000002,
                 4.5935),
             6: (-3.5275000000000003,
                 4.5935),
             7: (-3.5275000000000003,
                 3.9565)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge338 = airbridges(
design,
name='Airbridge338',
options={'cpw_name': 'cpw_(1,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path844 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path844',
options={'_actual_length': '0.5506238898038472 '
                   'mm',
 'anchors': {0: (-3.9, 3.8)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,0)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge697 = airbridges(
design,
name='Airbridge697',
options={'cpw_name': '(1,0)CPW(0,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad752 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad752',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-2.2',
 'pos_y': '4.26',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction291 = DolanJunction(
design,
name='dolan_junction291',
options={'Lj': '8',
 'layer': 2,
 'orientation': -180,
 'pos_x': -2.2,
 'pos_y': 4.3925},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee470 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee470',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '-2.5375',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path400 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path400',
options={'_actual_length': '3.716001118430776 '
                   'mm',
 'anchors': {0: (-2.4575,
                 4.0024999999999995),
             1: (-2.4575000000000005,
                 4.5175),
             2: (-1.9425000000000003,
                 4.5175),
             3: (-1.9425000000000003,
                 4.0024999999999995),
             4: (-2.5135,
                 3.9464999999999995),
             5: (-2.5135, 4.5085),
             6: (-2.5975, 4.5085),
             7: (-2.5975,
                 3.9464999999999995)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge588 = airbridges(
design,
name='Airbridge588',
options={'cpw_name': 'cpw_(2,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment249 = ShortRoute(
design,
name='short_line_Segment249',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(2,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge364 = airbridges(
design,
name='Airbridge364',
options={'cpw_name': '(2,0)CPW(1,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad850 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad850',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-1.3',
 'pos_y': '4.2299999999999995',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction290 = DolanJunction(
design,
name='dolan_junction290',
options={'Lj': '13',
 'layer': 2,
 'orientation': -180,
 'pos_x': -1.3,
 'pos_y': 4.353999999999999},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee660 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee660',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '-1.0515',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path564 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path564',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-1.5525,
                 3.977499999999999),
             1: (-1.5525,
                 4.482499999999999),
             2: (-1.0475, 4.4825),
             3: (-1.0475,
                 3.977499999999999),
             4: (-1.6085, 3.9215),
             5: (-1.6085,
                 4.538499999999999),
             6: (-0.9915, 4.5385),
             7: (-0.9915, 3.9215)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge445 = airbridges(
design,
name='Airbridge445',
options={'cpw_name': 'cpw_(3,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment190 = ShortRoute(
design,
name='short_line_Segment190',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(3,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge3 = airbridges(
design,
name='Airbridge3',
options={'cpw_name': '(3,0)CPW(2,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad972 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad972',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.4000000000000001',
 'pos_y': '4.26',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction362 = DolanJunction(
design,
name='dolan_junction362',
options={'Lj': '8',
 'layer': 2,
 'orientation': -180,
 'pos_x': -0.4000000000000001,
 'pos_y': 4.3975},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee31 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee31',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '-0.7425',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path417 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path417',
options={'_actual_length': '3.8223611184307775 '
                   'mm',
 'anchors': {0: (-0.6625000000000001,
                 3.9974999999999996),
             1: (-0.6625000000000001,
                 4.5225),
             2: (-0.13750000000000012,
                 4.5225),
             3: (-0.1375,
                 3.9974999999999996),
             4: (-0.7185,
                 3.9414999999999996),
             5: (-0.7185000000000001,
                 4.5365),
             6: (-0.8025000000000002,
                 4.5365),
             7: (-0.8025,
                 3.9414999999999996)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge539 = airbridges(
design,
name='Airbridge539',
options={'cpw_name': 'cpw_(4,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment680 = ShortRoute(
design,
name='short_line_Segment680',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(4,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge99 = airbridges(
design,
name='Airbridge99',
options={'cpw_name': '(4,0)CPW(3,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad160 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad160',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '0.49999999999999994',
 'pos_y': '4.25',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction527 = DolanJunction(
design,
name='dolan_junction527',
options={'Lj': '13',
 'layer': 2,
 'orientation': -180,
 'pos_x': 0.49999999999999994,
 'pos_y': 4.395},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee378 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee378',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '0.7669999999999999',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path310 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path310',
options={'_actual_length': '4.571361118430774 '
                   'mm',
 'anchors': {0: (0.22900000000000004,
                 3.979),
             1: (0.22899999999999993,
                 4.521),
             2: (0.7709999999999999,
                 4.521),
             3: (0.7709999999999999,
                 3.979),
             4: (0.173, 3.923),
             5: (0.17299999999999988,
                 4.577),
             6: (0.8269999999999998,
                 4.577),
             7: (0.827, 3.923)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge933 = airbridges(
design,
name='Airbridge933',
options={'cpw_name': 'cpw_(5,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment547 = ShortRoute(
design,
name='short_line_Segment547',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(5,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge75 = airbridges(
design,
name='Airbridge75',
options={'cpw_name': '(5,0)CPW(4,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad930 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad930',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '1.4',
 'pos_y': '4.258',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction50 = DolanJunction(
design,
name='dolan_junction50',
options={'layer': 2,
 'orientation': -180,
 'pos_x': 1.4,
 'pos_y': 4.3895},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee92 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee92',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '1.0394999999999999',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path691 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path691',
options={'_actual_length': '4.035071118430774 '
                   'mm',
 'anchors': {0: (1.1195, 3.9775),
             1: (1.1195, 4.5385),
             2: (1.6804999999999999,
                 4.5385),
             3: (1.6804999999999999,
                 3.9775),
             4: (1.0635, 3.9215),
             5: (1.0635,
                 4.539499999999999),
             6: (0.9794999999999998,
                 4.539499999999999),
             7: (0.9794999999999998,
                 3.9215)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge51 = airbridges(
design,
name='Airbridge51',
options={'cpw_name': 'cpw_(6,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment659 = ShortRoute(
design,
name='short_line_Segment659',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(6,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge180 = airbridges(
design,
name='Airbridge180',
options={'cpw_name': '(6,0)CPW(5,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad304 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad304',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '2.3',
 'pos_y': '4.25',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction729 = DolanJunction(
design,
name='dolan_junction729',
options={'Lj': '8',
 'layer': 2,
 'orientation': -180,
 'pos_x': 2.3,
 'pos_y': 4.3665},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee484 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee484',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '1.9569999999999999',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path764 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path764',
options={'_actual_length': '3.522751118430774 '
                   'mm',
 'anchors': {0: (2.037, 3.987),
             1: (2.037, 4.513),
             2: (2.5629999999999997,
                 4.513),
             3: (2.5629999999999997,
                 3.987),
             4: (1.9809999999999999,
                 3.931),
             5: (1.9809999999999999,
                 4.369),
             6: (1.8969999999999998,
                 4.369),
             7: (1.8969999999999998,
                 3.931)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge97 = airbridges(
design,
name='Airbridge97',
options={'cpw_name': 'cpw_(7,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment326 = ShortRoute(
design,
name='short_line_Segment326',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(7,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge495 = airbridges(
design,
name='Airbridge495',
options={'cpw_name': '(7,0)CPW(6,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad777 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad777',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': -180,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '3.2',
 'pos_y': '4.25',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction847 = DolanJunction(
design,
name='dolan_junction847',
options={'layer': 2,
 'orientation': -180,
 'pos_x': 3.2,
 'pos_y': 4.377},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee645 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee645',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': -180,
 'pos_x': '2.8515',
 'pos_y': '3.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path616 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path616',
options={'_actual_length': '3.8752311184307726 '
                   'mm',
 'anchors': {0: (2.9315,
                 3.9815000000000005),
             1: (2.9315,
                 4.5184999999999995),
             2: (3.4685, 4.5185),
             3: (3.4685,
                 3.9815000000000005),
             4: (2.8755,
                 3.9255000000000004),
             5: (2.8755, 4.5195),
             6: (2.7915, 4.5195),
             7: (2.7915,
                 3.9255000000000004)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge166 = airbridges(
design,
name='Airbridge166',
options={'cpw_name': 'cpw_(8,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment820 = ShortRoute(
design,
name='short_line_Segment820',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(8,0)',
                              'pin': 'prime_end'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge397 = airbridges(
design,
name='Airbridge397',
options={'cpw_name': '(8,0)CPW(7,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad498 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad498',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': -270,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.49',
 'pos_y': '4.4',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction30 = DolanJunction(
design,
name='dolan_junction30',
options={'Lj': '13',
 'layer': 2,
 'orientation': -270,
 'pos_x': 4.6275,
 'pos_y': 4.4},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee797 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee797',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': -270,
 'pos_x': '4.05',
 'pos_y': '4.1465000000000005',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path877 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path877',
options={'_actual_length': '4.36607111843078 mm',
 'anchors': {0: (4.2325,
                 4.657500000000001),
             1: (4.7475000000000005,
                 4.657500000000001),
             2: (4.7475000000000005,
                 4.1425),
             3: (4.2325, 4.1425),
             4: (4.1765,
                 4.713500000000001),
             5: (4.8035000000000005,
                 4.713500000000001),
             6: (4.8035000000000005,
                 4.0865),
             7: (4.1765, 4.0865)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,0)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,0)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge552 = airbridges(
design,
name='Airbridge552',
options={'cpw_name': 'cpw_(9,0)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path453 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path453',
options={'_actual_length': '1.2921238898038474 '
                   'mm',
 'anchors': {0: (4.05, 3.8)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'TQ(9,0)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge902 = airbridges(
design,
name='Airbridge902',
options={'cpw_name': '(9,0)CPW(8,0)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path385 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path385',
options={'_actual_length': '1.1497477796076938 '
                   'mm',
 'anchors': {0: (3.9, 4.75)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,0)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right0',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge179 = airbridges(
design,
name='Airbridge179',
options={'cpw_name': '(9,0)CPWwb_right0',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path850 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path850',
options={'_actual_length': '0.9752477796076933 '
                   'mm',
 'anchors': {0: (-3.9, 4.75)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,0)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left0',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge268 = airbridges(
design,
name='Airbridge268',
options={'cpw_name': '(0,0)CPWwb_left0',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad895 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad895',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-4.2',
 'pos_y': '3.15',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction736 = DolanJunction(
design,
name='dolan_junction736',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': 3.0075},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee221 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee221',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.8325',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path336 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path336',
options={'_actual_length': '4.167421118430776 '
                   'mm',
 'anchors': {0: (-3.9125, 3.4375),
             1: (-3.9125, 2.8625),
             2: (-4.4875, 2.8625),
             3: (-4.4875, 3.4375),
             4: (-3.8565, 3.4935),
             5: (-3.8565,
                 2.8564999999999996),
             6: (-3.7725,
                 2.8564999999999996),
             7: (-3.7725, 3.4935)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge607 = airbridges(
design,
name='Airbridge607',
options={'cpw_name': 'cpw_(0,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path829 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path829',
options={'_actual_length': '1.0637477796076935 '
                   'mm',
 'anchors': {0: (-4.75, 3.65)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,1)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left1',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge564 = airbridges(
design,
name='Airbridge564',
options={'cpw_name': '(0,1)CPWwb_left1',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad73 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad73',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-3.27',
 'pos_y': '3.21',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction798 = DolanJunction(
design,
name='dolan_junction798',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': 3.0869999999999997},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee809 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee809',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.941',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path698 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path698',
options={'_actual_length': '3.6146211184307764 '
                   'mm',
 'anchors': {0: (-3.021, 3.459),
             1: (-3.021, 2.961),
             2: (-3.519, 2.961),
             3: (-3.519, 3.459),
             4: (-2.965, 3.515),
             5: (-2.965, 2.96),
             6: (-2.881, 2.96),
             7: (-2.881, 3.515)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge648 = airbridges(
design,
name='Airbridge648',
options={'cpw_name': 'cpw_(1,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment990 = ShortRoute(
design,
name='short_line_Segment990',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge772 = airbridges(
design,
name='Airbridge772',
options={'cpw_name': '(1,1)CPW(0,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad843 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad843',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-2.34',
 'pos_y': '3.2199999999999998',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction487 = DolanJunction(
design,
name='dolan_junction487',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': 3.0959999999999996},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee960 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee960',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.5885',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path483 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path483',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-2.0875,
                 3.4724999999999997),
             1: (-2.0875, 2.9675),
             2: (-2.5925, 2.9675),
             3: (-2.5925,
                 3.4724999999999997),
             4: (-2.0315,
                 3.5284999999999997),
             5: (-2.0315,
                 2.9114999999999998),
             6: (-2.6485,
                 2.9114999999999998),
             7: (-2.6485,
                 3.5284999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge225 = airbridges(
design,
name='Airbridge225',
options={'cpw_name': 'cpw_(2,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment334 = ShortRoute(
design,
name='short_line_Segment334',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge551 = airbridges(
design,
name='Airbridge551',
options={'cpw_name': '(2,1)CPW(1,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad670 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad670',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '3.19',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction434 = DolanJunction(
design,
name='dolan_junction434',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': 3.0575},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee470 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee470',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.0725000000000002',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path834 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path834',
options={'_actual_length': '3.716001118430775 '
                   'mm',
 'anchors': {0: (-1.1525, 3.4475),
             1: (-1.1525, 2.9325),
             2: (-1.6675000000000002,
                 2.9325),
             3: (-1.6675000000000002,
                 3.4475),
             4: (-1.0965000000000003,
                 3.5035),
             5: (-1.0965000000000003,
                 2.9415),
             6: (-1.0125000000000002,
                 2.9415),
             7: (-1.0125000000000002,
                 3.5035)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge122 = airbridges(
design,
name='Airbridge122',
options={'cpw_name': 'cpw_(3,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment310 = ShortRoute(
design,
name='short_line_Segment310',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge198 = airbridges(
design,
name='Airbridge198',
options={'cpw_name': '(3,1)CPW(2,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad650 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad650',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '3.21',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction594 = DolanJunction(
design,
name='dolan_junction594',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': 3.0725},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee248 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee248',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.7335',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path24 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path24',
options={'_actual_length': '4.366071118430774 '
                   'mm',
 'anchors': {0: (-0.22249999999999998,
                 3.4675),
             1: (-0.22249999999999998,
                 2.9525),
             2: (-0.7375, 2.9525),
             3: (-0.7375, 3.4675),
             4: (-0.16649999999999998,
                 3.5235),
             5: (-0.16649999999999998,
                 2.8965),
             6: (-0.7935, 2.8965),
             7: (-0.7935, 3.5235)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge541 = airbridges(
design,
name='Airbridge541',
options={'cpw_name': 'cpw_(4,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment93 = ShortRoute(
design,
name='short_line_Segment93',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge787 = airbridges(
design,
name='Airbridge787',
options={'cpw_name': '(4,1)CPW(3,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad687 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad687',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '3.1999999999999997',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction430 = DolanJunction(
design,
name='dolan_junction430',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': 3.0729999999999995},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee732 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee732',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.7985000000000002',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path665 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path665',
options={'_actual_length': '3.875231118430775 '
                   'mm',
 'anchors': {0: (0.7185000000000001,
                 3.4684999999999997),
             1: (0.7185000000000001,
                 2.9314999999999998),
             2: (0.18150000000000022,
                 2.9314999999999998),
             3: (0.18150000000000022,
                 3.4684999999999997),
             4: (0.7745000000000002,
                 3.5244999999999997),
             5: (0.7745000000000002,
                 2.9305),
             6: (0.8585000000000002,
                 2.9305),
             7: (0.8585000000000002,
                 3.5244999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge503 = airbridges(
design,
name='Airbridge503',
options={'cpw_name': 'cpw_(5,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment308 = ShortRoute(
design,
name='short_line_Segment308',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge886 = airbridges(
design,
name='Airbridge886',
options={'cpw_name': '(5,1)CPW(4,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad634 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad634',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '1.38',
 'pos_y': '3.1999999999999997',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction524 = DolanJunction(
design,
name='dolan_junction524',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': 3.0835},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee787 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee787',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7229999999999999',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path53 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path53',
options={'_actual_length': '3.522751118430774 '
                   'mm',
 'anchors': {0: (1.6429999999999998,
                 3.4629999999999996),
             1: (1.6429999999999998,
                 2.937),
             2: (1.117, 2.937),
             3: (1.117,
                 3.4629999999999996),
             4: (1.6989999999999998,
                 3.5189999999999997),
             5: (1.6989999999999998,
                 3.081),
             6: (1.783, 3.081),
             7: (1.783,
                 3.5189999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge628 = airbridges(
design,
name='Airbridge628',
options={'cpw_name': 'cpw_(6,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment45 = ShortRoute(
design,
name='short_line_Segment45',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge384 = airbridges(
design,
name='Airbridge384',
options={'cpw_name': '(6,1)CPW(5,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad316 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad316',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '3.1919999999999997',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction40 = DolanJunction(
design,
name='dolan_junction40',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': 3.0604999999999998},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee653 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee653',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6705000000000005',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path872 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path872',
options={'_actual_length': '4.035071118430776 '
                   'mm',
 'anchors': {0: (2.5905000000000005,
                 3.4724999999999997),
             1: (2.5905000000000005,
                 2.9114999999999998),
             2: (2.0295000000000005,
                 2.9114999999999998),
             3: (2.0295000000000005,
                 3.4724999999999997),
             4: (2.6465000000000005,
                 3.5284999999999997),
             5: (2.6465000000000005,
                 2.9105),
             6: (2.7305000000000006,
                 2.9105),
             7: (2.7305000000000006,
                 3.5284999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge315 = airbridges(
design,
name='Airbridge315',
options={'cpw_name': 'cpw_(7,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment733 = ShortRoute(
design,
name='short_line_Segment733',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge758 = airbridges(
design,
name='Airbridge758',
options={'cpw_name': '(7,1)CPW(6,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad740 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad740',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '3.24',
 'pos_y': '3.1999999999999997',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction256 = DolanJunction(
design,
name='dolan_junction256',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': 3.0549999999999997},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee989 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee989',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.9730000000000003',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path440 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path440',
options={'_actual_length': '4.571361118430774 '
                   'mm',
 'anchors': {0: (3.511,
                 3.4709999999999996),
             1: (3.511, 2.929),
             2: (2.9690000000000003,
                 2.929),
             3: (2.9690000000000003,
                 3.4709999999999996),
             4: (3.567,
                 3.5269999999999997),
             5: (3.567,
                 2.8729999999999998),
             6: (2.9130000000000003,
                 2.8729999999999998),
             7: (2.9130000000000003,
                 3.5269999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge624 = airbridges(
design,
name='Airbridge624',
options={'cpw_name': 'cpw_(8,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment855 = ShortRoute(
design,
name='short_line_Segment855',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge178 = airbridges(
design,
name='Airbridge178',
options={'cpw_name': '(8,1)CPW(7,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad668 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad668',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '3.19',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction343 = DolanJunction(
design,
name='dolan_junction343',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': 3.0524999999999998},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee976 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee976',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '4.512500000000001',
 'pos_y': '3.65',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path263 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path263',
options={'_actual_length': '3.8223611184307766 '
                   'mm',
 'anchors': {0: (4.432500000000001,
                 3.4525),
             1: (4.432500000000001,
                 2.9274999999999998),
             2: (3.9075000000000006,
                 2.9274999999999998),
             3: (3.9075000000000006,
                 3.4525),
             4: (4.488500000000001,
                 3.5084999999999997),
             5: (4.488500000000001,
                 2.9135),
             6: (4.572500000000001,
                 2.9135),
             7: (4.572500000000001,
                 3.5084999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,1)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,1)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge891 = airbridges(
design,
name='Airbridge891',
options={'cpw_name': 'cpw_(9,1)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment427 = ShortRoute(
design,
name='short_line_Segment427',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,1)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge146 = airbridges(
design,
name='Airbridge146',
options={'cpw_name': '(9,1)CPW(8,1)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path10 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path10',
options={'_actual_length': '0.38374777960769335 '
                   'mm',
 'anchors': {0: (4.75, 3.65)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,1)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right1',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge968 = airbridges(
design,
name='Airbridge968',
options={'cpw_name': '(9,1)CPWwb_right1',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad837 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad837',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-4.2',
 'pos_y': '2.2600000000000002',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction300 = DolanJunction(
design,
name='dolan_junction300',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': 2.1370000000000005},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee481 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee481',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.871',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path166 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path166',
options={'_actual_length': '3.614621118430776 '
                   'mm',
 'anchors': {0: (-3.951,
                 2.5090000000000003),
             1: (-3.951, 2.011),
             2: (-4.449, 2.011),
             3: (-4.449,
                 2.5090000000000003),
             4: (-3.895,
                 2.5650000000000004),
             5: (-3.895,
                 2.0100000000000002),
             6: (-3.811,
                 2.0100000000000002),
             7: (-3.811,
                 2.5650000000000004)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge532 = airbridges(
design,
name='Airbridge532',
options={'cpw_name': 'cpw_(0,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path274 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path274',
options={'_actual_length': '0.9252477796076939 '
                   'mm',
 'anchors': {0: (-4.75, 2.7)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,2)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left2',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge272 = airbridges(
design,
name='Airbridge272',
options={'cpw_name': '(0,2)CPWwb_left2',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad797 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad797',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-3.27',
 'pos_y': '2.2',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction946 = DolanJunction(
design,
name='dolan_junction946',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': 2.0575},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee6 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee6',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.9025',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path221 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path221',
options={'_actual_length': '4.167421118430776 '
                   'mm',
 'anchors': {0: (-2.9825,
                 2.4875000000000003),
             1: (-2.9825, 1.9125),
             2: (-3.5575, 1.9125),
             3: (-3.5575,
                 2.4875000000000003),
             4: (-2.9265,
                 2.5435000000000003),
             5: (-2.9265,
                 1.9065000000000003),
             6: (-2.8425,
                 1.9065000000000003),
             7: (-2.8425,
                 2.5435000000000003)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge631 = airbridges(
design,
name='Airbridge631',
options={'cpw_name': 'cpw_(1,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment989 = ShortRoute(
design,
name='short_line_Segment989',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge803 = airbridges(
design,
name='Airbridge803',
options={'cpw_name': '(1,2)CPW(0,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad89 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad89',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-2.34',
 'pos_y': '2.24',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction138 = DolanJunction(
design,
name='dolan_junction138',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': 2.1075000000000004},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee437 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee437',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.0025',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path626 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path626',
options={'_actual_length': '3.716001118430774 '
                   'mm',
 'anchors': {0: (-2.0825, 2.4975),
             1: (-2.0825,
                 1.9825000000000002),
             2: (-2.5974999999999997,
                 1.9825000000000002),
             3: (-2.5974999999999997,
                 2.4975),
             4: (-2.0265, 2.5535),
             5: (-2.0265,
                 1.9915000000000003),
             6: (-1.9425,
                 1.9915000000000003),
             7: (-1.9425, 2.5535)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge800 = airbridges(
design,
name='Airbridge800',
options={'cpw_name': 'cpw_(2,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment889 = ShortRoute(
design,
name='short_line_Segment889',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge624 = airbridges(
design,
name='Airbridge624',
options={'cpw_name': '(2,2)CPW(1,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad218 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad218',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '2.27',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction194 = DolanJunction(
design,
name='dolan_junction194',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': 2.146},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee838 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee838',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.6585',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path299 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path299',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-1.1575000000000002,
                 2.5225),
             1: (-1.1575000000000002,
                 2.0175),
             2: (-1.6625, 2.0175),
             3: (-1.6625, 2.5225),
             4: (-1.1015000000000001,
                 2.5785),
             5: (-1.1015000000000001,
                 1.9615),
             6: (-1.7185000000000001,
                 1.9615),
             7: (-1.7185000000000001,
                 2.5785)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge246 = airbridges(
design,
name='Airbridge246',
options={'cpw_name': 'cpw_(3,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment834 = ShortRoute(
design,
name='short_line_Segment834',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge219 = airbridges(
design,
name='Airbridge219',
options={'cpw_name': '(3,2)CPW(2,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad651 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad651',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '2.24',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction924 = DolanJunction(
design,
name='dolan_junction924',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': 2.1025},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee277 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee277',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.13749999999999996',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path605 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path605',
options={'_actual_length': '3.8223611184307758 '
                   'mm',
 'anchors': {0: (-0.21749999999999997,
                 2.5025000000000004),
             1: (-0.21749999999999997,
                 1.9775000000000003),
             2: (-0.7424999999999999,
                 1.9775000000000003),
             3: (-0.7424999999999999,
                 2.5025000000000004),
             4: (-0.16149999999999998,
                 2.5585000000000004),
             5: (-0.16149999999999998,
                 1.9635000000000002),
             6: (-0.07749999999999996,
                 1.9635000000000002),
             7: (-0.07749999999999996,
                 2.5585000000000004)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge184 = airbridges(
design,
name='Airbridge184',
options={'cpw_name': 'cpw_(4,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment872 = ShortRoute(
design,
name='short_line_Segment872',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge830 = airbridges(
design,
name='Airbridge830',
options={'cpw_name': '(4,2)CPW(3,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad182 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad182',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '2.25',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction720 = DolanJunction(
design,
name='dolan_junction720',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': 2.105},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee333 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee333',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.18300000000000016',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path997 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path997',
options={'_actual_length': '4.571361118430774 '
                   'mm',
 'anchors': {0: (0.7210000000000001,
                 2.521),
             1: (0.7210000000000001,
                 1.979),
             2: (0.17900000000000021,
                 1.979),
             3: (0.17900000000000021,
                 2.521),
             4: (0.7770000000000001,
                 2.577),
             5: (0.7770000000000001,
                 1.923),
             6: (0.12300000000000022,
                 1.923),
             7: (0.12300000000000022,
                 2.577)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge636 = airbridges(
design,
name='Airbridge636',
options={'cpw_name': 'cpw_(5,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment807 = ShortRoute(
design,
name='short_line_Segment807',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge697 = airbridges(
design,
name='Airbridge697',
options={'cpw_name': '(5,2)CPW(4,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad123 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad123',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '1.38',
 'pos_y': '2.242',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction229 = DolanJunction(
design,
name='dolan_junction229',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': 2.1105},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee281 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee281',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7405',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path246 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path246',
options={'_actual_length': '4.035071118430775 '
                   'mm',
 'anchors': {0: (1.6604999999999999,
                 2.5225),
             1: (1.6604999999999999,
                 1.9615),
             2: (1.0995, 1.9615),
             3: (1.0995, 2.5225),
             4: (1.7165, 2.5785),
             5: (1.7165, 1.9605),
             6: (1.8005, 1.9605),
             7: (1.8005, 2.5785)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge104 = airbridges(
design,
name='Airbridge104',
options={'cpw_name': 'cpw_(6,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment610 = ShortRoute(
design,
name='short_line_Segment610',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge127 = airbridges(
design,
name='Airbridge127',
options={'cpw_name': '(6,2)CPW(5,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad478 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad478',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '2.25',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction84 = DolanJunction(
design,
name='dolan_junction84',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': 2.1335},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee485 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee485',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6530000000000005',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path194 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path194',
options={'_actual_length': '3.5227511184307745 '
                   'mm',
 'anchors': {0: (2.5730000000000004,
                 2.513),
             1: (2.5730000000000004,
                 1.987),
             2: (2.0470000000000006,
                 1.987),
             3: (2.0470000000000006,
                 2.513),
             4: (2.6290000000000004,
                 2.569),
             5: (2.6290000000000004,
                 2.1310000000000002),
             6: (2.7130000000000005,
                 2.1310000000000002),
             7: (2.7130000000000005,
                 2.569)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge590 = airbridges(
design,
name='Airbridge590',
options={'cpw_name': 'cpw_(7,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment599 = ShortRoute(
design,
name='short_line_Segment599',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge489 = airbridges(
design,
name='Airbridge489',
options={'cpw_name': '(7,2)CPW(6,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad976 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad976',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '3.24',
 'pos_y': '2.25',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction770 = DolanJunction(
design,
name='dolan_junction770',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': 2.123},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee936 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee936',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.5885000000000002',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path693 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path693',
options={'_actual_length': '3.875231118430775 '
                   'mm',
 'anchors': {0: (3.5085, 2.5185),
             1: (3.5085, 1.9815),
             2: (2.9715000000000003,
                 1.9815),
             3: (2.9715000000000003,
                 2.5185),
             4: (3.5645000000000002,
                 2.5745),
             5: (3.5645000000000002,
                 1.9805),
             6: (3.6485000000000003,
                 1.9805),
             7: (3.6485000000000003,
                 2.5745)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge543 = airbridges(
design,
name='Airbridge543',
options={'cpw_name': 'cpw_(8,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment190 = ShortRoute(
design,
name='short_line_Segment190',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge940 = airbridges(
design,
name='Airbridge940',
options={'cpw_name': '(8,2)CPW(7,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad987 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad987',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '2.2600000000000002',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction482 = DolanJunction(
design,
name='dolan_junction482',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': 2.1225},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee394 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee394',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.916500000000001',
 'pos_y': '2.7',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path451 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path451',
options={'_actual_length': '4.366071118430776 '
                   'mm',
 'anchors': {0: (4.427500000000001,
                 2.5175),
             1: (4.427500000000001,
                 2.0025000000000004),
             2: (3.912500000000001,
                 2.0025000000000004),
             3: (3.912500000000001,
                 2.5175),
             4: (4.483500000000001,
                 2.5735),
             5: (4.483500000000001,
                 1.9465000000000003),
             6: (3.856500000000001,
                 1.9465000000000003),
             7: (3.856500000000001,
                 2.5735)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,2)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,2)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge821 = airbridges(
design,
name='Airbridge821',
options={'cpw_name': 'cpw_(9,2)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment75 = ShortRoute(
design,
name='short_line_Segment75',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,2)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge250 = airbridges(
design,
name='Airbridge250',
options={'cpw_name': '(9,2)CPW(8,2)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path954 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path954',
options={'_actual_length': '0.8797477796076938 '
                   'mm',
 'anchors': {0: (4.75, 2.7)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,2)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right2',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge790 = airbridges(
design,
name='Airbridge790',
options={'cpw_name': '(9,2)CPWwb_right2',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad581 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad581',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-4.2',
 'pos_y': '1.25',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction293 = DolanJunction(
design,
name='dolan_junction293',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': 1.1075},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee652 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee652',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.8325',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path503 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path503',
options={'_actual_length': '4.167421118430775 '
                   'mm',
 'anchors': {0: (-3.9125, 1.5375),
             1: (-3.9125, 0.9625),
             2: (-4.4875, 0.9625),
             3: (-4.4875, 1.5375),
             4: (-3.8565, 1.5935),
             5: (-3.8565,
                 0.9565000000000001),
             6: (-3.7725,
                 0.9565000000000001),
             7: (-3.7725, 1.5935)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge391 = airbridges(
design,
name='Airbridge391',
options={'cpw_name': 'cpw_(0,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path941 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path941',
options={'_actual_length': '1.0179955592153875 '
                   'mm',
 'anchors': {0: (-4.75,
                 1.6099999999999999),
             1: (-4.67, 1.75)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,3)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left3',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge951 = airbridges(
design,
name='Airbridge951',
options={'cpw_name': '(0,3)CPWwb_left3',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad500 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad500',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-3.27',
 'pos_y': '1.31',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction184 = DolanJunction(
design,
name='dolan_junction184',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': 1.187},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee629 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee629',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.941',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path220 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path220',
options={'_actual_length': '3.6146211184307764 '
                   'mm',
 'anchors': {0: (-3.021,
                 1.5590000000000002),
             1: (-3.021, 1.061),
             2: (-3.519, 1.061),
             3: (-3.519,
                 1.5590000000000002),
             4: (-2.965, 1.615),
             5: (-2.965, 1.06),
             6: (-2.881, 1.06),
             7: (-2.881, 1.615)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge666 = airbridges(
design,
name='Airbridge666',
options={'cpw_name': 'cpw_(1,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment12 = ShortRoute(
design,
name='short_line_Segment12',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge416 = airbridges(
design,
name='Airbridge416',
options={'cpw_name': '(1,3)CPW(0,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad499 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad499',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-2.34',
 'pos_y': '1.32',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction966 = DolanJunction(
design,
name='dolan_junction966',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': 1.1960000000000002},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee345 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee345',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.5885',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path173 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path173',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-2.0875, 1.5725),
             1: (-2.0875,
                 1.0675000000000001),
             2: (-2.5925,
                 1.0675000000000001),
             3: (-2.5925, 1.5725),
             4: (-2.0315, 1.6285),
             5: (-2.0315, 1.0115),
             6: (-2.6485, 1.0115),
             7: (-2.6485, 1.6285)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge278 = airbridges(
design,
name='Airbridge278',
options={'cpw_name': 'cpw_(2,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment391 = ShortRoute(
design,
name='short_line_Segment391',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge683 = airbridges(
design,
name='Airbridge683',
options={'cpw_name': '(2,3)CPW(1,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad88 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad88',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '1.29',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction594 = DolanJunction(
design,
name='dolan_junction594',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': 1.1575},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee105 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee105',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.0725000000000002',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path785 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path785',
options={'_actual_length': '3.7160011184307757 '
                   'mm',
 'anchors': {0: (-1.1525, 1.5475),
             1: (-1.1525, 1.0325),
             2: (-1.6675000000000002,
                 1.0325),
             3: (-1.6675000000000002,
                 1.5475),
             4: (-1.0965000000000003,
                 1.6035),
             5: (-1.0965000000000003,
                 1.0415),
             6: (-1.0125000000000002,
                 1.0415),
             7: (-1.0125000000000002,
                 1.6035)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge999 = airbridges(
design,
name='Airbridge999',
options={'cpw_name': 'cpw_(3,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment335 = ShortRoute(
design,
name='short_line_Segment335',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge275 = airbridges(
design,
name='Airbridge275',
options={'cpw_name': '(3,3)CPW(2,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad818 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad818',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '1.31',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction318 = DolanJunction(
design,
name='dolan_junction318',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': 1.1725},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee35 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee35',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.7335',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path663 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path663',
options={'_actual_length': '4.366071118430775 '
                   'mm',
 'anchors': {0: (-0.22249999999999998,
                 1.5675000000000001),
             1: (-0.22249999999999998,
                 1.0525),
             2: (-0.7375, 1.0525),
             3: (-0.7375,
                 1.5675000000000001),
             4: (-0.16649999999999998,
                 1.6235),
             5: (-0.16649999999999998,
                 0.9965),
             6: (-0.7935, 0.9965),
             7: (-0.7935, 1.6235)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge684 = airbridges(
design,
name='Airbridge684',
options={'cpw_name': 'cpw_(4,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment821 = ShortRoute(
design,
name='short_line_Segment821',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge93 = airbridges(
design,
name='Airbridge93',
options={'cpw_name': '(4,3)CPW(3,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad142 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad142',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '1.3',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction615 = DolanJunction(
design,
name='dolan_junction615',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': 1.173},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee322 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee322',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.7985000000000002',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path900 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path900',
options={'_actual_length': '3.875231118430775 '
                   'mm',
 'anchors': {0: (0.7185000000000001,
                 1.5685),
             1: (0.7185000000000001,
                 1.0315),
             2: (0.18150000000000022,
                 1.0315),
             3: (0.18150000000000022,
                 1.5685),
             4: (0.7745000000000002,
                 1.6245),
             5: (0.7745000000000002,
                 1.0305),
             6: (0.8585000000000002,
                 1.0305),
             7: (0.8585000000000002,
                 1.6245)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge276 = airbridges(
design,
name='Airbridge276',
options={'cpw_name': 'cpw_(5,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment721 = ShortRoute(
design,
name='short_line_Segment721',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge438 = airbridges(
design,
name='Airbridge438',
options={'cpw_name': '(5,3)CPW(4,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad651 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad651',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '1.38',
 'pos_y': '1.3',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction802 = DolanJunction(
design,
name='dolan_junction802',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': 1.1835},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee583 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee583',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7229999999999999',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path680 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path680',
options={'_actual_length': '3.522751118430775 '
                   'mm',
 'anchors': {0: (1.6429999999999998,
                 1.5630000000000002),
             1: (1.6429999999999998,
                 1.037),
             2: (1.117, 1.037),
             3: (1.117,
                 1.5630000000000002),
             4: (1.6989999999999998,
                 1.619),
             5: (1.6989999999999998,
                 1.181),
             6: (1.783, 1.181),
             7: (1.783, 1.619)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge174 = airbridges(
design,
name='Airbridge174',
options={'cpw_name': 'cpw_(6,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment822 = ShortRoute(
design,
name='short_line_Segment822',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge413 = airbridges(
design,
name='Airbridge413',
options={'cpw_name': '(6,3)CPW(5,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad912 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad912',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '1.292',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction375 = DolanJunction(
design,
name='dolan_junction375',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': 1.1605},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee513 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee513',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6705000000000005',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path992 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path992',
options={'_actual_length': '4.035071118430776 '
                   'mm',
 'anchors': {0: (2.5905000000000005,
                 1.5725),
             1: (2.5905000000000005,
                 1.0115),
             2: (2.0295000000000005,
                 1.0115),
             3: (2.0295000000000005,
                 1.5725),
             4: (2.6465000000000005,
                 1.6285),
             5: (2.6465000000000005,
                 1.0105),
             6: (2.7305000000000006,
                 1.0105),
             7: (2.7305000000000006,
                 1.6285)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge793 = airbridges(
design,
name='Airbridge793',
options={'cpw_name': 'cpw_(7,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment778 = ShortRoute(
design,
name='short_line_Segment778',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge925 = airbridges(
design,
name='Airbridge925',
options={'cpw_name': '(7,3)CPW(6,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad778 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad778',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '3.24',
 'pos_y': '1.3',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction917 = DolanJunction(
design,
name='dolan_junction917',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': 1.155},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee449 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee449',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.9730000000000003',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path50 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path50',
options={'_actual_length': '4.571361118430774 '
                   'mm',
 'anchors': {0: (3.511, 1.571),
             1: (3.511,
                 1.0290000000000001),
             2: (2.9690000000000003,
                 1.0290000000000001),
             3: (2.9690000000000003,
                 1.571),
             4: (3.567, 1.627),
             5: (3.567,
                 0.9730000000000001),
             6: (2.9130000000000003,
                 0.9730000000000001),
             7: (2.9130000000000003,
                 1.627)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge951 = airbridges(
design,
name='Airbridge951',
options={'cpw_name': 'cpw_(8,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment482 = ShortRoute(
design,
name='short_line_Segment482',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge489 = airbridges(
design,
name='Airbridge489',
options={'cpw_name': '(8,3)CPW(7,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad85 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad85',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '1.29',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction596 = DolanJunction(
design,
name='dolan_junction596',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': 1.1525},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee823 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee823',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '4.512500000000001',
 'pos_y': '1.75',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path837 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path837',
options={'_actual_length': '3.8223611184307766 '
                   'mm',
 'anchors': {0: (4.432500000000001,
                 1.5525),
             1: (4.432500000000001,
                 1.0275),
             2: (3.9075000000000006,
                 1.0275),
             3: (3.9075000000000006,
                 1.5525),
             4: (4.488500000000001,
                 1.6085),
             5: (4.488500000000001,
                 1.0135),
             6: (4.572500000000001,
                 1.0135),
             7: (4.572500000000001,
                 1.6085)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,3)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,3)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge777 = airbridges(
design,
name='Airbridge777',
options={'cpw_name': 'cpw_(9,3)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment177 = ShortRoute(
design,
name='short_line_Segment177',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,3)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge795 = airbridges(
design,
name='Airbridge795',
options={'cpw_name': '(9,3)CPW(8,3)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path904 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path904',
options={'_actual_length': '0.3379955592153873 '
                   'mm',
 'anchors': {0: (4.75,
                 1.6099999999999999),
             1: (4.67, 1.75)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,3)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right3',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge279 = airbridges(
design,
name='Airbridge279',
options={'cpw_name': '(9,3)CPWwb_right3',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad144 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad144',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-4.2',
 'pos_y': '0.36000000000000004',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction663 = DolanJunction(
design,
name='dolan_junction663',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': 0.23700000000000004},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee845 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee845',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.871',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path383 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path383',
options={'_actual_length': '3.6146211184307746 '
                   'mm',
 'anchors': {0: (-3.951, 0.609),
             1: (-3.951,
                 0.11100000000000004),
             2: (-4.449,
                 0.11100000000000004),
             3: (-4.449, 0.609),
             4: (-3.895, 0.665),
             5: (-3.895,
                 0.11000000000000004),
             6: (-3.811,
                 0.11000000000000004),
             7: (-3.811, 0.665)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge461 = airbridges(
design,
name='Airbridge461',
options={'cpw_name': 'cpw_(0,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path684 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path684',
options={'_actual_length': '0.9794955592153878 '
                   'mm',
 'anchors': {0: (-4.75,
                 0.7099999999999997),
             1: (-4.67, 0.8)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,4)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left4',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge638 = airbridges(
design,
name='Airbridge638',
options={'cpw_name': '(0,4)CPWwb_left4',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad436 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad436',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-3.27',
 'pos_y': '0.30000000000000004',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction937 = DolanJunction(
design,
name='dolan_junction937',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': 0.15750000000000003},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee858 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee858',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.9025',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path427 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path427',
options={'_actual_length': '4.1674211184307755 '
                   'mm',
 'anchors': {0: (-2.9825, 0.5875),
             1: (-2.9825,
                 0.012500000000000067),
             2: (-3.5575,
                 0.012500000000000067),
             3: (-3.5575, 0.5875),
             4: (-2.9265, 0.6435),
             5: (-2.9265,
                 0.006500000000000061),
             6: (-2.8425,
                 0.006500000000000061),
             7: (-2.8425, 0.6435)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge516 = airbridges(
design,
name='Airbridge516',
options={'cpw_name': 'cpw_(1,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment701 = ShortRoute(
design,
name='short_line_Segment701',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge277 = airbridges(
design,
name='Airbridge277',
options={'cpw_name': '(1,4)CPW(0,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad22 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad22',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-2.34',
 'pos_y': '0.34',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction561 = DolanJunction(
design,
name='dolan_junction561',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': 0.20750000000000002},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee803 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee803',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.0025',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path100 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path100',
options={'_actual_length': '3.716001118430775 '
                   'mm',
 'anchors': {0: (-2.0825, 0.5975),
             1: (-2.0825,
                 0.08250000000000002),
             2: (-2.5974999999999997,
                 0.08250000000000002),
             3: (-2.5974999999999997,
                 0.5975),
             4: (-2.0265, 0.6535),
             5: (-2.0265,
                 0.09150000000000003),
             6: (-1.9425,
                 0.09150000000000003),
             7: (-1.9425, 0.6535)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge41 = airbridges(
design,
name='Airbridge41',
options={'cpw_name': 'cpw_(2,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment823 = ShortRoute(
design,
name='short_line_Segment823',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge648 = airbridges(
design,
name='Airbridge648',
options={'cpw_name': '(2,4)CPW(1,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad548 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad548',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '0.37000000000000005',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction74 = DolanJunction(
design,
name='dolan_junction74',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': 0.24600000000000005},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee335 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee335',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.6585',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path529 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path529',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-1.1575000000000002,
                 0.6225),
             1: (-1.1575000000000002,
                 0.11750000000000005),
             2: (-1.6625,
                 0.11750000000000005),
             3: (-1.6625, 0.6225),
             4: (-1.1015000000000001,
                 0.6785000000000001),
             5: (-1.1015000000000001,
                 0.061500000000000055),
             6: (-1.7185000000000001,
                 0.061500000000000055),
             7: (-1.7185000000000001,
                 0.6785000000000001)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge985 = airbridges(
design,
name='Airbridge985',
options={'cpw_name': 'cpw_(3,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment294 = ShortRoute(
design,
name='short_line_Segment294',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge227 = airbridges(
design,
name='Airbridge227',
options={'cpw_name': '(3,4)CPW(2,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad118 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad118',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '0.34',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction685 = DolanJunction(
design,
name='dolan_junction685',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': 0.2025},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee565 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee565',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.13749999999999996',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path14 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path14',
options={'_actual_length': '3.8223611184307753 '
                   'mm',
 'anchors': {0: (-0.21749999999999997,
                 0.6025),
             1: (-0.21749999999999997,
                 0.07750000000000001),
             2: (-0.7424999999999999,
                 0.07750000000000001),
             3: (-0.7424999999999999,
                 0.6025),
             4: (-0.16149999999999998,
                 0.6585000000000001),
             5: (-0.16149999999999998,
                 0.06350000000000006),
             6: (-0.07749999999999996,
                 0.06350000000000006),
             7: (-0.07749999999999996,
                 0.6585000000000001)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge411 = airbridges(
design,
name='Airbridge411',
options={'cpw_name': 'cpw_(4,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment691 = ShortRoute(
design,
name='short_line_Segment691',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge302 = airbridges(
design,
name='Airbridge302',
options={'cpw_name': '(4,4)CPW(3,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad55 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad55',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '0.35000000000000003',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction653 = DolanJunction(
design,
name='dolan_junction653',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': 0.20500000000000004},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee263 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee263',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.18300000000000016',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path731 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path731',
options={'_actual_length': '4.571361118430775 '
                   'mm',
 'anchors': {0: (0.7210000000000001,
                 0.621),
             1: (0.7210000000000001,
                 0.07900000000000007),
             2: (0.17900000000000021,
                 0.07900000000000007),
             3: (0.17900000000000021,
                 0.621),
             4: (0.7770000000000001,
                 0.677),
             5: (0.7770000000000001,
                 0.023000000000000076),
             6: (0.12300000000000022,
                 0.023000000000000076),
             7: (0.12300000000000022,
                 0.677)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge484 = airbridges(
design,
name='Airbridge484',
options={'cpw_name': 'cpw_(5,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment788 = ShortRoute(
design,
name='short_line_Segment788',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge651 = airbridges(
design,
name='Airbridge651',
options={'cpw_name': '(5,4)CPW(4,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad191 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad191',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '1.38',
 'pos_y': '0.342',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction421 = DolanJunction(
design,
name='dolan_junction421',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': 0.21050000000000002},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee684 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee684',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7405',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path720 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path720',
options={'_actual_length': '4.035071118430775 '
                   'mm',
 'anchors': {0: (1.6604999999999999,
                 0.6225),
             1: (1.6604999999999999,
                 0.061500000000000055),
             2: (1.0995,
                 0.061500000000000055),
             3: (1.0995, 0.6225),
             4: (1.7165, 0.6785),
             5: (1.7165,
                 0.060500000000000054),
             6: (1.8005,
                 0.060500000000000054),
             7: (1.8005, 0.6785)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge600 = airbridges(
design,
name='Airbridge600',
options={'cpw_name': 'cpw_(6,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment460 = ShortRoute(
design,
name='short_line_Segment460',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge850 = airbridges(
design,
name='Airbridge850',
options={'cpw_name': '(6,4)CPW(5,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad950 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad950',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '0.35000000000000003',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction712 = DolanJunction(
design,
name='dolan_junction712',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': 0.23350000000000004},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee216 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee216',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6530000000000005',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path890 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path890',
options={'_actual_length': '3.522751118430776 '
                   'mm',
 'anchors': {0: (2.5730000000000004,
                 0.613),
             1: (2.5730000000000004,
                 0.08700000000000002),
             2: (2.0470000000000006,
                 0.08700000000000002),
             3: (2.0470000000000006,
                 0.613),
             4: (2.6290000000000004,
                 0.669),
             5: (2.6290000000000004,
                 0.23100000000000004),
             6: (2.7130000000000005,
                 0.23100000000000004),
             7: (2.7130000000000005,
                 0.669)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge972 = airbridges(
design,
name='Airbridge972',
options={'cpw_name': 'cpw_(7,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment746 = ShortRoute(
design,
name='short_line_Segment746',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge882 = airbridges(
design,
name='Airbridge882',
options={'cpw_name': '(7,4)CPW(6,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad624 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad624',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '3.24',
 'pos_y': '0.35000000000000003',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction31 = DolanJunction(
design,
name='dolan_junction31',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': 0.22300000000000003},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee877 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee877',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.5885000000000002',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path222 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path222',
options={'_actual_length': '3.875231118430775 '
                   'mm',
 'anchors': {0: (3.5085, 0.6185),
             1: (3.5085,
                 0.08150000000000007),
             2: (2.9715000000000003,
                 0.08150000000000007),
             3: (2.9715000000000003,
                 0.6185),
             4: (3.5645000000000002,
                 0.6745),
             5: (3.5645000000000002,
                 0.08050000000000007),
             6: (3.6485000000000003,
                 0.08050000000000007),
             7: (3.6485000000000003,
                 0.6745)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge202 = airbridges(
design,
name='Airbridge202',
options={'cpw_name': 'cpw_(8,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment835 = ShortRoute(
design,
name='short_line_Segment835',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge47 = airbridges(
design,
name='Airbridge47',
options={'cpw_name': '(8,4)CPW(7,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad345 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad345',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '0.36000000000000004',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction317 = DolanJunction(
design,
name='dolan_junction317',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': 0.22250000000000003},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee678 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee678',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.916500000000001',
 'pos_y': '0.8',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path805 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path805',
options={'_actual_length': '4.366071118430777 '
                   'mm',
 'anchors': {0: (4.427500000000001,
                 0.6175),
             1: (4.427500000000001,
                 0.10250000000000004),
             2: (3.912500000000001,
                 0.10250000000000004),
             3: (3.912500000000001,
                 0.6175),
             4: (4.483500000000001,
                 0.6735),
             5: (4.483500000000001,
                 0.04650000000000004),
             6: (3.856500000000001,
                 0.04650000000000004),
             7: (3.856500000000001,
                 0.6735)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,4)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,4)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge305 = airbridges(
design,
name='Airbridge305',
options={'cpw_name': 'cpw_(9,4)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment202 = ShortRoute(
design,
name='short_line_Segment202',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,4)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge787 = airbridges(
design,
name='Airbridge787',
options={'cpw_name': '(9,4)CPW(8,4)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path1000 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path1000',
options={'_actual_length': '0.9339955592153877 '
                   'mm',
 'anchors': {0: (4.75,
                 0.7099999999999997),
             1: (4.67, 0.8)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,4)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right4',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge183 = airbridges(
design,
name='Airbridge183',
options={'cpw_name': '(9,4)CPWwb_right4',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad697 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad697',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-4.2',
 'pos_y': '-0.65',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction325 = DolanJunction(
design,
name='dolan_junction325',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': -0.7925},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee946 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee946',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.8325',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path596 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path596',
options={'_actual_length': '4.167421118430775 '
                   'mm',
 'anchors': {0: (-3.9125,
                 -0.36250000000000004),
             1: (-3.9125, -0.9375),
             2: (-4.4875, -0.9375),
             3: (-4.4875,
                 -0.36250000000000004),
             4: (-3.8565,
                 -0.30650000000000005),
             5: (-3.8565, -0.9435),
             6: (-3.7725, -0.9435),
             7: (-3.7725,
                 -0.30650000000000005)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge663 = airbridges(
design,
name='Airbridge663',
options={'cpw_name': 'cpw_(0,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path5 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path5',
options={'_actual_length': '0.9637477796076935 '
                   'mm',
 'anchors': {0: (-4.75, -0.15)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,5)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left5',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge510 = airbridges(
design,
name='Airbridge510',
options={'cpw_name': '(0,5)CPWwb_left5',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad548 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad548',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-3.27',
 'pos_y': '-0.59',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction689 = DolanJunction(
design,
name='dolan_junction689',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': -0.713},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee239 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee239',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.941',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path247 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path247',
options={'_actual_length': '3.6146211184307755 '
                   'mm',
 'anchors': {0: (-3.021,
                 -0.34099999999999997),
             1: (-3.021, -0.839),
             2: (-3.519, -0.839),
             3: (-3.519,
                 -0.34099999999999997),
             4: (-2.965, -0.285),
             5: (-2.965, -0.84),
             6: (-2.881, -0.84),
             7: (-2.881, -0.285)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge191 = airbridges(
design,
name='Airbridge191',
options={'cpw_name': 'cpw_(1,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment635 = ShortRoute(
design,
name='short_line_Segment635',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge89 = airbridges(
design,
name='Airbridge89',
options={'cpw_name': '(1,5)CPW(0,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad746 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad746',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-2.34',
 'pos_y': '-0.58',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction299 = DolanJunction(
design,
name='dolan_junction299',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': -0.704},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee630 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee630',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.5885',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path457 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path457',
options={'_actual_length': '4.2942511184307754 '
                   'mm',
 'anchors': {0: (-2.0875,
                 -0.32749999999999996),
             1: (-2.0875, -0.8325),
             2: (-2.5925, -0.8325),
             3: (-2.5925,
                 -0.32749999999999996),
             4: (-2.0315,
                 -0.27149999999999996),
             5: (-2.0315, -0.8885),
             6: (-2.6485, -0.8885),
             7: (-2.6485,
                 -0.27149999999999996)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge163 = airbridges(
design,
name='Airbridge163',
options={'cpw_name': 'cpw_(2,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment677 = ShortRoute(
design,
name='short_line_Segment677',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge702 = airbridges(
design,
name='Airbridge702',
options={'cpw_name': '(2,5)CPW(1,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad417 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad417',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '-0.61',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction969 = DolanJunction(
design,
name='dolan_junction969',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': -0.7424999999999999},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee733 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee733',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.0725000000000002',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path451 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path451',
options={'_actual_length': '3.7160011184307753 '
                   'mm',
 'anchors': {0: (-1.1525, -0.3525),
             1: (-1.1525,
                 -0.8674999999999999),
             2: (-1.6675000000000002,
                 -0.8674999999999999),
             3: (-1.6675000000000002,
                 -0.3525),
             4: (-1.0965000000000003,
                 -0.2965),
             5: (-1.0965000000000003,
                 -0.8585),
             6: (-1.0125000000000002,
                 -0.8585),
             7: (-1.0125000000000002,
                 -0.2965)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge701 = airbridges(
design,
name='Airbridge701',
options={'cpw_name': 'cpw_(3,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment731 = ShortRoute(
design,
name='short_line_Segment731',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge624 = airbridges(
design,
name='Airbridge624',
options={'cpw_name': '(3,5)CPW(2,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad770 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad770',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '-0.59',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction987 = DolanJunction(
design,
name='dolan_junction987',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': -0.7275},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee844 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee844',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.7335',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path22 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path22',
options={'_actual_length': '4.366071118430775 '
                   'mm',
 'anchors': {0: (-0.22249999999999998,
                 -0.33249999999999996),
             1: (-0.22249999999999998,
                 -0.8474999999999999),
             2: (-0.7375,
                 -0.8474999999999999),
             3: (-0.7375,
                 -0.33249999999999996),
             4: (-0.16649999999999998,
                 -0.27649999999999997),
             5: (-0.16649999999999998,
                 -0.9035),
             6: (-0.7935, -0.9035),
             7: (-0.7935,
                 -0.27649999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge603 = airbridges(
design,
name='Airbridge603',
options={'cpw_name': 'cpw_(4,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment284 = ShortRoute(
design,
name='short_line_Segment284',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge105 = airbridges(
design,
name='Airbridge105',
options={'cpw_name': '(4,5)CPW(3,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad374 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad374',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '-0.6',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction973 = DolanJunction(
design,
name='dolan_junction973',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': -0.727},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee688 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee688',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.7985000000000002',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path701 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path701',
options={'_actual_length': '3.875231118430775 '
                   'mm',
 'anchors': {0: (0.7185000000000001,
                 -0.3315),
             1: (0.7185000000000001,
                 -0.8684999999999999),
             2: (0.18150000000000022,
                 -0.8684999999999999),
             3: (0.18150000000000022,
                 -0.3315),
             4: (0.7745000000000002,
                 -0.2755),
             5: (0.7745000000000002,
                 -0.8694999999999998),
             6: (0.8585000000000002,
                 -0.8694999999999998),
             7: (0.8585000000000002,
                 -0.2755)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge128 = airbridges(
design,
name='Airbridge128',
options={'cpw_name': 'cpw_(5,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment71 = ShortRoute(
design,
name='short_line_Segment71',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge859 = airbridges(
design,
name='Airbridge859',
options={'cpw_name': '(5,5)CPW(4,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad737 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad737',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '1.38',
 'pos_y': '-0.6',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction165 = DolanJunction(
design,
name='dolan_junction165',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': -0.7165},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee42 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee42',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7229999999999999',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path782 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path782',
options={'_actual_length': '3.5227511184307754 '
                   'mm',
 'anchors': {0: (1.6429999999999998,
                 -0.33699999999999997),
             1: (1.6429999999999998,
                 -0.863),
             2: (1.117, -0.863),
             3: (1.117,
                 -0.33699999999999997),
             4: (1.6989999999999998,
                 -0.28099999999999997),
             5: (1.6989999999999998,
                 -0.7190000000000001),
             6: (1.783,
                 -0.7190000000000001),
             7: (1.783,
                 -0.28099999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge508 = airbridges(
design,
name='Airbridge508',
options={'cpw_name': 'cpw_(6,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment287 = ShortRoute(
design,
name='short_line_Segment287',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge802 = airbridges(
design,
name='Airbridge802',
options={'cpw_name': '(6,5)CPW(5,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad975 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad975',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '-0.608',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction601 = DolanJunction(
design,
name='dolan_junction601',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': -0.7395},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee501 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee501',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6705000000000005',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path781 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path781',
options={'_actual_length': '4.035071118430776 '
                   'mm',
 'anchors': {0: (2.5905000000000005,
                 -0.3275),
             1: (2.5905000000000005,
                 -0.8885),
             2: (2.0295000000000005,
                 -0.8885),
             3: (2.0295000000000005,
                 -0.3275),
             4: (2.6465000000000005,
                 -0.2715),
             5: (2.6465000000000005,
                 -0.8894999999999998),
             6: (2.7305000000000006,
                 -0.8894999999999998),
             7: (2.7305000000000006,
                 -0.2715)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge896 = airbridges(
design,
name='Airbridge896',
options={'cpw_name': 'cpw_(7,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment868 = ShortRoute(
design,
name='short_line_Segment868',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge228 = airbridges(
design,
name='Airbridge228',
options={'cpw_name': '(7,5)CPW(6,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad193 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad193',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '3.24',
 'pos_y': '-0.6',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction341 = DolanJunction(
design,
name='dolan_junction341',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': -0.745},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee922 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee922',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.9730000000000003',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path354 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path354',
options={'_actual_length': '4.571361118430775 '
                   'mm',
 'anchors': {0: (3.511, -0.329),
             1: (3.511, -0.871),
             2: (2.9690000000000003,
                 -0.871),
             3: (2.9690000000000003,
                 -0.329),
             4: (3.567, -0.273),
             5: (3.567,
                 -0.9269999999999999),
             6: (2.9130000000000003,
                 -0.9269999999999999),
             7: (2.9130000000000003,
                 -0.273)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge441 = airbridges(
design,
name='Airbridge441',
options={'cpw_name': 'cpw_(8,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment43 = ShortRoute(
design,
name='short_line_Segment43',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge127 = airbridges(
design,
name='Airbridge127',
options={'cpw_name': '(8,5)CPW(7,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad148 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad148',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '-0.61',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction247 = DolanJunction(
design,
name='dolan_junction247',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': -0.7475},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee917 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee917',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '4.512500000000001',
 'pos_y': '-0.15',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path483 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path483',
options={'_actual_length': '3.8223611184307766 '
                   'mm',
 'anchors': {0: (4.432500000000001,
                 -0.3475),
             1: (4.432500000000001,
                 -0.8725),
             2: (3.9075000000000006,
                 -0.8725),
             3: (3.9075000000000006,
                 -0.3475),
             4: (4.488500000000001,
                 -0.2915),
             5: (4.488500000000001,
                 -0.8865),
             6: (4.572500000000001,
                 -0.8865),
             7: (4.572500000000001,
                 -0.2915)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,5)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,5)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge682 = airbridges(
design,
name='Airbridge682',
options={'cpw_name': 'cpw_(9,5)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment926 = ShortRoute(
design,
name='short_line_Segment926',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,5)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge633 = airbridges(
design,
name='Airbridge633',
options={'cpw_name': '(9,5)CPW(8,5)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path730 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path730',
options={'_actual_length': '0.2837477796076934 '
                   'mm',
 'anchors': {0: (4.75, -0.15)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,5)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right5',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge124 = airbridges(
design,
name='Airbridge124',
options={'cpw_name': '(9,5)CPWwb_right5',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad22 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad22',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-4.2',
 'pos_y': '-1.54',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction405 = DolanJunction(
design,
name='dolan_junction405',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': -1.663},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee534 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee534',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.871',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path696 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path696',
options={'_actual_length': '3.614621118430776 '
                   'mm',
 'anchors': {0: (-3.951, -1.291),
             1: (-3.951,
                 -1.7890000000000001),
             2: (-4.449,
                 -1.7890000000000001),
             3: (-4.449, -1.291),
             4: (-3.895, -1.235),
             5: (-3.895, -1.79),
             6: (-3.811, -1.79),
             7: (-3.811, -1.235)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge611 = airbridges(
design,
name='Airbridge611',
options={'cpw_name': 'cpw_(0,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path475 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path475',
options={'_actual_length': '1.0252477796076935 '
                   'mm',
 'anchors': {0: (-4.75, -1.1)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,6)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left6',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge36 = airbridges(
design,
name='Airbridge36',
options={'cpw_name': '(0,6)CPWwb_left6',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad881 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad881',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-3.27',
 'pos_y': '-1.6',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction329 = DolanJunction(
design,
name='dolan_junction329',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': -1.7425000000000002},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee687 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee687',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.9025',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path279 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path279',
options={'_actual_length': '4.1674211184307755 '
                   'mm',
 'anchors': {0: (-2.9825, -1.3125),
             1: (-2.9825,
                 -1.8875000000000002),
             2: (-3.5575,
                 -1.8875000000000002),
             3: (-3.5575, -1.3125),
             4: (-2.9265,
                 -1.2565000000000002),
             5: (-2.9265, -1.8935),
             6: (-2.8425, -1.8935),
             7: (-2.8425,
                 -1.2565000000000002)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge473 = airbridges(
design,
name='Airbridge473',
options={'cpw_name': 'cpw_(1,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment262 = ShortRoute(
design,
name='short_line_Segment262',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge448 = airbridges(
design,
name='Airbridge448',
options={'cpw_name': '(1,6)CPW(0,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad752 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad752',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-2.34',
 'pos_y': '-1.56',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction688 = DolanJunction(
design,
name='dolan_junction688',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': -1.6925000000000001},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee657 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee657',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.0025',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path302 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path302',
options={'_actual_length': '3.716001118430775 '
                   'mm',
 'anchors': {0: (-2.0825, -1.3025),
             1: (-2.0825,
                 -1.8175000000000001),
             2: (-2.5974999999999997,
                 -1.8175000000000001),
             3: (-2.5974999999999997,
                 -1.3025),
             4: (-2.0265,
                 -1.2465000000000002),
             5: (-2.0265, -1.8085),
             6: (-1.9425, -1.8085),
             7: (-1.9425,
                 -1.2465000000000002)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge331 = airbridges(
design,
name='Airbridge331',
options={'cpw_name': 'cpw_(2,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment74 = ShortRoute(
design,
name='short_line_Segment74',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge983 = airbridges(
design,
name='Airbridge983',
options={'cpw_name': '(2,6)CPW(1,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad739 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad739',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '-1.53',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction664 = DolanJunction(
design,
name='dolan_junction664',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': -1.654},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee236 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee236',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.6585',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path57 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path57',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-1.1575000000000002,
                 -1.2775),
             1: (-1.1575000000000002,
                 -1.7825),
             2: (-1.6625, -1.7825),
             3: (-1.6625, -1.2775),
             4: (-1.1015000000000001,
                 -1.2215),
             5: (-1.1015000000000001,
                 -1.8385),
             6: (-1.7185000000000001,
                 -1.8385),
             7: (-1.7185000000000001,
                 -1.2215)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge794 = airbridges(
design,
name='Airbridge794',
options={'cpw_name': 'cpw_(3,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment389 = ShortRoute(
design,
name='short_line_Segment389',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge883 = airbridges(
design,
name='Airbridge883',
options={'cpw_name': '(3,6)CPW(2,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad447 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad447',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '-1.56',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction449 = DolanJunction(
design,
name='dolan_junction449',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': -1.6975},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee445 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee445',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.13749999999999996',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path216 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path216',
options={'_actual_length': '3.8223611184307744 '
                   'mm',
 'anchors': {0: (-0.21749999999999997,
                 -1.2975),
             1: (-0.21749999999999997,
                 -1.8225),
             2: (-0.7424999999999999,
                 -1.8225),
             3: (-0.7424999999999999,
                 -1.2975),
             4: (-0.16149999999999998,
                 -1.2415),
             5: (-0.16149999999999998,
                 -1.8365),
             6: (-0.07749999999999996,
                 -1.8365),
             7: (-0.07749999999999996,
                 -1.2415)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge644 = airbridges(
design,
name='Airbridge644',
options={'cpw_name': 'cpw_(4,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment965 = ShortRoute(
design,
name='short_line_Segment965',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge93 = airbridges(
design,
name='Airbridge93',
options={'cpw_name': '(4,6)CPW(3,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad603 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad603',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '-1.55',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction207 = DolanJunction(
design,
name='dolan_junction207',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': -1.695},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee382 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee382',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.18300000000000016',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path368 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path368',
options={'_actual_length': '4.571361118430774 '
                   'mm',
 'anchors': {0: (0.7210000000000001,
                 -1.2790000000000001),
             1: (0.7210000000000001,
                 -1.821),
             2: (0.17900000000000021,
                 -1.821),
             3: (0.17900000000000021,
                 -1.2790000000000001),
             4: (0.7770000000000001,
                 -1.223),
             5: (0.7770000000000001,
                 -1.877),
             6: (0.12300000000000022,
                 -1.877),
             7: (0.12300000000000022,
                 -1.223)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge365 = airbridges(
design,
name='Airbridge365',
options={'cpw_name': 'cpw_(5,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment234 = ShortRoute(
design,
name='short_line_Segment234',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge369 = airbridges(
design,
name='Airbridge369',
options={'cpw_name': '(5,6)CPW(4,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad3 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad3',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '1.38',
 'pos_y': '-1.558',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction175 = DolanJunction(
design,
name='dolan_junction175',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': -1.6895},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee793 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee793',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7405',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path519 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path519',
options={'_actual_length': '4.035071118430776 '
                   'mm',
 'anchors': {0: (1.6604999999999999,
                 -1.2775),
             1: (1.6604999999999999,
                 -1.8385),
             2: (1.0995, -1.8385),
             3: (1.0995, -1.2775),
             4: (1.7165, -1.2215),
             5: (1.7165,
                 -1.8395000000000001),
             6: (1.8005,
                 -1.8395000000000001),
             7: (1.8005, -1.2215)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge221 = airbridges(
design,
name='Airbridge221',
options={'cpw_name': 'cpw_(6,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment513 = ShortRoute(
design,
name='short_line_Segment513',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge95 = airbridges(
design,
name='Airbridge95',
options={'cpw_name': '(6,6)CPW(5,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad868 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad868',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '-1.55',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction649 = DolanJunction(
design,
name='dolan_junction649',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': -1.6665},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee350 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee350',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6530000000000005',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path881 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path881',
options={'_actual_length': '3.5227511184307754 '
                   'mm',
 'anchors': {0: (2.5730000000000004,
                 -1.287),
             1: (2.5730000000000004,
                 -1.8130000000000002),
             2: (2.0470000000000006,
                 -1.8130000000000002),
             3: (2.0470000000000006,
                 -1.287),
             4: (2.6290000000000004,
                 -1.231),
             5: (2.6290000000000004,
                 -1.669),
             6: (2.7130000000000005,
                 -1.669),
             7: (2.7130000000000005,
                 -1.231)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge475 = airbridges(
design,
name='Airbridge475',
options={'cpw_name': 'cpw_(7,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment423 = ShortRoute(
design,
name='short_line_Segment423',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge521 = airbridges(
design,
name='Airbridge521',
options={'cpw_name': '(7,6)CPW(6,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad134 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad134',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '3.24',
 'pos_y': '-1.55',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction222 = DolanJunction(
design,
name='dolan_junction222',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': -1.677},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee775 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee775',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.5885000000000002',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path859 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path859',
options={'_actual_length': '3.8752311184307753 '
                   'mm',
 'anchors': {0: (3.5085, -1.2815),
             1: (3.5085, -1.8185),
             2: (2.9715000000000003,
                 -1.8185),
             3: (2.9715000000000003,
                 -1.2815),
             4: (3.5645000000000002,
                 -1.2255),
             5: (3.5645000000000002,
                 -1.8195000000000001),
             6: (3.6485000000000003,
                 -1.8195000000000001),
             7: (3.6485000000000003,
                 -1.2255)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge165 = airbridges(
design,
name='Airbridge165',
options={'cpw_name': 'cpw_(8,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment689 = ShortRoute(
design,
name='short_line_Segment689',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge5 = airbridges(
design,
name='Airbridge5',
options={'cpw_name': '(8,6)CPW(7,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad33 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad33',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '-1.54',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction6 = DolanJunction(
design,
name='dolan_junction6',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': -1.6775},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee638 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee638',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.916500000000001',
 'pos_y': '-1.1',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path222 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path222',
options={'_actual_length': '4.366071118430777 '
                   'mm',
 'anchors': {0: (4.427500000000001,
                 -1.2825),
             1: (4.427500000000001,
                 -1.7975),
             2: (3.912500000000001,
                 -1.7975),
             3: (3.912500000000001,
                 -1.2825),
             4: (4.483500000000001,
                 -1.2265000000000001),
             5: (4.483500000000001,
                 -1.8535),
             6: (3.856500000000001,
                 -1.8535),
             7: (3.856500000000001,
                 -1.2265000000000001)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,6)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,6)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge161 = airbridges(
design,
name='Airbridge161',
options={'cpw_name': 'cpw_(9,6)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment545 = ShortRoute(
design,
name='short_line_Segment545',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,6)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge975 = airbridges(
design,
name='Airbridge975',
options={'cpw_name': '(9,6)CPW(8,6)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path99 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path99',
options={'_actual_length': '0.9797477796076934 '
                   'mm',
 'anchors': {0: (4.75, -1.1)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,6)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right6',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge573 = airbridges(
design,
name='Airbridge573',
options={'cpw_name': '(9,6)CPWwb_right6',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad14 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad14',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-4.2',
 'pos_y': '-2.55',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction28 = DolanJunction(
design,
name='dolan_junction28',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': -2.6925},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee368 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee368',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.8325',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path801 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path801',
options={'_actual_length': '4.167421118430776 '
                   'mm',
 'anchors': {0: (-3.9125,
                 -2.2624999999999997),
             1: (-3.9125, -2.8375),
             2: (-4.4875, -2.8375),
             3: (-4.4875,
                 -2.2624999999999997),
             4: (-3.8565,
                 -2.2064999999999997),
             5: (-3.8565, -2.8435),
             6: (-3.7725, -2.8435),
             7: (-3.7725,
                 -2.2064999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge847 = airbridges(
design,
name='Airbridge847',
options={'cpw_name': 'cpw_(0,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path424 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path424',
options={'_actual_length': '1.1637477796076934 '
                   'mm',
 'anchors': {0: (-4.75, -2.05)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,7)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left7',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge977 = airbridges(
design,
name='Airbridge977',
options={'cpw_name': '(0,7)CPWwb_left7',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad219 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad219',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-3.27',
 'pos_y': '-2.4899999999999998',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction266 = DolanJunction(
design,
name='dolan_junction266',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': -2.6129999999999995},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee594 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee594',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.941',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path220 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path220',
options={'_actual_length': '3.614621118430777 '
                   'mm',
 'anchors': {0: (-3.021,
                 -2.2409999999999997),
             1: (-3.021, -2.739),
             2: (-3.519, -2.739),
             3: (-3.519,
                 -2.2409999999999997),
             4: (-2.965,
                 -2.1849999999999996),
             5: (-2.965,
                 -2.7399999999999998),
             6: (-2.881,
                 -2.7399999999999998),
             7: (-2.881,
                 -2.1849999999999996)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge698 = airbridges(
design,
name='Airbridge698',
options={'cpw_name': 'cpw_(1,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment779 = ShortRoute(
design,
name='short_line_Segment779',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge660 = airbridges(
design,
name='Airbridge660',
options={'cpw_name': '(1,7)CPW(0,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad770 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad770',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-2.34',
 'pos_y': '-2.48',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction705 = DolanJunction(
design,
name='dolan_junction705',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': -2.604},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee380 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee380',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.5885',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path495 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path495',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-2.0875, -2.2275),
             1: (-2.0875, -2.7325),
             2: (-2.5925, -2.7325),
             3: (-2.5925, -2.2275),
             4: (-2.0315, -2.1715),
             5: (-2.0315, -2.7885),
             6: (-2.6485, -2.7885),
             7: (-2.6485, -2.1715)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge266 = airbridges(
design,
name='Airbridge266',
options={'cpw_name': 'cpw_(2,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment72 = ShortRoute(
design,
name='short_line_Segment72',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge814 = airbridges(
design,
name='Airbridge814',
options={'cpw_name': '(2,7)CPW(1,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad113 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad113',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '-2.51',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction746 = DolanJunction(
design,
name='dolan_junction746',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': -2.6424999999999996},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee335 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee335',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.0725000000000002',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path108 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path108',
options={'_actual_length': '3.7160011184307744 '
                   'mm',
 'anchors': {0: (-1.1525, -2.2525),
             1: (-1.1525,
                 -2.7674999999999996),
             2: (-1.6675000000000002,
                 -2.7674999999999996),
             3: (-1.6675000000000002,
                 -2.2525),
             4: (-1.0965000000000003,
                 -2.1965),
             5: (-1.0965000000000003,
                 -2.7584999999999997),
             6: (-1.0125000000000002,
                 -2.7584999999999997),
             7: (-1.0125000000000002,
                 -2.1965)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge647 = airbridges(
design,
name='Airbridge647',
options={'cpw_name': 'cpw_(3,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment855 = ShortRoute(
design,
name='short_line_Segment855',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge15 = airbridges(
design,
name='Airbridge15',
options={'cpw_name': '(3,7)CPW(2,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad62 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad62',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '-2.4899999999999998',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction936 = DolanJunction(
design,
name='dolan_junction936',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': -2.6275},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee752 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee752',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.7335',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path944 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path944',
options={'_actual_length': '4.366071118430774 '
                   'mm',
 'anchors': {0: (-0.22249999999999998,
                 -2.2325),
             1: (-0.22249999999999998,
                 -2.7474999999999996),
             2: (-0.7375,
                 -2.7474999999999996),
             3: (-0.7375, -2.2325),
             4: (-0.16649999999999998,
                 -2.1765),
             5: (-0.16649999999999998,
                 -2.8034999999999997),
             6: (-0.7935,
                 -2.8034999999999997),
             7: (-0.7935, -2.1765)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge561 = airbridges(
design,
name='Airbridge561',
options={'cpw_name': 'cpw_(4,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment996 = ShortRoute(
design,
name='short_line_Segment996',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge112 = airbridges(
design,
name='Airbridge112',
options={'cpw_name': '(4,7)CPW(3,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad512 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad512',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '-2.5',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction670 = DolanJunction(
design,
name='dolan_junction670',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': -2.627},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee319 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee319',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.7985000000000002',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path275 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path275',
options={'_actual_length': '3.8752311184307753 '
                   'mm',
 'anchors': {0: (0.7185000000000001,
                 -2.2315),
             1: (0.7185000000000001,
                 -2.7685),
             2: (0.18150000000000022,
                 -2.7685),
             3: (0.18150000000000022,
                 -2.2315),
             4: (0.7745000000000002,
                 -2.1755),
             5: (0.7745000000000002,
                 -2.7695),
             6: (0.8585000000000002,
                 -2.7695),
             7: (0.8585000000000002,
                 -2.1755)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge931 = airbridges(
design,
name='Airbridge931',
options={'cpw_name': 'cpw_(5,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment337 = ShortRoute(
design,
name='short_line_Segment337',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge707 = airbridges(
design,
name='Airbridge707',
options={'cpw_name': '(5,7)CPW(4,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad332 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad332',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '1.38',
 'pos_y': '-2.5',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction37 = DolanJunction(
design,
name='dolan_junction37',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': -2.6165},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee296 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee296',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7229999999999999',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path662 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path662',
options={'_actual_length': '3.522751118430774 '
                   'mm',
 'anchors': {0: (1.6429999999999998,
                 -2.237),
             1: (1.6429999999999998,
                 -2.763),
             2: (1.117, -2.763),
             3: (1.117, -2.237),
             4: (1.6989999999999998,
                 -2.181),
             5: (1.6989999999999998,
                 -2.6189999999999998),
             6: (1.783,
                 -2.6189999999999998),
             7: (1.783, -2.181)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge107 = airbridges(
design,
name='Airbridge107',
options={'cpw_name': 'cpw_(6,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment362 = ShortRoute(
design,
name='short_line_Segment362',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge452 = airbridges(
design,
name='Airbridge452',
options={'cpw_name': '(6,7)CPW(5,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad806 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad806',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '-2.508',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction405 = DolanJunction(
design,
name='dolan_junction405',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': -2.6395},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee870 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee870',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6705000000000005',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path743 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path743',
options={'_actual_length': '4.035071118430776 '
                   'mm',
 'anchors': {0: (2.5905000000000005,
                 -2.2275),
             1: (2.5905000000000005,
                 -2.7885),
             2: (2.0295000000000005,
                 -2.7885),
             3: (2.0295000000000005,
                 -2.2275),
             4: (2.6465000000000005,
                 -2.1715),
             5: (2.6465000000000005,
                 -2.7895),
             6: (2.7305000000000006,
                 -2.7895),
             7: (2.7305000000000006,
                 -2.1715)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge668 = airbridges(
design,
name='Airbridge668',
options={'cpw_name': 'cpw_(7,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment525 = ShortRoute(
design,
name='short_line_Segment525',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge267 = airbridges(
design,
name='Airbridge267',
options={'cpw_name': '(7,7)CPW(6,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad998 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad998',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '3.24',
 'pos_y': '-2.5',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction997 = DolanJunction(
design,
name='dolan_junction997',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': -2.645},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee883 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee883',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.9730000000000003',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path54 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path54',
options={'_actual_length': '4.571361118430774 '
                   'mm',
 'anchors': {0: (3.511, -2.229),
             1: (3.511, -2.771),
             2: (2.9690000000000003,
                 -2.771),
             3: (2.9690000000000003,
                 -2.229),
             4: (3.567, -2.173),
             5: (3.567, -2.827),
             6: (2.9130000000000003,
                 -2.827),
             7: (2.9130000000000003,
                 -2.173)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge727 = airbridges(
design,
name='Airbridge727',
options={'cpw_name': 'cpw_(8,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment705 = ShortRoute(
design,
name='short_line_Segment705',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge554 = airbridges(
design,
name='Airbridge554',
options={'cpw_name': '(8,7)CPW(7,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad735 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad735',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '-2.51',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction971 = DolanJunction(
design,
name='dolan_junction971',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': -2.6475},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee678 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee678',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '4.512500000000001',
 'pos_y': '-2.05',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path836 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path836',
options={'_actual_length': '3.822361118430779 '
                   'mm',
 'anchors': {0: (4.432500000000001,
                 -2.2474999999999996),
             1: (4.432500000000001,
                 -2.7725),
             2: (3.9075000000000006,
                 -2.7725),
             3: (3.9075000000000006,
                 -2.2474999999999996),
             4: (4.488500000000001,
                 -2.1914999999999996),
             5: (4.488500000000001,
                 -2.7865),
             6: (4.572500000000001,
                 -2.7865),
             7: (4.572500000000001,
                 -2.1914999999999996)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,7)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,7)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge282 = airbridges(
design,
name='Airbridge282',
options={'cpw_name': 'cpw_(9,7)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment672 = ShortRoute(
design,
name='short_line_Segment672',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,7)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge541 = airbridges(
design,
name='Airbridge541',
options={'cpw_name': '(9,7)CPW(8,7)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path452 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path452',
options={'_actual_length': '0.4837477796076932 '
                   'mm',
 'anchors': {0: (4.75, -2.05)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,7)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right7',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge328 = airbridges(
design,
name='Airbridge328',
options={'cpw_name': '(9,7)CPWwb_right7',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad988 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad988',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-4.2',
 'pos_y': '-3.44',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction393 = DolanJunction(
design,
name='dolan_junction393',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': -3.5629999999999997},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee366 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee366',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.871',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path58 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path58',
options={'_actual_length': '3.614621118430776 '
                   'mm',
 'anchors': {0: (-3.951, -3.191),
             1: (-3.951, -3.689),
             2: (-4.449, -3.689),
             3: (-4.449, -3.191),
             4: (-3.895, -3.135),
             5: (-3.895, -3.69),
             6: (-3.811, -3.69),
             7: (-3.811, -3.135)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge606 = airbridges(
design,
name='Airbridge606',
options={'cpw_name': 'cpw_(0,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path610 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path610',
options={'_actual_length': '1.2252477796076937 '
                   'mm',
 'anchors': {0: (-4.75, -3.0)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,8)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left8',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge544 = airbridges(
design,
name='Airbridge544',
options={'cpw_name': '(0,8)CPWwb_left8',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad441 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad441',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-3.27',
 'pos_y': '-3.5',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction677 = DolanJunction(
design,
name='dolan_junction677',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': -3.6425},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee768 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee768',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.9025',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path518 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path518',
options={'_actual_length': '4.167421118430777 '
                   'mm',
 'anchors': {0: (-2.9825, -3.2125),
             1: (-2.9825, -3.7875),
             2: (-3.5575, -3.7875),
             3: (-3.5575, -3.2125),
             4: (-2.9265, -3.1565),
             5: (-2.9265,
                 -3.7935000000000003),
             6: (-2.8425,
                 -3.7935000000000003),
             7: (-2.8425, -3.1565)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge454 = airbridges(
design,
name='Airbridge454',
options={'cpw_name': 'cpw_(1,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment739 = ShortRoute(
design,
name='short_line_Segment739',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge512 = airbridges(
design,
name='Airbridge512',
options={'cpw_name': '(1,8)CPW(0,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad123 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad123',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-2.34',
 'pos_y': '-3.46',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction718 = DolanJunction(
design,
name='dolan_junction718',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': -3.5925},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee614 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee614',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.0025',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path727 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path727',
options={'_actual_length': '3.7160011184307735 '
                   'mm',
 'anchors': {0: (-2.0825, -3.2025),
             1: (-2.0825, -3.7175),
             2: (-2.5974999999999997,
                 -3.7175),
             3: (-2.5974999999999997,
                 -3.2025),
             4: (-2.0265, -3.1465),
             5: (-2.0265, -3.7085),
             6: (-1.9425, -3.7085),
             7: (-1.9425, -3.1465)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge552 = airbridges(
design,
name='Airbridge552',
options={'cpw_name': 'cpw_(2,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment26 = ShortRoute(
design,
name='short_line_Segment26',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge117 = airbridges(
design,
name='Airbridge117',
options={'cpw_name': '(2,8)CPW(1,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad891 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad891',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '-3.43',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction216 = DolanJunction(
design,
name='dolan_junction216',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': -3.5540000000000003},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee777 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee777',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.6585',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path339 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path339',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-1.1575000000000002,
                 -3.1775),
             1: (-1.1575000000000002,
                 -3.6825),
             2: (-1.6625, -3.6825),
             3: (-1.6625, -3.1775),
             4: (-1.1015000000000001,
                 -3.1215),
             5: (-1.1015000000000001,
                 -3.7385),
             6: (-1.7185000000000001,
                 -3.7385),
             7: (-1.7185000000000001,
                 -3.1215)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge32 = airbridges(
design,
name='Airbridge32',
options={'cpw_name': 'cpw_(3,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment516 = ShortRoute(
design,
name='short_line_Segment516',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge214 = airbridges(
design,
name='Airbridge214',
options={'cpw_name': '(3,8)CPW(2,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad733 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad733',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '-3.46',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction521 = DolanJunction(
design,
name='dolan_junction521',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': -3.5975},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee94 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee94',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.13749999999999996',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path638 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path638',
options={'_actual_length': '3.8223611184307775 '
                   'mm',
 'anchors': {0: (-0.21749999999999997,
                 -3.1975),
             1: (-0.21749999999999997,
                 -3.7225),
             2: (-0.7424999999999999,
                 -3.7225),
             3: (-0.7424999999999999,
                 -3.1975),
             4: (-0.16149999999999998,
                 -3.1414999999999997),
             5: (-0.16149999999999998,
                 -3.7365000000000004),
             6: (-0.07749999999999996,
                 -3.7365000000000004),
             7: (-0.07749999999999996,
                 -3.1414999999999997)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge394 = airbridges(
design,
name='Airbridge394',
options={'cpw_name': 'cpw_(4,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment1000 = ShortRoute(
design,
name='short_line_Segment1000',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge554 = airbridges(
design,
name='Airbridge554',
options={'cpw_name': '(4,8)CPW(3,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad929 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad929',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '-3.45',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction141 = DolanJunction(
design,
name='dolan_junction141',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': -3.595},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee748 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee748',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.18300000000000016',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path385 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path385',
options={'_actual_length': '4.571361118430775 '
                   'mm',
 'anchors': {0: (0.7210000000000001,
                 -3.1790000000000003),
             1: (0.7210000000000001,
                 -3.721),
             2: (0.17900000000000021,
                 -3.721),
             3: (0.17900000000000021,
                 -3.1790000000000003),
             4: (0.7770000000000001,
                 -3.123),
             5: (0.7770000000000001,
                 -3.777),
             6: (0.12300000000000022,
                 -3.777),
             7: (0.12300000000000022,
                 -3.123)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge414 = airbridges(
design,
name='Airbridge414',
options={'cpw_name': 'cpw_(5,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment830 = ShortRoute(
design,
name='short_line_Segment830',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge227 = airbridges(
design,
name='Airbridge227',
options={'cpw_name': '(5,8)CPW(4,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad303 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad303',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '1.38',
 'pos_y': '-3.458',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction940 = DolanJunction(
design,
name='dolan_junction940',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': -3.5895},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee779 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee779',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7405',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path834 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path834',
options={'_actual_length': '4.035071118430776 '
                   'mm',
 'anchors': {0: (1.6604999999999999,
                 -3.1775),
             1: (1.6604999999999999,
                 -3.7385),
             2: (1.0995, -3.7385),
             3: (1.0995, -3.1775),
             4: (1.7165, -3.1215),
             5: (1.7165, -3.7395),
             6: (1.8005, -3.7395),
             7: (1.8005, -3.1215)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge495 = airbridges(
design,
name='Airbridge495',
options={'cpw_name': 'cpw_(6,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment332 = ShortRoute(
design,
name='short_line_Segment332',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge861 = airbridges(
design,
name='Airbridge861',
options={'cpw_name': '(6,8)CPW(5,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad529 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad529',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '-3.45',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction181 = DolanJunction(
design,
name='dolan_junction181',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': -3.5665},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee174 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee174',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6530000000000005',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path816 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path816',
options={'_actual_length': '3.5227511184307745 '
                   'mm',
 'anchors': {0: (2.5730000000000004,
                 -3.1870000000000003),
             1: (2.5730000000000004,
                 -3.713),
             2: (2.0470000000000006,
                 -3.713),
             3: (2.0470000000000006,
                 -3.1870000000000003),
             4: (2.6290000000000004,
                 -3.1310000000000002),
             5: (2.6290000000000004,
                 -3.569),
             6: (2.7130000000000005,
                 -3.569),
             7: (2.7130000000000005,
                 -3.1310000000000002)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge65 = airbridges(
design,
name='Airbridge65',
options={'cpw_name': 'cpw_(7,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment263 = ShortRoute(
design,
name='short_line_Segment263',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge446 = airbridges(
design,
name='Airbridge446',
options={'cpw_name': '(7,8)CPW(6,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad52 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad52',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '3.24',
 'pos_y': '-3.45',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction179 = DolanJunction(
design,
name='dolan_junction179',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': -3.577},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee713 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee713',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.5885000000000002',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path908 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path908',
options={'_actual_length': '3.875231118430775 '
                   'mm',
 'anchors': {0: (3.5085, -3.1815),
             1: (3.5085, -3.7185),
             2: (2.9715000000000003,
                 -3.7185),
             3: (2.9715000000000003,
                 -3.1815),
             4: (3.5645000000000002,
                 -3.1255),
             5: (3.5645000000000002,
                 -3.7195),
             6: (3.6485000000000003,
                 -3.7195),
             7: (3.6485000000000003,
                 -3.1255)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge652 = airbridges(
design,
name='Airbridge652',
options={'cpw_name': 'cpw_(8,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment100 = ShortRoute(
design,
name='short_line_Segment100',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge387 = airbridges(
design,
name='Airbridge387',
options={'cpw_name': '(8,8)CPW(7,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad111 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad111',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '-3.44',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction562 = DolanJunction(
design,
name='dolan_junction562',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': -3.5775},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee692 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee692',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '3.916500000000001',
 'pos_y': '-3.0',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path960 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path960',
options={'_actual_length': '4.366071118430776 '
                   'mm',
 'anchors': {0: (4.427500000000001,
                 -3.1825),
             1: (4.427500000000001,
                 -3.6975),
             2: (3.912500000000001,
                 -3.6975),
             3: (3.912500000000001,
                 -3.1825),
             4: (4.483500000000001,
                 -3.1265),
             5: (4.483500000000001,
                 -3.7535),
             6: (3.856500000000001,
                 -3.7535),
             7: (3.856500000000001,
                 -3.1265)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,8)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,8)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge96 = airbridges(
design,
name='Airbridge96',
options={'cpw_name': 'cpw_(9,8)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment78 = ShortRoute(
design,
name='short_line_Segment78',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,8)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge893 = airbridges(
design,
name='Airbridge893',
options={'cpw_name': '(9,8)CPW(8,8)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path192 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path192',
options={'_actual_length': '1.1797477796076936 '
                   'mm',
 'anchors': {0: (4.75, -3.0)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,8)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right8',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge552 = airbridges(
design,
name='Airbridge552',
options={'cpw_name': '(9,8)CPWwb_right8',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad526 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad526',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '245.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '245.0 um',
 'pocket_width': '305.0 um',
 'pos_x': '-4.2',
 'pos_y': '-4.45',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction440 = DolanJunction(
design,
name='dolan_junction440',
options={'layer': 2,
 'orientation': 0,
 'pos_x': -4.2,
 'pos_y': -4.5925},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee762 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee762',
options={'coupling_length': '120 um',
 'coupling_space': '2.19um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-3.8325',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path438 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path438',
options={'_actual_length': '4.167421118430772 '
                   'mm',
 'anchors': {0: (-3.9125,
                 -4.1625000000000005),
             1: (-3.9125, -4.7375),
             2: (-4.4875, -4.7375),
             3: (-4.4875,
                 -4.1625000000000005),
             4: (-3.8565,
                 -4.1065000000000005),
             5: (-3.8565, -4.7435),
             6: (-3.7725, -4.7435),
             7: (-3.7725,
                 -4.1065000000000005)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(0,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge974 = airbridges(
design,
name='Airbridge974',
options={'cpw_name': 'cpw_(0,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path314 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path314',
options={'_actual_length': '1.3637477796076938 '
                   'mm',
 'anchors': {0: (-4.75, -3.95)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,9)',
                            'pin': 'prime_start'},
                'start_pin': {'component': 'wb_left9',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge208 = airbridges(
design,
name='Airbridge208',
options={'cpw_name': '(0,9)CPWwb_left9',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad732 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad732',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '206.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '206.0 um',
 'pocket_width': '266.0 um',
 'pos_x': '-3.27',
 'pos_y': '-4.390000000000001',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction93 = DolanJunction(
design,
name='dolan_junction93',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -3.27,
 'pos_y': -4.513000000000001},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee594 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee594',
options={'coupling_length': '120 um',
 'coupling_space': '3.99um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.941',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path327 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path327',
options={'_actual_length': '3.614621118430774 '
                   'mm',
 'anchors': {0: (-3.021,
                 -4.141000000000001),
             1: (-3.021, -4.639),
             2: (-3.519, -4.639),
             3: (-3.519,
                 -4.141000000000001),
             4: (-2.965,
                 -4.085000000000001),
             5: (-2.965,
                 -4.640000000000001),
             6: (-2.881,
                 -4.640000000000001),
             7: (-2.881,
                 -4.085000000000001)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(1,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge347 = airbridges(
design,
name='Airbridge347',
options={'cpw_name': 'cpw_(1,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment944 = ShortRoute(
design,
name='short_line_Segment944',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(0,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(1,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge21 = airbridges(
design,
name='Airbridge21',
options={'cpw_name': '(1,9)CPW(0,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad246 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad246',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '24.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '208.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '208.0 um',
 'pocket_width': '268.0 um',
 'pos_x': '-2.34',
 'pos_y': '-4.38',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction718 = DolanJunction(
design,
name='dolan_junction718',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -2.34,
 'pos_y': -4.504},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee493 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee493',
options={'coupling_length': '120 um',
 'coupling_space': '1.86um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-2.5885',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path299 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path299',
options={'_actual_length': '4.294251118430775 '
                   'mm',
 'anchors': {0: (-2.0875,
                 -4.1274999999999995),
             1: (-2.0875, -4.6325),
             2: (-2.5925, -4.6325),
             3: (-2.5925,
                 -4.1274999999999995),
             4: (-2.0315, -4.0715),
             5: (-2.0315,
                 -4.6884999999999994),
             6: (-2.6485,
                 -4.6884999999999994),
             7: (-2.6485, -4.0715)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(2,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge341 = airbridges(
design,
name='Airbridge341',
options={'cpw_name': 'cpw_(2,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment539 = ShortRoute(
design,
name='short_line_Segment539',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(1,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(2,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge32 = airbridges(
design,
name='Airbridge32',
options={'cpw_name': '(2,9)CPW(1,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad677 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad677',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '23.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '225.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '225.0 um',
 'pocket_width': '285.0 um',
 'pos_x': '-1.4100000000000001',
 'pos_y': '-4.41',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction992 = DolanJunction(
design,
name='dolan_junction992',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': -1.4100000000000001,
 'pos_y': -4.5425},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee532 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee532',
options={'coupling_length': '120 um',
 'coupling_space': '3.61um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-1.0725000000000002',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path203 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path203',
options={'_actual_length': '3.716001118430777 '
                   'mm',
 'anchors': {0: (-1.1525, -4.1525),
             1: (-1.1525, -4.6675),
             2: (-1.6675000000000002,
                 -4.6675),
             3: (-1.6675000000000002,
                 -4.1525),
             4: (-1.0965000000000003,
                 -4.0965),
             5: (-1.0965000000000003,
                 -4.6585),
             6: (-1.0125000000000002,
                 -4.6585),
             7: (-1.0125000000000002,
                 -4.0965)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(3,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge913 = airbridges(
design,
name='Airbridge913',
options={'cpw_name': 'cpw_(3,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment800 = ShortRoute(
design,
name='short_line_Segment800',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(2,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(3,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge38 = airbridges(
design,
name='Airbridge38',
options={'cpw_name': '(3,9)CPW(2,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad593 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad593',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '40.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '-0.48',
 'pos_y': '-4.390000000000001',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction739 = DolanJunction(
design,
name='dolan_junction739',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': -0.48,
 'pos_y': -4.527500000000001},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee110 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee110',
options={'coupling_length': '120 um',
 'coupling_space': '1.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '-0.7335',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path259 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path259',
options={'_actual_length': '4.366071118430778 '
                   'mm',
 'anchors': {0: (-0.22249999999999998,
                 -4.1325),
             1: (-0.22249999999999998,
                 -4.647500000000001),
             2: (-0.7375,
                 -4.647500000000001),
             3: (-0.7375, -4.1325),
             4: (-0.16649999999999998,
                 -4.0765),
             5: (-0.16649999999999998,
                 -4.703500000000001),
             6: (-0.7935,
                 -4.703500000000001),
             7: (-0.7935, -4.0765)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(4,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge201 = airbridges(
design,
name='Airbridge201',
options={'cpw_name': 'cpw_(4,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment202 = ShortRoute(
design,
name='short_line_Segment202',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(3,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(4,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge951 = airbridges(
design,
name='Airbridge951',
options={'cpw_name': '(4,9)CPW(3,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad410 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad410',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '27.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '214.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '214.0 um',
 'pocket_width': '274.0 um',
 'pos_x': '0.4500000000000002',
 'pos_y': '-4.4',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction262 = DolanJunction(
design,
name='dolan_junction262',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 0.4500000000000002,
 'pos_y': -4.527},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee271 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee271',
options={'coupling_length': '120 um',
 'coupling_space': '2.88um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '0.7985000000000002',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path383 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path383',
options={'_actual_length': '3.8752311184307726 '
                   'mm',
 'anchors': {0: (0.7185000000000001,
                 -4.131500000000001),
             1: (0.7185000000000001,
                 -4.6685),
             2: (0.18150000000000022,
                 -4.6685),
             3: (0.18150000000000022,
                 -4.131500000000001),
             4: (0.7745000000000002,
                 -4.075500000000001),
             5: (0.7745000000000002,
                 -4.6695),
             6: (0.8585000000000002,
                 -4.6695),
             7: (0.8585000000000002,
                 -4.075500000000001)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(5,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge401 = airbridges(
design,
name='Airbridge401',
options={'cpw_name': 'cpw_(5,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment524 = ShortRoute(
design,
name='short_line_Segment524',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(4,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(5,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge667 = airbridges(
design,
name='Airbridge667',
options={'cpw_name': '(5,9)CPW(4,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad13 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad13',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '20.0 '
                                      'um',
                           'pad_height': '30um-20.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '193.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '193.0 um',
 'pocket_width': '253.0 um',
 'pos_x': '1.38',
 'pos_y': '-4.4',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction693 = DolanJunction(
design,
name='dolan_junction693',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 1.38,
 'pos_y': -4.516500000000001},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee649 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee649',
options={'coupling_length': '120 um',
 'coupling_space': '4.36um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '1.7229999999999999',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path641 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path641',
options={'_actual_length': '3.5227511184307736 '
                   'mm',
 'anchors': {0: (1.6429999999999998,
                 -4.1370000000000005),
             1: (1.6429999999999998,
                 -4.663),
             2: (1.117, -4.663),
             3: (1.117,
                 -4.1370000000000005),
             4: (1.6989999999999998,
                 -4.081),
             5: (1.6989999999999998,
                 -4.519),
             6: (1.783, -4.519),
             7: (1.783, -4.081)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(6,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge53 = airbridges(
design,
name='Airbridge53',
options={'cpw_name': 'cpw_(6,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment347 = ShortRoute(
design,
name='short_line_Segment347',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(5,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(6,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge408 = airbridges(
design,
name='Airbridge408',
options={'cpw_name': '(6,9)CPW(5,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad648 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad648',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '30.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 22.05010056 ',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '223.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '223.0 um',
 'pocket_width': '283.0 um',
 'pos_x': '2.3100000000000005',
 'pos_y': '-4.408',
 'q3d_capacitance':  ' 22.05010056 '}
)




dolan_junction986 = DolanJunction(
design,
name='dolan_junction986',
options={'layer': 2,
 'orientation': 0,
 'pos_x': 2.3100000000000005,
 'pos_y': -4.5395},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee902 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee902',
options={'coupling_length': '120 um',
 'coupling_space': '2.54um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.6705000000000005',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path244 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path244',
options={'_actual_length': '4.035071118430777 '
                   'mm',
 'anchors': {0: (2.5905000000000005,
                 -4.1275),
             1: (2.5905000000000005,
                 -4.6885),
             2: (2.0295000000000005,
                 -4.6885),
             3: (2.0295000000000005,
                 -4.1275),
             4: (2.6465000000000005,
                 -4.0715),
             5: (2.6465000000000005,
                 -4.689500000000001),
             6: (2.7305000000000006,
                 -4.689500000000001),
             7: (2.7305000000000006,
                 -4.0715)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(7,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge610 = airbridges(
design,
name='Airbridge610',
options={'cpw_name': 'cpw_(7,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment493 = ShortRoute(
design,
name='short_line_Segment493',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(6,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(7,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge386 = airbridges(
design,
name='Airbridge386',
options={'cpw_name': '(7,9)CPW(6,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad815 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad815',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '47.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 16.96161581 ',
 'hfss_inductance': '13nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '250.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '250.0 um',
 'pocket_width': '310.0 um',
 'pos_x': '3.24',
 'pos_y': '-4.4',
 'q3d_capacitance':  ' 16.96161581 ',
 'q3d_inductance': '13nH'}
)




dolan_junction4 = DolanJunction(
design,
name='dolan_junction4',
options={'Lj': '13',
 'layer': 2,
 'orientation': 0,
 'pos_x': 3.24,
 'pos_y': -4.545},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee979 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee979',
options={'coupling_length': '120 um',
 'coupling_space': '1.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'mirror': True,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '2.9730000000000003',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path36 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path36',
options={'_actual_length': '4.571361118430775 '
                   'mm',
 'anchors': {0: (3.511,
                 -4.1290000000000004),
             1: (3.511, -4.671),
             2: (2.9690000000000003,
                 -4.671),
             3: (2.9690000000000003,
                 -4.1290000000000004),
             4: (3.567, -4.073),
             5: (3.567, -4.727),
             6: (2.9130000000000003,
                 -4.727),
             7: (2.9130000000000003,
                 -4.073)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(8,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge357 = airbridges(
design,
name='Airbridge357',
options={'cpw_name': 'cpw_(8,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment728 = ShortRoute(
design,
name='short_line_Segment728',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(7,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(8,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge550 = airbridges(
design,
name='Airbridge550',
options={'cpw_name': '(8,9)CPW(7,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)





            # WARNING
#options_connection_pads failed to have a value
rounded_single_pad499 = Round_TransmonPocket_Single(
design,
name='rounded_single_pad499',
options={'connection_pads': {'a': {'corner_radius': 'connection_pad_buffer_radius',
                           'cpw_extend': '0um',
                           'cpw_gap': 'trace_gap',
                           'cpw_width': 'trace_width',
                           'loc_H': 1,
                           'loc_W': 0,
                           'pad_cpw_extent': '10um',
                           'pad_cpw_shift': '5um',
                           'pad_gap': '15.0 '
                                      'um',
                           'pad_height': '30um-15.0 '
                                         'um',
                           'pad_width': '25.0 '
                                        'um',
                           'pocket_extent': '0um',
                           'pocket_rise': '0um',
                           'round_corners': 'True'}},
 'hfss_capacitance':  ' 27.5626257 ',
 'hfss_inductance': '8nH',
 'junction': 'True',
 'layer': 5,
 'orientation': 0,
 'pad_height': '235.0 um',
 'pad_pocket_distance_top': '40um',
 'pad_width': '235.0 um',
 'pocket_width': '295.0 um',
 'pos_x': '4.170000000000001',
 'pos_y': '-4.41',
 'q3d_capacitance':  ' 27.5626257 ',
 'q3d_inductance': '8nH'}
)




dolan_junction363 = DolanJunction(
design,
name='dolan_junction363',
options={'Lj': '8',
 'layer': 2,
 'orientation': 0,
 'pos_x': 4.170000000000001,
 'pos_y': -4.5475},

component_template=None,
)




qiskit_metal.qlibrary.couplers.coupled_line_tee48 = CoupledLineTee(
design,
name='qiskit_metal.qlibrary.couplers.coupled_line_tee48',
options={'coupling_length': '120 um',
 'coupling_space': '3.25um',
 'down_length': '40 um',
 'fillet': '30um',
 'layer': 5,
 'open_termination': False,
 'orientation': 0,
 'pos_x': '4.512500000000001',
 'pos_y': '-3.95',
 'prime_gap': '6.99 um',
 'prime_width': '12.4 um',
 'second_gap': '6.99 um',
 'second_width': '12.4 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.anchored_path639 = RouteAnchors(
design,
name='qiskit_metal.qlibrary.tlines.anchored_path639',
options={'_actual_length': '3.822361118430779 '
                   'mm',
 'anchors': {0: (4.432500000000001,
                 -4.1475),
             1: (4.432500000000001,
                 -4.6725),
             2: (3.9075000000000006,
                 -4.6725),
             3: (3.9075000000000006,
                 -4.1475),
             4: (4.488500000000001,
                 -4.0915),
             5: (4.488500000000001,
                 -4.6865000000000006),
             6: (4.572500000000001,
                 -4.6865000000000006),
             7: (4.572500000000001,
                 -4.0915)},
 'fillet': '30 um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '20um',
          'start_jogged_extension': '',
          'start_straight': '15um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,9)',
                            'pin': 'second_end'},
                'start_pin': {'component': 'qubit(9,9)',
                              'pin': 'a'}},
 'q3d_wire_bonds': True,
 'total_length': '5 mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge356 = airbridges(
design,
name='Airbridge356',
options={'cpw_name': 'cpw_(9,9)',
 'dis': '50um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




short_line_Segment773 = ShortRoute(
design,
name='short_line_Segment773',
options={'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_straight': '5um',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(8,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'TQ(9,9)',
                              'pin': 'prime_start'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

component_template=None,
)




Airbridge283 = airbridges(
design,
name='Airbridge283',
options={'cpw_name': '(9,9)CPW(8,9)',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)




qiskit_metal.qlibrary.tlines.mixed_path340 = RouteMixed(
design,
name='qiskit_metal.qlibrary.tlines.mixed_path340',
options={'_actual_length': '0.6837477796076936 '
                   'mm',
 'anchors': {0: (4.75, -3.95)},
 'fillet': '30um',
 'hfss_wire_bonds': True,
 'layer': 5,
 'lead': {'end_jogged_extension': '',
          'end_straight': '5um',
          'start_jogged_extension': '',
          'start_straight': '5um'},
 'pin_inputs': {'end_pin': {'component': 'TQ(9,9)',
                            'pin': 'prime_end'},
                'start_pin': {'component': 'wb_right9',
                              'pin': 'tie'}},
 'q3d_wirebonds': True,
 'total_length': '0.5mm',
 'trace_gap': '6.99 um',
 'trace_width': '12.4 um'},

type='CPW',
)




Airbridge462 = airbridges(
design,
name='Airbridge462',
options={'cpw_name': '(9,9)CPWwb_right9',
 'dis': '0um',
 'layer_ab': '8',
 'layer_ab_square': '9',
 'total_length': '80 um'},

component_template=None,
)



gui.rebuild()
gui.autoscale()
        