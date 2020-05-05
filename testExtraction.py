import os
from time import perf_counter 
import fitz 
import pdftotext 

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

def tratarPDFcomPyMuPDF(arquivos):
    tempoInicial = perf_counter()
    for arquivo in arquivos:
        doc = fitz.open(arquivo) 
        textoCompleto = ""
        for page in doc:
            texto = page.getText("text")
            textoCompleto = textoCompleto + texto
        nomeArquivo = os.path.basename(arquivo)
        salvarTexto(textoCompleto, nomeArquivo, "PyMuPDF")
        doc.close()
    tempoFinal = perf_counter()
    tempoTotal = tempoFinal - tempoInicial
    print("Tempo total em segundos - PyMuPDF ", tempoTotal )

def tratarPDFcomPdfToText(arquivos):
    tempoInicial = perf_counter()
    for arquivo in arquivos:
        textoCompleto = ""
        with open(arquivo, "rb") as f:
            doc = pdftotext.PDF(f)
            for page in doc:
                textoCompleto = textoCompleto + page
        nomeArquivo = os.path.basename(arquivo)
        salvarTexto(textoCompleto, nomeArquivo, "PdfToText")
        f.close()
    tempoFinal = perf_counter()
    tempoTotal = tempoFinal - tempoInicial
    print("Tempo total em segundos - PdfToText ", tempoTotal )

if __name__ == "__main__":
    print(PDFlist)
    tratarPDFcomPyMuPDF(PDFlist) 
    tratarPDFcomPdfToText(PDFlist)
