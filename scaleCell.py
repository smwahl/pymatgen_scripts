#! /u/smwahl/packages/anaconda/bin/python

'''
scaleCell.py

Script for scaling the volume of a cell by performing a scaling of the lattice vectors 
so that length proportions and angles are preserved. Uses Pymatgens lattice.scale().
Reads in and replaces POSCAR file.

Arguments:
-------------------------------------
    volume: volume of the cell in angstrom^3

Modifies:
-------------------------------------
    POSCAR file for current run
'''  

import os, sys
from pymatgen.io.smartio import read_structure, write_structure
from pymatgen.io.vaspio import Poscar,Potcar
from shutil import copyfile,move

def scaleCell(path,volume):
    poscar = os.path.join(path,'POSCAR')
    refcar = os.path.join(path,'REFCAR')
    potcar = Potcar()

    assert os.path.isfile(poscar)

    struct = read_structure(poscar)
    struct.scale_lattice(volume)
    species = [ pot.element for pot in potcar.from_file('POTCAR') ]
    reprule = { old:new  for old,new in zip(struct.composition.elements,species) }
    struct.replace_species(reprule)

    p = Poscar(struct)

    with open(poscar) as f:
        poscomment = f.readline().strip()

    p.comment = poscomment
    p.write_file(poscar,vasp4_compatible=True)

    if os.path.isfile(refcar):
        tmp = os.path.join(path,'POSCARtmp')

        # copy Poscar to temporary file and refcar to poscar
        copyfile(poscar,tmp)
        copyfile(refcar,poscar)

        struct = read_structure(poscar)
        struct.scale_lattice(volume)
        species = [ pot.element for pot in potcar.from_file('POTCAR') ]
        reprule = { old:new  for old,new in zip(struct.composition.elements,species) }
        struct.replace_species(reprule)

        r = Poscar(struct)

        with open(poscar) as f:
            poscomment = f.readline().strip()

        r.comment = poscomment
        r.write_file(poscar,vasp4_compatible=True)

        with open(refcar) as f:
            poscomment = f.readline().strip()

        r.comment = poscomment
        r.write_file(refcar,vasp4_compatible=True)

        # replace poscar with its original
        move(tmp,poscar)
    else:
        print 'No REFCAR found.'

if __name__=="__main__":

    assert len(sys.argv) == 2, 'scaleCell.py takes only one argument'

    volume = float(sys.argv[1])

    dir = os.getcwd()

    scaleCell(dir,volume)
