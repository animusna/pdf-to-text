# pdf-to-text
**pdf-to-text** is an utility to extract text content from PDF files using [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) (**Optical Character Recognition**).
This is utility use the package [**Tesseract OCR**](https://github.com/tesseract-ocr/tesseract) through the python library [**pytesseract**](https://pypi.org/project/pytesseract/). Also the utility uses the python library [**pdf2image**](https://pypi.org/project/pdf2image/) to extract images from pdf documents.

## Requirements
On your workstation you must have installed:
- Python 3.10
- TesserAct (follow the [guide](https://tesseract-ocr.github.io/tessdoc/Installation.html))
- TesserAct language pack (in case you decide to use a specific language)

## How the utility works

The utility elaborate all pdf files contained in the **input directory** (by default is **./data/in**) and produce the text content in **the output folder** (by default is **./data/out**).

### Examples

If you have in the input folders the following files:

```
data
|
|-in
|  |-mydoc-01.pdf
|  |-mydoc-02.pdf
|
```

The utility will produce the text content in the output folder like shown below.

```
data
|
|-in
|  |-mydoc-01.pdf
|  |-mydoc-02.pdf
|
|-out
|  |
|  |-mydoc-01
|  |    |
|  |    |-mydoc-01_0.pdf
|  |    |-mydoc-01_1.pdf
|  |    |-mydoc-01.txt
|  |    
|  |-mydoc-02
|  |    |
|  |    |-mydoc-02_0.pdf
|  |    |-mydoc-02_1.pdf
|  |    |-mydoc-02.txt
```

The utility will produce, for each PDF file, a text file and *n* image files where *n* is the number of the pages of the document.
