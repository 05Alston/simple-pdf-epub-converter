import pikepdf

with pikepdf.open('name.pdf') as pdf:
    num_pages = len(pdf.pages)
    del pdf.pages[-1]
    pdf.save('output.pdf')