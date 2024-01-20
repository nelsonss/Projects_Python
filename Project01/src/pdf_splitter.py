import PyPDF2
import os


def split_pdf(input_pdf_path, output_folder, pages_per_file):
    file_name = os.path.basename(input_pdf_path).replace('.pdf', '')
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for start_page in range(0, num_pages, pages_per_file):
            writer = PyPDF2.PdfWriter()
            end_page = min(start_page + pages_per_file, num_pages)

            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])

            output_pdf_path = os.path.join(output_folder, f'{file_name}_part_{start_page // pages_per_file + 1}.pdf')
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)
            print(f"Generated: {output_pdf_path}")


def main():
    input_folder = '../input_pdfs'
    output_folder = '../output_pdfs'
    pages_per_file = 48  # Modify as needed

    for pdf_file in os.listdir(input_folder):
        if pdf_file.endswith('.pdf'):
            split_pdf(os.path.join(input_folder, pdf_file), output_folder, pages_per_file)


if __name__ == "__main__":
    main()
