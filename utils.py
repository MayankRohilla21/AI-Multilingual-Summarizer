import PyPDF2

# EXTRACT TEXT FROM PDF

def extract_text_from_pdf(pdf_file):

    text = ""

    try:

        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Check if PDF is encrypted
        if pdf_reader.is_encrypted:
            return "Error: Encrypted PDF files are not supported."

        for page in pdf_reader.pages:

            extracted_text = page.extract_text()

            if extracted_text and extracted_text.strip():

                text += extracted_text.strip() + "\n\n"

        if not text.strip():
            return "No readable text found in the PDF."

        return text

    except Exception as e:

        return f"Error reading PDF: {str(e)}"