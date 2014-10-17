#! /Users/swahl/anaconda/bin/python

# /u/smwahl/packages/anaconda/bin/python

'''
supercell.py

Script for creating a supercell from a POSCAR file of a unitcell. 

Usage:
-------------------------------------
supercell.py path_to_POSCAR_file path_to_new_POSCAR_file scalea scaleb scalec 
'''  

import os, sys
# from pymatgen.io.smartio import read_structure, write_structure
from pymatgen.io.vaspio import Poscar
# from shutil import copyfile,move

usage_stmt="Usage:\nsupercell.py path_to_POSCAR_file path_to_new_POSCAR_file scalea scaleb scalec" 

def supercell(poscar,scale,outFile=None,replace=False):
    '''Reads in a structure in VASP POSCAR format and returns one with a supercell
    of that structure

    Args:
    -------------------------------------
        poscar: location of POSCAR file to find supercell of
        scale: iterable of integer scaling factors with length 3.

    kwargs:
    -------------------------------------
        outFile: location for new poscar file with 

    modifies:
    -------------------------------------
        outFile: if replace=True
        poscar: if replace=False
    '''

    assert os.path.isfile(poscar)
    assert replace==True or not outFile is None

    p = Poscar.from_file(poscar,False)
#     with open(poscar) as f:
#         poscomment = f.readline().strip()
# 
#     p.comment = poscomment
    p.structure.make_supercell(scale)
    if replace==True:
        p.write_file(poscar,vasp4_compatible=True)
    else:
        p.write_file(outFile,vasp4_compatible=True)

if __name__=="__main__":

    assert len(sys.argv) == 6, usage_stmt
    poscar = sys.argv[1]
    target = sys.argv[2]
    scale = sys.argv[3:6]

    supercell(poscar,scale,replace=False,outFile=target)


