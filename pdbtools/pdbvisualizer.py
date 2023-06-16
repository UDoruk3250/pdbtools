import os
from .pdbreader import *

try:
    import nglview as n
except Exception:
    os.system("pip install nglview")



def show():

    # print(name.upper())
    print("-------------------")
    # n.show_url("https://swissmodel.expasy.org/templates/"+self.name.upper())

PDBreader.show = show

# class Visual(PDBreader):
#     def __init__(self):
#         super().__init__()
#
