#!/u/smwahl/packages/anaconda/bin/python

import sys, glob,itertools
from pymatgen.io.vaspio import Vasprun, Poscar, Chgcar, VaspInput,vasp_input,vasp_output

class Vrun 

#def readVasp(dirs):
#    if files
#
#dir = 
#input = VaspInput.from_directory("vasp_test_data/md_dft/")
#run = Vasprun("vasp_test_data/md_dft/vasprun.xml")
#
#poscar = input['POSCAR']
#kpoints = input['KPOINTS']
#potcar = input['POTCAR']

#from pymatgen.io.vaspio.vasp_output import Outcar,Dos,BandStructure,Oszicar,xml,glob


if __name__ == "__main__":
    # Parse arguments as paths (with wildcards) 
    rundirs = []
    for dname in itertools.chain(*map(glob.iglob, sys.argv[1:])):
           rundirs.append(dname) 

   runs =  readVasp(rundirs)    

   for run in runs:
       print run
