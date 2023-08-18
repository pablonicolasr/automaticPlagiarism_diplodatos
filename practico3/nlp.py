# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:18:27 2020

@author: pablonicolasr
"""


import string
import operator
import functools
import textstat

from collections import Counter
from lexicalrichness import LexicalRichness
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag, map_tag
      
    
# Indice de Facilidad de Lectura
def getfleshReadingEase(text):
    
    fleshReadingEase = 0.0
    
    fleshReadingEase = textstat.flesch_reading_ease(text)
    
    return fleshReadingEase  
       

# Proporcion de numero de signos de puntuación en un segmento
def getnumOfPunctN(text):
    
    punctuation = string.punctuation
    
    numOfPunct = len(list(filter(functools.partial(operator.contains, punctuation), text)))
    
    count = len(word_tokenize(text))

    if (count != 0):
        
        numOfPunctN = float(numOfPunct)/float(count)
        
    else:
        
        numOfPunctN = 0     
        
    return numOfPunctN    

# La metrica Type-Token Ratio (TTR) es una medida de riqueza léxica que compara la cantidad de palabras unicas 
# (tipos) con la cantidad total de palabras (tokens) en un texto.
def gettypeToken(text, language):    
    tam = len(text)
    if tam <= 0:        
        text = 0    
    else:
        try:
            text = text.lower()
            text = LexicalRichness(text)    
            text = text.ttr
        except ZeroDivisionError:
            text = 0    
    return text



    


