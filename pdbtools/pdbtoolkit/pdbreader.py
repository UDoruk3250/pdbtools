import os
from pdbtools.pdbtoolkit.pdbexpressions import *


class PDBreader:
    def __init__(self):
        self.command = ""
        self.name = ""
        self.filedir = ""
        self.atomlist = []

    def importMolecule(self, file=""):

        if not file.endswith(".pdb"):
            raise InvalidFileException
        else:
            self.name = file[:-4]
            self.filedir = file
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

    def getIndexAtom(self, index=1):
        if index < 1:
            raise ValueError
        if self.atomlist:
            a = 0
            s = 0
            while s < index:
                if self.atomlist[a][0] == "ATOM":
                    s += 1
                a += 1

        else:
            raise NoSourceFileProvidedException

        return self.atomlist[a - 1]

    def PDB2FASTA(self, output_file=""):
        print(self.name)
        fasta = ""
        chain = ""
        if any("SEQRES" in s for s in self.atomlist):
            for line in self.atomlist:
                if line[0] == "SEQRES":
                    if line[2] != chain:
                        chain = line[2]
                        fasta += "\n"
                        fasta += "> Chain " + chain + ": \n  "

                    for acid in line[4:]:
                        fasta += aminoacids.get(str(acid))
        else:
            for line in self.atomlist:
                acidindex = -1
                if line[0] == "ATOM":
                    if not line[4] == chain:
                        chain = line[4]
                        fasta += "\n"
                        fasta += "> Chain " + chain + ": \n  "

                    if not line[5] == acidindex:
                        fasta += aminoacids.get(line[3])

        if output_file:
            if not os.path.exists(output_file):
                if not output_file.endswith(".fasta"):
                    output_file = output_file + ".fasta"
                with open(output_file, "w") as f:
                    f.write(fasta)
            else:
                raise FileExistsError
        return fasta


class IllegiblePDBFileException(Exception):
    def __init__(self, msg="The .PDB file is illegible; may be corrupted. Check the file."):
        super().__init__(msg)

    """The .PDB file is illegible; may be corrupted. Check the file.")"""
    pass


class NoSourceFileProvidedException(Exception):
    def __init__(self, msg="No .PDB file has been provided. Check if you are using the importMolecule() method."):
        super().__init__(msg)

    """No .PDB file has been provided. Check if you are using the importMolecule() method."""
    pass


class InvalidFileException(Exception):
    def __init__(self, msg="The file attempted to import is invalid."):
        super().__init__(msg)

    """The file attempted to import is invalid."""
    pass
