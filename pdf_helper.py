from pdfminer.high_level import extract_text, extract_pages
import fitz


def get_pdf_page_count(file_path):
    pdf_document = fitz.open(file_path)
    page_count = pdf_document.page_count
    pdf_document.close()
    return page_count


# Function to check if the PDF contains images
def pdf_has_images(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        if image_list:
            return True  # At least one image found
    return False


get_pdf_page_count("example.pdf")
