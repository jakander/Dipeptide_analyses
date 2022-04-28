import numpy as np
import MDAnalysis
import MDAnalysis.analysis.hbonds as hbond


topology="VF_monomer.prmtop"
trajectory="VF_monomer.run30.dcd"

class WaterBridgeAnalysis_OtherFF(hbond.WaterBridgeAnalysis):
    DEFAULT_DONORS = {"OtherFF": tuple(set(["N"]))}
    DEFAULT_ACCEPTORS = {"OtherFF": tuple(set(["O","OXT"]))}

u = MDAnalysis.Universe(topology, trajectory)
w= hbond.WaterBridgeAnalysis(u, 'resname PHE', 'resname VAL',water_selection='resname WAT', update_selection1=True, selection1_type="acceptor", update_selection2=True, update_water_selection=True,filte_first=False, distance=4., donors="N,O",acceptors="O,OXT",forcefield='OtherFF').run(start=0, stop=10,debug=True, verbose=True)

print w.timeseries

#w.generate_table()
#print w.table
#np.savetxt("water_wire.dat", table)
