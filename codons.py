def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()

    codons_dict = {}
    for row in rows:
        row = row.strip()
        cells = row.split("\t")
        codons_dict.update({cells[0]:cells[2]})
    return codons_dict


