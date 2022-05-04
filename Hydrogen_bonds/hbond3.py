import numpy as np
import MDAnalysis
import sys
import math
import MDAnalysis.analysis.hbonds


top_file = sys.argv[1]
traj_file = sys.argv[2]


u = MDAnalysis.Universe(top_file,traj_file)

sc_sc1 = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, 'resname VAL and name N', 'resname WAT', distance=3, angle=120.0)
sc_sc2 = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, 'resname VAL and name O', 'resname WAT', distance=3, angle=120.0)
sc_sc3 = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, 'resname PHE and name N', 'resname WAT', distance=3, angle=120.0)
sc_sc4 = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, 'resname PHE and name O OXT', 'resname WAT', distance=3, angle=120.0)

sc_sc1.run(verbose=True)
sc_sc2.run(verbose=True)
sc_sc3.run(verbose=True)
sc_sc4.run(verbose=True)
#sc_sc2.run(start=100001,stop=200000,verbose=True)

sc_sc1.generate_table()
sc_sc2.generate_table()
sc_sc3.generate_table()
sc_sc4.generate_table()
print sc_sc4.table
counts1=sc_sc1.count_by_time()
counts2=sc_sc2.count_by_time()
counts3=sc_sc3.count_by_time()
counts4=sc_sc4.count_by_time()

counts1 = np.reshape(counts1["count"],(1,len(counts1)))
counts2 = np.reshape(counts2["count"],(1,len(counts2)))
counts3 = np.reshape(counts3["count"],(1,len(counts3)))
counts4 = np.reshape(counts4["count"],(1,len(counts4)))
counts = np.concatenate((counts1.T,counts2.T,counts3.T,counts4.T),axis=1)
#np.savetxt("hbond_counts.dat",counts)
#hbond_donors = sc_sc1.table["donor_index"]
#hbond_donors = np.reshape(hbond_donors,(1,len(hbond_donors)))
#hbond_acceptors = sc_sc1.table["acceptor_index"]
#hbond_acceptors = np.reshape(hbond_acceptors,(1,len(hbond_acceptors)))
#hbonds = np.concatenate((hbond_donors, hbond_acceptors))
#np.savetxt("hbonds.dat", hbonds)
#print sc_sc2.table
#wbridge_donors = sc_sc2.table["donor_index"]
#wbridge_donors = np.reshape(wbridge_donors, (1,len(wbridge_donors)))
#wbridge_acceptors = sc_sc2.table["acceptor_index"]
#wbridge_acceptors = np.reshape(wbridge_acceptors, (1,len(wbridge_acceptors)))
#wbridges = np.concatenate((wbridge_donors, wbridge_acceptors))
#wb_counts = sc_sc2.count_by_type()
#print wb_counts
#np.savetxt("wbridges3.smalltimestep.dat",wbridges, fmt='%d')
#np.savetxt("wbridges3.full.smalltimestep.dat",sc_sc2.table,fmt=('%.10f','%d','%d','%s','%d','%s','%s','%d','%s','%f','%f'))
#np.savetxt("wbridges3_counts.dat", wb_counts, fmt=('%d','%d','%s','%d','%s','%s','%d','%s','%f'))

#np.savetxt("hbonds.dat",hbonds,fmt=('%.10f','%d','%d','%s','%d','%s','%s','%d','%s','%f','%f'))
