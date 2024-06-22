from pdfminer.high_level import extract_text, extract_pages
import fitz
from datetime import datetime
import os
import PyPDF4


# Helper function to generate a custom filename with timestamp
def generate_filename(filename):
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base}_{timestamp}{ext}"


# Function to save the uploaded PDF file
def save_uploaded_file(uploaded_file):
    # Generate a custom filename with a timestamp
    custom_filename = generate_filename(uploaded_file.name)
    save_path = os.path.join("uploads", custom_filename)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return save_path


# Function to check if the PDF contains images
def pdf_has_images(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        if image_list:
            return True  # At least one image found
    return False


# create a function
def getPageCount(filepath):

    # printing file path
    print("\nFile path : ", filepath)
    # creating a pdf file object
    file = open(filepath, "rb")
    # creating a pdf reader object
    readpdf = PyPDF4.PdfFileReader(file)
    # get total number of pages in pdf file
    totalpages = readpdf.numPages
    # printing number of pages in pdf file
    print("Number of pages : ", totalpages, "\n")
    return totalpages
