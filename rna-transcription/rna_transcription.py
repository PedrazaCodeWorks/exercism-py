def to_rna(dna_strand):
    t = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(t)

