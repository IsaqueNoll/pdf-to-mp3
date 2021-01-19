#imports
from tika import parser


#definitions
def readPdf(filename):
    text = parser.from_file(filename)

    return (text['content'])
