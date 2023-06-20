# TODO: put different kind of definitions such as Aminoacid sequences, SMILES, and FASTA sequence meanings

codon_to_pro = {
                'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
                'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S', 'ATA': 'I', 'ATC': 'I', 'ATG': 'M', 'ATT': 'I',
                'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
                'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
                'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAT': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
                'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
                'TAA': 'STOP', 'TAC': 'Y', 'TAG': 'STOP', 'TAT': 'Y', 'TCA': 'S', 'TCC': 's', 'TCG': 'S', 'TCT': 'S',
                'TGA': 'STOP', 'TGC': 'C', 'TGG': 'W', 'TGT': 'C', 'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F'
                }

# while start + 2 < len(DNA):
#         codon = DNA[start:start + 3]
#         protein.append(dna_to_pro[codon])
#         start += 3
