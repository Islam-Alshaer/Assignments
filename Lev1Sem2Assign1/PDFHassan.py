from PyPDF2 import PdfMerger, PdfReader, PdfWriter # imports needed objects from the PyPDF2 library

# function to merge two files into one pdf
def merge(file1, file2):
    merger = PdfMerger() # creates the PdfMerger object
    for pdf in [file1, file2]:
        merger.append(pdf) # merges the two provided pdfs
    merger.write("mergedFile.pdf") # writes the new file
    print("Files have been merged into: mergedFile.pdf")


# function to extract each page of a certain pdf into a separate file
def extract(file):
    read = PdfReader(file) # creates the PdfReader object
    for i, page in enumerate(read.pages):
        write = PdfWriter() # creates a new PdfWriter object in each iteration
        write.add_page(page) # extracts the current page in the iteration
        with open("page_" + str(i + 1) + ".pdf", 'wb') as outputFile:
            write.write(outputFile) # write the new file with its number as the name
    print("Pages have been extracted.")


