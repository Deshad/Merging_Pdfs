import PyPDF2
import os
import sys

# Get the names of both PDF files from command line arguments
file1 = sys.argv[1]
file2 = sys.argv[2]

# Get the current working directory
cwd = os.getcwd()

# Check if the provided files exist and are PDFs
for file in [file1, file2]:
    # Check if the file has a .pdf extension
    if not file.endswith('.pdf'):
        print(f"Error: The file '{file}' is not a PDF file.")
        sys.exit()

    # Check if the file exists in the current directory
    if not os.path.exists(file):
        print(f"Error: The file '{file}' does not exist in the current working directory: {cwd}")
        sys.exit()

# Merge the two PDF files
try:
    pdf1 = PyPDF2.PdfReader(file1)
    pdf2 = PyPDF2.PdfReader(file2)
    pdf_writer = PyPDF2.PdfWriter()

    # Add pages from the first PDF
    for page in pdf1.pages:
        pdf_writer.add_page(page)

    # Add pages from the second PDF
    for page in pdf2.pages:
        pdf_writer.add_page(page)

    # Save the merged PDF to a new file
    output_filename = 'merged.pdf'
    with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"Success: The PDF files have been merged and saved as '{output_filename}'.")

except Exception as e:
    print(f"An error occurred while merging the PDF files: {e}")
