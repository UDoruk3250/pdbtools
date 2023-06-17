try:
    from pdbtools.pdbtoolkit.pdbreader import *
    from pdbtools.pdbtoolkit.pdbvisualizer import *
    from pdbtools.pdbtoolkit.pdbtool import *
except Exception:
    raise ImportError


class PDBToolkit(Visualize):
    pass

