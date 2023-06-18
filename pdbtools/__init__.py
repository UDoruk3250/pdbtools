try:
<<<<<<< HEAD
    from .pdbtool import *
    from .pdbreader import *
    from .pdbvisualizer import *
=======
    from pdbtools.pdbtoolkit.pdbtool import *
    from pdbtools.pdbtoolkit.pdbreader import *
    from pdbtools import *
>>>>>>> visualizer
except Exception:
    raise ImportError
