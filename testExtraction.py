import os
from time import perf_counter 
import fitz 
import pdftotext 
import tika
from tika import parser 
import PyPDF2 
from nltk.tokenize import RegexpTokenizer

# artigo do ano de 2002 
arqPDF1 = "/Volumes/SD-64-Interno/artigosPDFbmc/1471-2318-2-3.pdf" 
# artigo do ano de 2009 
arqPDF2 = "/Volumes/SD-64-Interno/artigosPDFbmc/1471-2318-9-12.pdf"
# artigo do ano de 2016
arqPDF3 = "/Volumes/SD-64-Interno/artigosPDFbmc/s12877-016-0361-8.pdf" 
# lista de arquivos
PDFlist = [arqPDF1, arqPDF2, arqPDF3]

def salvarTexto(texto, nomeArq, nomeLib):
    arquivo = open(nomeArq + "-" + nomeLib + ".txt", "w")
    arquivo.write(texto) 
    arquivo.close()

def emitirMiniRelatorio(texto, nomeArq, nomeLib, tempoConversao):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(texto)
    print(nomeLib, " - ", nomeArq, " - Total de caracteres: ", str(len(texto)) )
    print(nomeLib, " - ", nomeArq, " - Total de palavras: ", str(len(tokens)) )
    print(nomeLib, " - ", nomeArq, " - Tempo de conversao em segundos: ", str(tempoConversao) )

def tratarPDFcomPyMuPDF(arquivos):
    for arquivo in arquivos:
        tempoInicial = perf_counter()
        doc = fitz.open(arquivo) 
        textoCompleto = ""
        for page in doc:
            texto = page.getText("text")
            textoCompleto = textoCompleto + texto
        nomeArquivo = os.path.basename(arquivo)
        tempoFinal = perf_counter()
        tempoTotal = tempoFinal - tempoInicial
        emitirMiniRelatorio(textoCompleto, nomeArquivo, "PyMuPDF", tempoTotal)
        salvarTexto(textoCompleto, nomeArquivo, "PyMuPDF")
        doc.close()
    print("--- PyMuPDF ---" )

def tratarPDFcomPdfToText(arquivos):
    for arquivo in arquivos:
        tempoInicial = perf_counter()
        textoCompleto = ""
        with open(arquivo, "rb") as f:
            doc = pdftotext.PDF(f)
            for page in doc:
                textoCompleto = textoCompleto + page
        nomeArquivo = os.path.basename(arquivo)
        tempoFinal = perf_counter()
        tempoTotal = tempoFinal - tempoInicial
        emitirMiniRelatorio(textoCompleto, nomeArquivo, "PdfToText", tempoTotal)
        salvarTexto(textoCompleto, nomeArquivo, "PdfToText")
        f.close()
    print("--- PdfToText ---" )

def tratarPDFcomTika(arquivos):
    tika.initVM()  
    for arquivo in arquivos:
        tempoInicial = perf_counter()
        textoCompleto = parser.from_file(arquivo) 
        nomeArquivo = os.path.basename(arquivo)         
        tempoFinal = perf_counter() 
        tempoTotal = tempoFinal - tempoInicial
        emitirMiniRelatorio(textoCompleto["content"], nomeArquivo, "Tika", tempoTotal)
        salvarTexto(textoCompleto["content"], nomeArquivo, "Tika") 
    print("--- Tika ---")

def tratarPDFcomPyPDF2(arquivos):
    for arquivo in arquivos:
        tempoInicial = perf_counter()
        with open(arquivo, "rb") as f:
            doc = PyPDF2.PdfFileReader(f)
            numPags = doc.getNumPages()
            textoCompleto = ""
            for i in range(numPags):
                textoCompleto = textoCompleto + doc.getPage(i).extractText()
            nomeArquivo = os.path.basename(arquivo) 
            tempoFinal = perf_counter() 
            tempoTotal = tempoFinal - tempoInicial
            emitirMiniRelatorio(textoCompleto, nomeArquivo, "PyPDF2", tempoTotal)
            salvarTexto(textoCompleto, nomeArquivo, "PyPDF2") 
    print("--- PyPDF2 ---" )

if __name__ == "__main__":
    print(PDFlist)
    tratarPDFcomPyMuPDF(PDFlist) 
    tratarPDFcomPdfToText(PDFlist)
    tratarPDFcomTika(PDFlist)
    tratarPDFcomPyPDF2(PDFlist)
