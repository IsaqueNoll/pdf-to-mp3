#imports
import pdf_to_str as pts
import str_to_mp3 as stm



#def
def writePdf(filename):
    text = pts.readPdf(filename)
    stm.save(text)