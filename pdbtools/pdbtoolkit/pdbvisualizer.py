import os
from .pdbreader import *

try:
    import nglview as n
except Exception:
    os.system("pip install nglview")


class Visualize:
    def show(self):
            # print(name.upper())
            print("-------------------")
            # n.show_url("https://swissmodel.expasy.org/templates/"+self.name.upper())
# class Visual(PDBreader):
#     def __init__(self):
#         super().__init__()
#