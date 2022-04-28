#script to read in trajectory and compute average RGYR for each residue
package require pbctools
mol new VF_monomer.prmtop type parm7 first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
mol addfile VF_monomer.run??.xyz.nc type netcdf first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all
set sidechain_outfile sidechainsim1_sasa_out.??.dat
set backbone_outfile backbonesim1_sasa_out.??.dat 
set total_outfile total_sasa.??.dat

# selection to compute SASA of
set backbonesel01 [atomselect top "protein and resid 1 2 and name N or name H1 or name H2 or name H3 or name CA or name HA or name C or name O or name H or name OXT"]
set sidechainsel01 [atomselect top "protein and resid 1 2 and name CB HB2 HB3 CG CD1 HD1 CE1 HE1 CZ HZ CE2 HE2 CD2 HD2 CG1 HG11
HG12 HG13 CG2 HG21 HG22 HG23"]
set total [atomselect top "protein"]

#fine the number of selections and the number of frames in the loaded trajectory
set nFrames [molinfo top get numframes]

#open output file
set sidechain_outstream [open $sidechain_outfile w]
set backbone_outstream [open $backbone_outfile w]
set total_outstream [open $total_outfile w]

#for each frame, update the selection to that frame, and compute sasa for the selection 
for {set k 0} {$k < $nFrames} {incr k 10} {
	$sidechainsel01 frame $k
	$sidechainsel01 update
	$backbonesel01 frame $k
	$backbonesel01 update
	$total frame $k
	$total update
	pbc box -center com -centersel "resid 1 2"
	pbc wrap -compound fragment -center com -centersel "resid 1 2"
	set backbone_total_sasa01 [measure sasa 1.4 $total -restrict $backbonesel01]
	set sidechain_total_sasa01 [measure sasa 1.4 $total -restrict $sidechainsel01]
	set total_sasa01 [measure sasa 1.4 $total]


	puts $sidechain_outstream [format "%4d %8.3f" [expr $k]  $sidechain_total_sasa01] 
	puts $backbone_outstream [format "%4d %8.3f" [expr $k]  $backbone_total_sasa01] 
	puts $total_outstream [format "%4d %8.3f" [expr $k]  $sidechain_total_sasa01] 
	puts "Frame $k finished. Next frame."
}

#close file
close $sidechain_outstream
close $backbone_outstream
close $total_outstream

quit
