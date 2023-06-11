class MoleculeStructure:
    def __init__(self):

        self.atomlist = []

    def importMolecule(self,file=""):
        try:
            with open(file) as f:
                liste=[]
                liste = list(f.read().split("\n"))
                for atom in liste:
                    self.atomlist.append(list(atom.split(" ")))
        except FileNotFoundError:
            raise FileNotFoundError


    def getIndexAtom(self, index=0):
        if self.atomlist:
            return self.atomlist[0]

