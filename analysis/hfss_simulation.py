import datetime as dt
import pandas as pd
import numpy as np
import astropy.units as u
from qiskit_metal import Dict
import analysis.Transmon_specifications as ts
from qiskit_metal.analyses.quantization import EPRanalysis


class HFSSHandler:
    """Class to handle HFSS simulations for qubit designs"""
    
    def __init__(self, design, components, nmodes=2, Ljs=['13nH'], max_passes=30, min_passes=10, conv_threshold=0.1, wb_threshold='72um'):
        """Initialize the HFSS handler and simulation
        
        Args:
            design: QiskitMetal design object
            components: List of components to simulate
            nmodes: Number of modes to simulate (default: 2)
            Ljs: List of junction inductances (default: ['13nH'])
            max_passes: Maximum number of mesh refinement passes (default: 30)
            min_passes: Minimum number of mesh refinement passes (default: 10)
            conv_threshold: Convergence threshold in % (default: 0.1)
            wb_threshold: Wavebox threshold (default: '72um')
        """
        self.design = design
        self.components = components
        self.nmodes = nmodes
        
        # Initialize HFSS simulation
        self.eig_all = EPRanalysis(self.design, 'hfss')
        self.renderer_hfss = self.design.renderers.hfss
        self.hfss = self.eig_all.sim.renderer
        self.eig_all.sim.renderer.options['wb_threshold'] = wb_threshold

        # Setup simulation parameters
        self.eig_all.sim.setup.max_passes = max_passes
        self.eig_all.sim.setup.min_passes = min_passes
        self.eig_all.sim.setup.max_delta_f = conv_threshold
        self.eig_all.sim.setup.n_modes = nmodes
        self.eig_all.sim.renderer.options['x_buffer_width_mm'] = 0.5
        self.eig_all.sim.renderer.options['y_buffer_width_mm'] = 0.5
        
        # Set junction parameters
        for i, Lj in enumerate(Ljs):
            self.eig_all.sim.setup.vars[f'Lj{i+1}'] = Lj
            self.eig_all.sim.setup.vars[f'Cj{i+1}'] = f'{(ts.find_junction_capacitance(float(Lj[:-2])*u.nH)).to(u.fF).value}fF'
        

        # Default simulation options
        self.default_options = {
            'max_mesh_length_jj': '7um',
            'max_mesh_length_port': '7um',
            '_Rj': 0,
        }
        
    def get_timestamp(self):
        """Get current timestamp string"""
        return dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    def setup_junction(self, qubit_name, Lj, Cj):
        """Setup junction parameters
        
        Args:
            qubit_name: Name of qubit component
            Lj: Junction inductance (with units)
            Cj: Junction capacitance (with units)
        """
        # Convert to strings with units if needed
        Lj_str = f"{Lj.to(u.nH).value}nH" if hasattr(Lj, 'unit') else Lj
        Cj_str = f"{Cj.to(u.fF).value}fF" if hasattr(Cj, 'unit') else Cj
        
        # Update renderer options
        self.eig_all.sim.renderer.options['Lj'] = Lj_str
        self.eig_all.sim.renderer.options['Cj'] = Cj_str
        
        # Update setup variables
        self.eig_all.sim.setup.vars['Lj'] = Lj_str
        self.eig_all.sim.setup.vars['Cj'] = Cj_str
        
        # Setup junction definition
        try:
            del self.eig_all.setup.junctions['jj']
        except:
            pass
            
        self.eig_all.setup.junctions.jj1 = Dict(
            rect=f'JJ_rect_Lj_{qubit_name}_rect_jj',
            line=f'JJ_Lj_{qubit_name}_rect_jj_',
            Lj_variable='Lj',
            Cj_variable='Cj'
        )

    def run_simulation(self, qubit, components, target_freq, sim_name, save_dir = None):
        """Run HFSS simulation and EPR analysis
        
        Args:
            qubit: Qubit object with L property
            components: List of component names to simulate, start with qubit first
            target_freq: Target frequency in GHz
            sim_name: Name for the simulation
            
        Returns:
            DataFrame with simulation results
        """
        # Initialize results dictionary
        dat = {
            'f_target': target_freq
        }
        
        # Setup junction parameters
        self.setup_junction(components[0], qubit.L, ts.find_junction_capacitance(qubit.L))
        
        # Run HFSS simulation
        self.eig_all.sim.run(name=sim_name, components=components)
        
        # Get convergence data
        convergence = pd.read_csv('hfss_eig_f_convergence.csv')
        conv = convergence.dropna()
        
        # Store frequencies
        ind = list(conv.keys())[1:]
        for i in range(self.nmodes):
            freq = conv[ind[i]].values[-1]
            dat[f'Freq{i+1}(GHz)'] = freq
            
        # Run EPR analysis
        self.eig_all.run_epr()
        chi = self.eig_all.sim.renderer.epr_quantum_analysis.get_chis().to_numpy()
        freq_EPR = self.eig_all.sim.renderer.epr_quantum_analysis.get_frequencies().to_numpy()[:,0]
        
        # Store EPR results
        for i in range(self.nmodes):
            freq = freq_EPR[i]
            dat[f'Freq_EPR{i+1}(MHz)'] = freq
            for j in range(i+1):
                dat[f'Chi{i+1}_{j+1}(MHz)'] = chi[i][j]
                
        # Create and save dataframe
        data = pd.DataFrame(dat, index=[0])
        timestamp = self.get_timestamp()
        if save_dir is None:
            data.to_csv(f'{timestamp}_{sim_name}.csv')
        else:
            data.to_csv(f'{save_dir}/{timestamp}_{sim_name}.csv')
        
        return data

    def change_inductance(self, Lj_value):
        """Change junction inductance
        
        Args:
            Lj_value: New inductance value (with units)
        """
        Lj_str = f"{Lj_value.to(u.nH).value}nH" if hasattr(Lj_value, 'unit') else Lj_value
        self.eig_all.sim.renderer.options['Lj'] = Lj_str
        self.eig_all.sim.setup.vars['Lj'] = Lj_str 