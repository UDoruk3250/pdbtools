class MoleculeStructure:
    def __init__(self):

        self.atomlist = []

    def importMolecule(self,file=""):
        if not file.endswith(".pdb"):
            raise InvalidFileException
        else:
            try:
                with open(file) as f:
                    liste = list(f.read().split("\n"))
                    for atom in liste:
                        self.atomlist.append(list(atom.split(" ")))
            except Exception:
                raise IllegiblePDBFileException

    def getIndexAtom(self, index=0):
        if self.atomlist:
            return self.atomlist[index]


class IllegiblePDBFileException(Exception):
    """The .PDB file is illegible; may be corrupted. Check the file."""
    pass


class InvalidFileException(Exception):
    """The file attempted to import is invalid."""
    pass