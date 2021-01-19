#imports
import pdf_to_str as pts
import str_to_wav as stw



#def
def writePdf(filename):
    text = pts.readPdf(filename)
    stw.save(text)