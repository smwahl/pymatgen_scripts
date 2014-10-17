#! /u/smwahl/packages/anaconda/bin/python
'''
Strip element names from POSCAR in order to work with Burkhards fm code.

May want to add this to the scaleCell function in case other scripts break
in the same way.
'''
import os,sys

def stripElements(paths):
    if isinstance(paths,str):
        pathlist = [paths]
    elif isinstance(paths,list):
        pathlist = paths
    else:
        raise TypeError('Takes a file of list of files')

    for path in pathlist:
        if not os.path.isfile(path):
            print 'File ' + path + 'not found.'
            break
        file = open(path)
        lines = file.readlines()
        file.close()
        slines = [ line.split() for line in lines ]
        slinesMod = slines[:6] + [ line[:3] for line in slines[6:]]
        linesMod = [ ' '.join(line) + '\n' for line in slinesMod ]

        outfile = open(path, "w")
        outfile.writelines( linesMod )

if __name__ == "__main__":
    # add POSCARS in each path
    paths = [ os.path.join(arg,'POSCAR') for arg in sys.argv[1:] ]

    # add refcars if they exist
    refpaths = [ os.path.join(arg,'REFCAR') for arg in sys.argv[1:] \
            if os.path.isfile(os.path.join(arg,'REFCAR') ) ]
    paths += refpaths

    # ovewrite POSCARS without element names
    stripElements(paths)


