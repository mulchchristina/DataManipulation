fixploidy = {}
with open('fixploidy.txt') as f1:
    for line in f1:
        parts = line.strip().split('\t')
        if len(parts) >= 12:
            id_ = parts[2]  # Use column 3 from fixploidy.txt (index 2)
            ncalled = parts[6]  # HOM-REF is in column 5 (index 6)
            hom_ref = parts[9]  # HOM-REF is in column 10 (index 9)
            hom_var = parts[10]  # HOM-VAR is in column 11 (index 10)
            het = parts[11]  # HET is in column 12 (index 11)
            fixploidy[id_] = f"{ncalled}\t{hom_ref}\t{hom_var}\t{het}"
        else:
            print(f"Skipping line in fixploidy.txt due to unexpected format: {line}")

print(f"Fixploidy dictionary loaded with {len(fixploidy)} entries")

# Read paragraph_ID_AF_SampleList.txt, update with data from the dictionary, and write to a new file
with open('paragraph_ID_AF_SampleList.txt') as f2:
    lines = f2.readlines()

if lines:
    data_lines = lines  # No header in paragraph_ID_AF_SampleList.txt, so use all lines

    print(f"Processing {len(data_lines)} data lines")

    # Write output to a new file called 'updated_paragraph_ID_AF_SampleList.txt'
    with open('updated_paragraph_ID_AF_SampleList.txt', 'w') as f_out:
        for line in data_lines:
            parts = line.strip().split('\t')
            id_ = parts[0]
            # Fetch from dictionary or default to NA if ID not found
            ncalled, hom_ref, hom_var, het = fixploidy.get(id_, 'NA\tNA\tNA\tNA').split('\t')
            f_out.write(f"{line.strip()}\t{hom_ref}\t{hom_var}\t{het}\n")
else:
    print("No data lines found in paragraph_ID_AF_SampleList.txt")
