This project aims to compare a set of extractors in Python for PDF texts, specifically academic texts.

The following libraries were considered:

- PyMuPDF | https://pypi.org/project/PyMuPDF/
- pdftotext | https://pypi.org/project/pdftotext/
- Tika-Python | https://pypi.org/project/tika/
- PyPDF2 | https://pypi.org/project/PyPDF2/

The textract library was not considered for using the same algorithm as pdftotext. (textract is a wrapper for Poppler: pdftotext) | https://pypi.org/project/textract/
The observations about the extraction of the algorithm are dependent on the PDF file, its encoding process and the diversity of non-textual elements present, such as Images and Tables.

* Main features found:

- PyMuPDF | Good conversion even considering the tables. The algorithm does not consider blank line spaces, which helps in the treatment. It has a very fast conversion time.

- pdftotext | Great conversion, but it extracts the text in two columns, as in the original layout, a characteristic that will result in an error due to the combination of different phrases. It has excellent extraction quality, but for my purpose (information retrieval) it won't do.

- Tika-Python | Good conversion with URL recognition and full extraction. But the algorithm considers blank line spaces, another necessity in the treatment. Its processing time is longer than PyMuPDF, but nothing that prevents its use. It also has the disadvantage of not being native: The .jar file is downloaded in the first call of the library, a Java server is executed to serve the requests.

- PyPDF2 | Many line breaks that have not occurred in other converters. And in 3 files of the test, the extraction was unacceptable due to the total absence of spaces between words.

* Abstract:

- In this experiment, the choice should fall on the PyMuPDF or Tika-Python libraries. pdftotext is a great library, but preserves the same layout as the original text, which in certain situations is inappropriate.

** --- **

Este projeto tem como objetivo comparar um conjunto de extratores em Python para textos em PDF, especificamente, textos acadêmicos. 

As seguintes bibliotecas foram consideradas: 

- PyMuPDF | https://pypi.org/project/PyMuPDF/ 
- pdftotext | https://pypi.org/project/pdftotext/ 
- Tika-Python | https://pypi.org/project/tika/ 
- PyPDF2 | https://pypi.org/project/PyPDF2/

A biblioteca textract não foi considerada por usar o mesmo algoritmo do pdftotext. textract (is a wrapper for Poppler:pdftotext) | https://pypi.org/project/textract/ 
As observações sobre a extração do algoritmo é dependente do arquivo PDF, seu processo de codificação e diversidade de elementos não textuais presentes, como Imagens e Tabelas.

* Principais características encontradas:

- PyMuPDF | Boa conversão mesmo considerando as tabelas. O algoritmo não considera espaços de linhas em branco, o que ajuda no tratamento. Tem um tempo de conversão muito rápido.

- pdftotext | Ótima conversão porém extrai o texto em duas colunas, como na diagramação original, característica que redundará em erro pela junção de frases diferentes. Possui uma qualidade de extração excelente, mas para meu objetivo (recuperação da informação) não vai servir.

- Tika-Python | Boa conversão com reconhecimento de URLs e sua extração por completo. Mas o algoritmo considera espaços de linha em branco, mais uma necessidade no tratamento. Seu tempo de processamento é superior ao PyMuPDF, mas nada que impeça seu uso. Possui ainda a desvantagem de não ser nativo: É feito download do arquivo .jar na primeira chamada da biblioteca, um servidor Java é executado para servir às requisições.

- PyPDF2 | Muitas quebras de linha que não ocorreram em outros conversores. E em 3 arquivos do teste, a extração foi inaceitável pela total ausência de espaços entre as palavras. 

* Resumo: 

- Neste experimento a escolha deve recair sobre as bibliotecas PyMuPDF ou Tika-Python. pdftotext é uma ótima biblioteca, mas preserva a mesma diagramação do texto original, o que em determinadas situações é inadequado. 

