import pikepdf

with pikepdf.Pdf.open('name.pdf') as my_pdf:
    for page in my_pdf.pages:
        page.Rotate = 180
    my_pdf.save('name-rotated.pdf')