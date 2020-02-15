#!/usr/bin/env python
# coding: utf-8

import PyPDF2
import pyttsx3

#Function to extract text from the PDF file

def extract_text(filename):
  
    pdfFileObj = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    mytext = ""

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        mytext += pageObj.extractText()

    pdfFileObj.close()
    
    return mytext


#Function to read out the text

def speak_text(text):
  
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('voice', 'en+m7')
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text = extract_text("PDFToText.pdf")
    speak_text(text)

