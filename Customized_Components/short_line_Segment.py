from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary.core import QComponent
import numpy as np


class ShortRoute(QComponent):
    component_metadata = Dict(short_name='cpw', _qgeometry_table_path='True')
    """Component metadata"""

    #Currently setting the primary CPW length based on the coupling_length
    #May want it to be it's own value that the user can control?
    default_options = Dict(trace_width='10um',
                           trace_gap='6um',
                           pin_inputs = Dict(
        start_pin=Dict(component = 'component1', pin = 'pin1'),
        end_pin = Dict(component = 'component2', pin = 'pin2')
                           ))
    
    def make(self):
        design = self.design
        p = self.p
        start_element = p.pin_inputs['start_pin']['component']
        start_pin = p.pin_inputs['start_pin']['pin']
        end_element = p.pin_inputs['end_pin']['component']
        end_pin = p.pin_inputs['end_pin']['pin']
        start_coord = design.components[start_element].pins[start_pin]['middle']
        end_coord = design.components[end_element].pins[end_pin]['middle']

        trace = draw.LineString([start_coord, end_coord])

        self.add_qgeometry('path', {'prime_cpw': trace},
                           width=p.trace_width,
                           layer=p.layer)
        self.add_qgeometry('path', {'prime_cpw_sub': trace},
                           width=p.trace_width + 2 * p.trace_gap,
                           subtract=True,
                           layer=p.layer)
