import datetime as dt
import pandas as pd
import numpy as np
import astropy.units as u
from qiskit_metal import Dict
from qiskit_metal.analyses.quantization.lumped_capacitive import LOManalysis

class Q3DHandler:
    """Class to handle Q3D simulations for capacitance extraction"""
    
    def __init__(self, design, max_passes=20, min_passes=10, wb_threshold='72um'):
        """Initialize Q3D simulation with default parameters
        
        Args:
            design: QiskitMetal design object
            max_passes: Maximum number of convergence passes
            min_passes: Minimum number of convergence passes
            wb_threshold: Wire bond threshold length
        """
        self.design = design
        self.renderer_q3d = design.renderers.q3d
        self.q3d = LOManalysis(design, "q3d")
        
        # Configure simulation settings
        self.q3d.sim.setup.min_passes = min_passes
        self.q3d.sim.setup.max_passes = max_passes
        self.q3d.sim.setup.freq_ghz = 5
        
        # Set renderer options
        self.q3d.sim.renderer.options['wb_threshold'] = wb_threshold
        self.q3d.sim.renderer.options['x_buffer_width_mm'] = 0.5
        self.q3d.sim.renderer.options['y_buffer_width_mm'] = 0.5
        
        # Default simulation options
        self.default_options = {
            'mesh_sizes': {
                'ground_main_plane': '7um',
                'qubit_pad': '5um',
                'resonator': '10um'
            },
            'convergence_max_passes': 15,
            'convergence_min_passes': 3,
            'max_delta_p': 0.5
        }
        
    def get_timestamp(self):
        """Get current timestamp string"""
        return dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    def setup_capacitance(self, components, substrate_height='200um', gap='15um'):
        """Setup capacitance simulation parameters
        
        Args:
            components: List of component names to include
            substrate_height: Height of substrate
            gap: Coupling gap size
        """
        # Update renderer options
        self.renderer_q3d.options['substrate_height'] = substrate_height
        self.renderer_q3d.options['gap'] = gap
        
        # Setup simulation parameters
        self.q3d.sim.setup.reuse_selected_design = False
        self.q3d.sim.setup.reuse_setup = False
        self.q3d.sim.setup.max_parallel = None
        
        # Configure mesh settings
        for component, size in self.default_options['mesh_sizes'].items():
            self.renderer_q3d.mesh.assign_mesh_length(component, size)

    def run_simulation(self, components, sim_name, save_dir = None):
        """Run Q3D simulation and extract capacitance matrix
        
        Args:
            components: List of component names to simulate
            sim_name: Name for the simulation
            
        Returns:
            DataFrame with simulation results
        """
        # Initialize results dictionary
        dat = {}
        
        # Run Q3D simulation
        self.q3d.sim.run(name=sim_name, components=components)
        
        # Get capacitance matrix
        cap_matrix = self.q3d.sim.capacitance_matrix
        if cap_matrix is None:
            return pd.DataFrame()

        # Store capacitance values
        for i in range(len(cap_matrix)):
            for j in range(len(cap_matrix[i])):
                if i <= j:
                    dat[f'C{i+1}{j+1} (fF)'] = cap_matrix[i][j] * 1e15
                    
        # Store simulation parameters
        dat['substrate_height'] = self.renderer_q3d.options['substrate_height']
        dat['gap'] = self.renderer_q3d.options['gap']
        
        # Create and save dataframe
        data = pd.DataFrame(dat, index=[0])
        timestamp = self.get_timestamp()
        if save_dir is None:
            data.to_csv(f'{timestamp}_{sim_name}_q3d.csv')
        else:
            data.to_csv(f'{save_dir}/{timestamp}_{sim_name}_q3d.csv')
        
        return data

    def update_substrate(self, new_height):
        """Update substrate height parameter
        
        Args:
            new_height: New substrate height value with units
        """
        self.renderer_q3d.options['substrate_height'] = f"{new_height.to(u.um).value}um"

    def update_gap(self, new_gap):
        """Update coupling gap parameter
        
        Args:
            new_gap: New gap size value with units
        """
        self.renderer_q3d.options['gap'] = f"{new_gap.to(u.um).value}um" 