#


from PyPDF2 import PdfReader, PdfMerger, PdfWriter, PdfFileReader, PdfFileWriter

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

if choice == "1":
    Merge_two_files()
# elif choice == "2":
#     Extract()
elif choice == "3":
    split()
# else
#     exit()