# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:18:29 2020

@author: pablonicolasr
"""

import nlp
import pandas as pd
import re

from seg import Segmentation


def getRow(originalFileName, originalText, language, index):
    
    fleshReadingEase = nlp.getfleshReadingEase(originalText)    
    numOfPunctN = nlp.getnumOfPunctN(originalText)
    typeToken = nlp.gettypeToken(originalText, language)    

    
    row = [index,
           originalFileName,           
           fleshReadingEase,           
           numOfPunctN,
           typeToken]      
    
    return row


def generate(rootPath, outputPath, file, language):    
    
    csvMode = "a"
    csvHeader = False
    csvIndex = False
    index = 1
    
    print("***Generating CSV***\n")
    
    header = [["index",
               "suspicious",               
               "fleshReadingEase",               
               "numOfPunctN",
               "typeToken"]]
      
               
    
    df = pd.DataFrame(header)    
          
    df.to_csv(outputPath, mode = csvMode, header = csvHeader, index = csvIndex)
    
    f = open(rootPath, encoding= "utf-8-sig")
    
    text = f.read() 
    
    f.close()
    
    segm = Segmentation(text)
      
    text = segm.paraSegmentation()
    
    text = [re.sub("\n", " ", sentence) for sentence in text]
    
    for j in range(len(text)):

        text2 = text[j-1]

        plagiarismRow = getRow(file, text2, language, index)        

        print("Row: " + str(plagiarismRow))

        df = pd.DataFrame([plagiarismRow])

        df.to_csv(outputPath, mode = csvMode, header = csvHeader, index = csvIndex)

        index = index + 1     
            
        
    print("\n***End generating***")
