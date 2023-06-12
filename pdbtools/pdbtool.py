# class MoleculeStructure:
#     def __init__(self):
#         self.atomlist = []
#         self.commandlist = ["HEADER", "ATOM", "TER", "END", "CRYST1", "TITLE", "REMARK", "HETATM", "COMPND",
#         "SOURCE", "KEYWDS", "EXPDTA", "AUTHOR", "REVDAT", "JRNL", "SEQRES", "SEQADV", "DBREF", "HET", "HETNAM",
#         "HETSYN", "FORMUL", "HELIX", "SHEET", "SSBOND", "LINK", "CISPEP", "ORIGX1", "ORIGX2", "ORIGX3", "SCALE1",
#         "SCALE2", "SCALE3", "ANISOU", "CONECT", "MASTER"]
#
#     def importMolecule(self,file=""):
#         if not file.endswith(".pdb"):
#             raise InvalidFileException
#         else:
#             try:
#                 with open(file) as f:
#                     liste = list(f.read().split("\n"))
#                     for element in liste:
#                         self.atomlist.append(list(element.split()))
#
#                 self.atomlist.pop(0)
#                 self.atomlist.pop(len(self.atomlist) - 1)
#
#                 print(self.atomlist)
#                 for each in self.atomlist:
#                     if not each[0] in self.commandlist:
#                         print(each[0])
#                         raise IllegiblePDBFileException
#
#             except Exception:
#                 print(self.atomlist)
#                 raise IllegiblePDBFileException
#
#     def getIndexAtom(self, index=0):
#         if self.atomlist:
#             return self.atomlist[index]
#
#
# class IllegiblePDBFileException(Exception):
#     def __init__(self,msg = "The .PDB file is illegible; may be corrupted. Check the file."):
#         super().__init__(msg)
#     """The .PDB file is illegible; may be corrupted. Check the file.")"""
#     pass
#
#
# class InvalidFileException(Exception):
#     def __init__(self,msg = "The file attempted to import is invalid."):
#         super().__init__(msg)
#     """The file attempted to import is invalid."""
#     pass
