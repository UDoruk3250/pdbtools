import os
from .pdbreader import *
import Bio
try:
    import nglview as n
except ModuleNotFoundError:
    os.system("pip install nglview")


class Visualize(PDBreader):

    def show(self):
        print(self.name)
        # print(name.upper())
        n.show_url("https://swissmodel.expasy.org/templates/"+self.name.upper())
        n.show_biopython()

# class Visual(PDBreader):
#     def __init__(self):
#         super().__init__()
