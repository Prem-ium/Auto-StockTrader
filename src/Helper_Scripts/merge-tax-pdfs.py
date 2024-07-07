# This is a simple script that takes a folder containing PDF files and merges the specified pages from each PDF into a single output file.

# CD into the src/Helper_Scripts directory and run pip install -r requirements.txt before first usage. 
# Usage: python script.py <input_folder> <output_file> <page_numbers>
# Example:
#    python main.py C:\Users\Premium\Desktop\TaxForms\Vanguard Vanguard-Combined.pdf 3 4
# The above command will merge pages 3 and 4 from all PDF files in the "Vanguard" folder into a single PDF file named "Vanguard-Combined.pdf".


import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_folder, output_file, pages):
    writer = PdfWriter()
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(input_folder, filename)
            print(f"Processing {file_path}")
            reader = PdfReader(file_path)
            for page_num in pages:
                writer.add_page(reader.pages[page_num - 1])
                
    with open(output_file, 'wb') as out_file:
        writer.write(out_file)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <input_folder> <output_file> <page_numbers>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_file = sys.argv[2]
    pages = [int(page) for page in sys.argv[3:]]
    
    merge_pdfs(input_folder, output_file, pages)