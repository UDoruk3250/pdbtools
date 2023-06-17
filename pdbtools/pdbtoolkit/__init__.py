from pdbtools.pdbtoolkit.pdbtool import *
from pdbtools.pdbtoolkit.pdbreader import *
from pdbtools.pdbtoolkit.pdbvisualizer import *


class PDBToolkit(PDBreader, Visualize):
    try:
        from pdbtools.pdbtoolkit.pdbreader import *
        from pdbtools.pdbtoolkit.pdbvisualizer import *
    except Exception:
        raise ImportError


class PDBToolkit(PDBreader):
    pass
