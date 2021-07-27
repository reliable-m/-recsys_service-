import mimetypes
import os
import docx
import PyPDF2


class Document:

    def __init__(self, path):
        self.path = path

    def get_mime_type(self):
        return mimetypes.guess_type(self.path, strict=True)[0]

    def extractText(self):
        return textract.process(self.path)

    def read(self):
        if os.path.isfile(self.path):
            mime_type = self.get_mime_type()
            if mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = docx.Document(self.path)
                fullText = []
                for para in doc.paragraphs:
                    fullText.append(para.text)
                return '\n'.join(fullText)
            elif mime_type == "application/pdf":
                fullText = ""
                with open(self.path, 'rb') as f:
                    pdfReader = PyPDF2.PdfFileReader(f)
                    for page in range(0, pdfReader.numPages):
                        pageObj = pdfReader.getPage(page)
                        fullText = fullText + pageObj.extractText()
                return fullText
            else:
                raise ValueError(
                    'Invalid file format, please upload PDF, DOC & DOCX only!')
        else:
            raise ValueError('File could not be found!')
