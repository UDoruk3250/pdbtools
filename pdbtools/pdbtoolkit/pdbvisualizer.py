from pdbtools.pdbtoolkit.pdbreader import *
import Bio.PDB

try:
    import nglview as n
except ModuleNotFoundError:
    os.system("pip install nglview")


class Visualizer(PDBreader):
    def show(self):
        print(self.name)
        # print(name.upper())
        n.show_url("https://swissmodel.expasy.org/templates/"+self.name.upper())
        n.show_biopython(Bio.PDB.PDBParser().get_structure("test", self.filedir))

# class Visual(PDBreader):
#     def __init__(self):
#         super().__init__()
