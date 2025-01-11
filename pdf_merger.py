import PyPDF2

pdffiles = [
    r"C:\Users\Home\Desktop\Nandhu\Python\Basic Python Project\DE Module I.pdf",
    r"C:\Users\Home\Desktop\Nandhu\Python\Basic Python Project\DE Module II.pdf"
]
merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    with open(filename, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)

with open('merge.pdf', 'wb') as outputFile:
    merger.write(outputFile)