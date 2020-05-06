import os
from time import perf_counter 
import fitz 
import pdftotext 
import tika
from tika import parser 
import PyPDF2 
from nltk.tokenize import RegexpTokenizer

# artigo de 2002 - 6 paginas com 2 figuras e 5 tabelas
arqPDF1 = "/Volumes/SD-64-Interno/artigosPDFbmc/1471-2318-2-3.pdf" 
# artigo de 2007 - 12 paginas com 1 figura e 3 tabelas
arqPDF2 = "/Volumes/SD-64-Interno/artigosPDFbmc/1471-2318-7-23.pdf"
# artigo de 2009 - 9 paginas com 2 figuras e 3 tabelas
arqPDF3 = "/Volumes/SD-64-Interno/artigosPDFbmc/1471-2318-9-12.pdf"
# artigo de 2016 - 14 paginas com 1 figura
arqPDF4 = "/Volumes/SD-64-Interno/artigosPDFbmc/s12877-016-0361-8.pdf" 
# artigo de 2019 - 8 paginas com 1 figura e 4 tabelas
arqPDF5 = "/Volumes/SD-64-Interno/artigosPDFbmc/s12877-019-1283-z.pdf"
# artigo de 2019 - 12 paginas com 1 figura 
arqPDF6 = "/Volumes/SD-64-Interno/artigosPDFbmc/s12877-019-1372-z.pdf"

# lista de arqs
PDFlist = [arqPDF1, arqPDF2, arqPDF3, arqPDF4, arqPDF5, arqPDF6]

def saveText(texto, fileName, nameLib):
    """Save the text in a file

    Arguments:
        texto {str} -- text in str format
        fileName {str} -- filename (without path in this code)
        nameLib {str} -- name of extractor project
    """    
    arq = open(fileName + "-" + nameLib + ".txt", "w")
    arq.write(texto) 
    arq.close()

def printMiniReport(texto, fileName, nameLib, timeConversion):
    """Shows in the screen, some informations to help compare performance in extract file

    Arguments:
        texto {str} -- text in str format
        fileName {str} -- filename (without path in this code)
        nameLib {str} -- name of extractor project
        timeConversion {float} -- time in seconds
    """    
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(texto)
    print(nameLib, " - ", fileName, " - Total of chars: ", str(len(texto)) )
    print(nameLib, " - ", fileName, " - Total of tokens: ", str(len(tokens)) )
    print(nameLib, " - ", fileName, " - Extract time in seconds: ", str(timeConversion) )

def extractPDFwithPyMuPDF(arqs):
    """Using PyMuPDF do extract PDF text - https://pypi.org/project/PyMuPDF/

    Arguments:
        arqs {str} -- A list of filenames with path 
    """    
    for arq in arqs:
        timeIni = perf_counter()
        doc = fitz.open(arq) 
        textoCompleto = ""
        for page in doc:
            texto = page.getText("text")
            textoCompleto = textoCompleto + texto
        fileName = os.path.basename(arq)
        timeEnd = perf_counter()
        timeTotal = timeEnd - timeIni
        printMiniReport(textoCompleto, fileName, "PyMuPDF", timeTotal)
        saveText(textoCompleto, fileName, "PyMuPDF")
        doc.close()
    print("--- PyMuPDF ---" )

def extractPDFwithPdfToText(arqs):
    """Using PdfToText to extract PDF text - https://pypi.org/project/pdftotext/ 

    Arguments:
        arqs {str} -- A list of filenames with path 
    """    
    for arq in arqs:
        timeIni = perf_counter()
        textoCompleto = ""
        with open(arq, "rb") as f:
            doc = pdftotext.PDF(f)
            for page in doc:
                textoCompleto = textoCompleto + page
        fileName = os.path.basename(arq)
        timeEnd = perf_counter()
        timeTotal = timeEnd - timeIni
        printMiniReport(textoCompleto, fileName, "PdfToText", timeTotal)
        saveText(textoCompleto, fileName, "PdfToText")
        f.close()
    print("--- PdfToText ---" )

def extractPDFwithTika(arqs):
    """Using Apache Tika to extract PDF text - https://pypi.org/project/tika/ 

    Arguments:
        arqs {str} -- A list of filenames with path 
    """    
    #the time for load the Tika .jar server impact in first time of use
    tika.initVM()  
    for arq in arqs:
        timeIni = perf_counter()
        textoCompleto = parser.from_file(arq) 
        fileName = os.path.basename(arq)         
        timeEnd = perf_counter() 
        timeTotal = timeEnd - timeIni
        printMiniReport(textoCompleto["content"], fileName, "Tika", timeTotal)
        saveText(textoCompleto["content"], fileName, "Tika") 
    print("--- Tika ---")

def extractPDFwithPyPDF2(arqs):
    """Using PyPDF2 to extract PDF text - https://pypi.org/project/PyPDF2/ 

    Arguments:
        arqs {str} -- A list of filenames with path 
    """    
    for arq in arqs:
        timeIni = perf_counter()
        with open(arq, "rb") as f:
            doc = PyPDF2.PdfFileReader(f)
            numPags = doc.getNumPages()
            textoCompleto = ""
            for i in range(numPags):
                textoCompleto = textoCompleto + doc.getPage(i).extractText()
            fileName = os.path.basename(arq) 
            timeEnd = perf_counter() 
            timeTotal = timeEnd - timeIni
            printMiniReport(textoCompleto, fileName, "PyPDF2", timeTotal)
            saveText(textoCompleto, fileName, "PyPDF2") 
    print("--- PyPDF2 ---" )

if __name__ == "__main__":
    print(PDFlist)
    extractPDFwithPyMuPDF(PDFlist) 
    extractPDFwithPdfToText(PDFlist)
    extractPDFwithTika(PDFlist)
    extractPDFwithPyPDF2(PDFlist)
