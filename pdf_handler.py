import dropbox
import PyPDF2
from dropbox_config import DROPBOX_ACCESS_TOKEN

# Download files in dropbox
def download_pdf(file_path, local_path):
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    with open(local_path, "wb") as f:
        metadata, res = dbx.files_download(path=file_path)
        f.write(res.content)

# Extractb pdf 
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
