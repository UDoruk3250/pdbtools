try:
    from pdbtools.pdbtoolkit.pdbreader import *
    from pdbtools.pdbtoolkit.pdbvisualizer import *
    from pdbtools.pdbtoolkit.pdbtool import *
    from pdbtools.pdbtoolkit.pdbexpressions import *
except Exception:
    raise ImportError


class PDBToolkit(Visualizer):
    pass

