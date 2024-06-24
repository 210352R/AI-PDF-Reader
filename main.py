import streamlit as st
from pdfminer.high_level import extract_text
import pdf_helper

# Set page title and favicon
st.set_page_config(page_title="Upload PDF", page_icon=":file_folder:")

# Display header
st.title("Upload your PDF file")

# File size limit in megabytes
MAX_FILE_SIZE_MB = 200
# File upload widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")


# Check if a file is uploaded
if uploaded_file is not None:

    try:

        # Check the file size
        file_size_mb = uploaded_file.size / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            st.error(
                f"File size exceeds the limit of {MAX_FILE_SIZE_MB} MB. Please upload a smaller file."
            )
        else:
            # save pdf in server
            save_path = pdf_helper.save_uploaded_file(uploaded_file)
            print("Save Path : ", save_path)
            # Extract text from the uploaded PDF file
            text = extract_text(uploaded_file)

            page_count = pdf_helper.getPageCount(save_path)
            print("Page Count : ", page_count)

            st.subheader(f"Pages: {page_count}")

            # Display the extracted text on the web page
            st.subheader("Extracted Text")
            text = pdf_helper.preprocess_text(text)
            st.write(text.strip())

            # Check if the PDF has images
            uploaded_file.seek(0)  # Reset the file pointer to the beginning
            has_images = pdf_helper.pdf_has_images(uploaded_file)
            print(has_images)

    except Exception as e:
        print(e)
        st.error(f"An error occurred: {e}")
