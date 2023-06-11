class MoleculeStructure:
    def __init__(self):
        self.command = ""
        self.atomlist = []
        self.commandlist = ["HEADER", "ATOM  ", "TER   ", "END   ", "CRYST1", "TITLE ", "REMARK", "HETATM", "COMPND",
                            "SOURCE", "KEYWDS", "EXPDTA", "AUTHOR", "REVDAT", "JRNL  ", "SEQRES", "SEQADV", "DBREF ",
                            "HET   ", "HETNAM", "HETSYN", "FORMUL", "HELIX ", "SHEET ", "SSBOND", "LINK  ", "CISPEP",
                            "ORIGX1", "ORIGX2", "ORIGX3", "SCALE1", "SCALE2", "SCALE3", "ANISOU", "CONECT", "MASTER"]
        self.aminoacids = {"ALA": "A", "ASX": "B", "CYS": "C", "ASP": "D", "GLU": "E", "PHE": "F", "GLY": "G",
                           "HIS": "H", "ILE": "I", "LYS": "K", "LEU": "L", "MET": "M", "ASN": "N", "PRO": "P",
                           "GLN": "Q", "ARG": "R", "SER": "S", "THR": "T", "VAL": "V", "TRP": "W","TYR": "Y",
                           "GLX": "Z"}

    def importMolecule(self, file=""):
        if not file.endswith(".pdb"):
            raise InvalidFileException
        else:
            try:
                with open(file) as f:
                    liste = list(f.read().split("\n"))
                    for i, element in enumerate(liste):

                        if not (element.startswith("REMARK") or element.startswith("HEADER") or element.startswith(
                                "TITLE")):
                            self.atomlist.append(list(element.split()))
                            if element.startswith("END"):
                                break
                            elif len(str(self.atomlist[-1][0])) > 6:
                                self.atomlist[-1].insert(1, self.atomlist[-1][0][6:])
                                self.atomlist[-1][0] = self.atomlist[-1][0][:6]
                        else:
                            i -= 1
            except Exception:
                raise IllegiblePDBFileException

    def getIndexAtom(self, index=0):
        if self.atomlist:
            return self.atomlist[index]

    def PDB2FASTA(self):
        fasta = ""
        chain = ""
        for line in self.atomlist:
            if line[0] == "SEQRES":
                if line[2] != chain:
                    chain = line[2]
                    fasta += "\n"
                    fasta += "> Chain " + chain + ": \n  "

                for acid in line[4:]:
                    fasta += self.aminoacids.get(str(acid))



        return fasta


class IllegiblePDBFileException(Exception):
    def __init__(self, msg="The .PDB file is illegible; may be corrupted. Check the file."):
        super().__init__(msg)

    """The .PDB file is illegible; may be corrupted. Check the file.")"""
    pass


class InvalidFileException(Exception):
    def __init__(self, msg="The file attempted to import is invalid."):
        super().__init__(msg)

    """The file attempted to import is invalid."""
    pass
