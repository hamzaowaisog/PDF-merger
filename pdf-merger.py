from PyPDF2 import PdfFileMerger, PdfMerger

pdfs = ['pdf1.pdf', 'pdf2.pdf', 'pdf3.pdf', 'pdf4.pdf']
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()