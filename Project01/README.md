# PDF Splitter Project

## Project Description
The PDF Splitter Project is a Python-based tool designed to divide large PDF files into smaller segments. This utility is ideal for managing extensive PDF documents, breaking them down into more manageable parts for easier handling and distribution.

## How to Use
1. Place your PDF files in the `input_pdfs` directory.
2. Run the `pdf_splitter.py` script located in the `src` directory.
3. Find the split PDF files in the `output_pdfs` directory.

Each PDF will be split into parts, with each part saved as a separate file in the `output_pdfs` directory. The files are named to ensure no overwriting occurs.

## Requirements
- Python 3.x
- PyPDF2

To install PyPDF2, run:

pip install PyPDF2


## Solving Common Issues
- **Deprecation Warning**: If using PyPDF2 version 3.0.0 or later, `PdfFileReader` and `PdfFileWriter` are replaced by `PdfReader` and `PdfWriter`. The script is updated to comply with these changes.

## Libraries Used
- `PyPDF2` for PDF manipulation.
- `os` for file and directory operations.

## Contributors
[nelson.sanchez@uniandes.edu.co]

## License


