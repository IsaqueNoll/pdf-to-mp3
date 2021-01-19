#imports
import pdf-to-str
import str-to-wav



#def
def writePdf(filename):
    text = pdf-to-str.readPdf(filename)
    str-to-wav.save(text)