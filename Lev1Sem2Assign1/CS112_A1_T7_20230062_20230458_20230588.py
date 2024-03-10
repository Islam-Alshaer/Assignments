
"""
Discrebtion: this file should perform 3 different tasks to a pdf file in the directory :
1. Merge 2 pdfs
2. Extract a page from a pdf
3. split pdf pages into seperate pdf files
Input Format: a pdf file name ending with .pdf
and a positive integer less than the number of pages in case of extract


Author:
1.Islam Waleed Salah -> 20230062 -> S21
2.Hassan Ali Hassan -> 2023 ->
3.Hesham Mohamed Koutp Fahmy -> 2023 ->

Version: 8.0
Date: 01-03-2024

Rules:
Islam  : Function split and the main body of the program
Hassan : Function Merge and extract
Hesham : Testing and revising

"""

from PyPDF2 import PdfReader, PdfMerger, PdfWriter

#discribe the program
print("Welcome to the PDF machine")
print("Please enter a choice: ")
print("1. Merge 2 files")
print("2. Extract a page from a file")
print("3. split files into seperate pages")
print("4. Exit")

choice = input("")

def take_input1():
    pdfs = ["a", "a"]
    valid = False
    while not valid:
        pdfs[0] = input("Please, enter the name of the first file: ")
        pdfs[1] = input("Please, enter the name of the second file: ")
        extension1 = pdfs[0][-4:]
        extension2 = pdfs[1][-4:]
        if extension1 == ".pdf" and extension2 == ".pdf":
            valid = True
        else:
            print("invalid input")
    return pdfs

def take_input2():

    valid = False
    while not valid:
        pdf = input("Please, enter the name of the file: ")
        extension1 = pdf[-4:]
        if extension1 == ".pdf":
            valid = True
        else:
            print("invalid input")
    return pdf



def Merge_two_files():
    pdfs2 = take_input1()
    wanted_name = input("Please, enter the name of the file you want it to have after merging, eg. my_file.pdf: ")
    while not wanted_name[-4:] == ".pdf":
        wanted_name = input("Please, enter a valid name: ")
    merger = PdfMerger()
    for pdf in pdfs2:
        merger.append(pdf)
    merger.write(wanted_name)
    merger.close()
    print("Merging done successfully")
    print("The merged pdf should be the directory with name you have entered.")


def split():
    whole_file = take_input2()

    # Extracting the file name without extension
    file_name = whole_file[:-4]

    with open(whole_file, 'rb') as my_file:
        reader = PdfReader(my_file)

        for i in range(len(reader.pages)):
            # Create a new file
            writer = PdfWriter()
            # Add the current page to that file
            writer.add_page(reader.pages[i])

            # Save the file with the name
            splitted_file = f"{file_name}_page_{i + 1}.pdf"
            with open(splitted_file, 'wb') as output_file:
                writer.write(output_file)
            print(f"file {splitted_file} done successfully")

    print("The pdf should be splitted successfully, and the PDFs should be in the directory.")



# function to extract each page of a certain pdf into a separate file
def extract(file, page):
    reader = PdfReader(file)
    with open(file, 'rb') as my_file:
        writer = PdfWriter()
        writer.add_page(reader.pages[page - 1])
        extracted_page = f"{file[:-4]}_page_{page}.pdf"
        with open(extracted_page, 'wb') as output_file:
            writer.write(output_file)
    print(f"file {extracted_page} done successfully")


#main body of the program
if choice == "1":
    Merge_two_files()
elif choice == "2":
    file_name = take_input2()
    page = input("Enter the page number")
    while not page.isnumeric():
        print("invalid input\n")
        page = input("Enter the page number")
    page = int(page)
    extract(file_name, page)
elif choice == "3":
    split()
else:
    exit()