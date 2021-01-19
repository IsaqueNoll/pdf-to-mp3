#imports
from tika import parser


#definitions
def readPdf():
    text = parser.from_file('sample.pdf')

    return (text['content'])