#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import string
import operator
import functools
import glob
import os
import matplotlib.colors as mc
import nltk
import numpy as np
import textstat
import unicodedata
import pandas as pd

import textstat
from lexicalrichness import LexicalRichness
from collections import Counter

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag, map_tag
from nltk.tokenize import sent_tokenize

 # Feature Selection
from sklearn.feature_selection import VarianceThreshold


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


# In[2]:


engine = create_engine("sqlite:///mentoriam11.sqlite3", echo=True)


# Crea una clase base declarativa
Base = declarative_base()

# Define la clase "Documento"
class Documento(Base):
    __tablename__ = 'documento'

    id_documento = Column(Integer, primary_key=True)
    filename = Column(String)
    text = Column(String)
    segmentos = relationship('Segmento', backref='documento')

# Define la clase "Segmento"
class Segmento(Base):
    __tablename__ = 'segmento'

    id_segmento = Column(Integer, primary_key=True)
    segmento_texto = Column(String)
    segmento_limpio = Column(String)
    init_s = Column(Integer)
    length = Column(Integer)
    id_documento = Column(Integer, ForeignKey('documento.id_documento'))

# Crea las tablas en la base de datos
Base.metadata.create_all(engine)


# In[3]:


df = pd.read_csv(os.path.join(os.getcwd(), "intrinsic.csv"))
df


# In[4]:


class Segmentation:
    
    def __init__(self, text):
        
        self.text = text
        
    def sentSegmentation(self):
        
        return sent_tokenize(self.text)
    
    def paraSegmentation(self):
        
        texto = self.text.split("\n\n")
        
        return list(filter(bool, texto))


# In[5]:


SPECIAL_CHARACTERS = []

SPECIAL_CHARACTERS.extend(map(chr, range(0, 32)))
SPECIAL_CHARACTERS.extend(map(chr, range(33, 48)))
SPECIAL_CHARACTERS.extend(map(chr, range(58, 65)))
SPECIAL_CHARACTERS.extend(map(chr, range(91, 97)))
SPECIAL_CHARACTERS.extend(map(chr, range(123, 225)))
SPECIAL_CHARACTERS.extend(map(chr, range(226, 233)))
SPECIAL_CHARACTERS.extend(map(chr, range(234, 237)))
SPECIAL_CHARACTERS.extend(map(chr, range(238, 241)))
SPECIAL_CHARACTERS.extend(map(chr, range(242, 243)))
SPECIAL_CHARACTERS.extend(map(chr, range(244, 250)))
SPECIAL_CHARACTERS.extend(map(chr, range(251, 880)))


# In[6]:


class CleanText():
    
    def __init__(self, text, language="english"):
        
        self.text = text
        
        self.language = language
        
        self.clean_text = None
        
        self.remove_spec_text = None
        
        self.remove_stop_text = None
        
        self.lemma_text = None
    
    def removePatterns(self):
        
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        
        self.text = str(self.text)
        
        self.clean_text = self.text.lower()
        
        self.clean_text = re.sub(r"\s{2,}", " ", self.clean_text)
        
        self.clean_text = re.sub(r"\n", " ", self.clean_text)
        
        self.clean_text = re.sub(r"\d+", " ", self.clean_text)
        
        self.clean_text = re.sub(r"^\s+", " ", self.clean_text)
        
        self.clean_text = re.sub(r"\s+", " ", self.clean_text)
        
        for a, b in replacements:
            
            self.clean_text = self.clean_text.replace(a, b).replace(a.upper(), b.upper())
        
        return self.clean_text
    
    def removeSpecChars(self):
        
        remove_patterns = self.removePatterns()
        
        tokens = list(word_tokenize(remove_patterns))
        
        clean_tokens = tokens.copy()
        
        for i in range(len(clean_tokens)):
            
            for special_character in SPECIAL_CHARACTERS:
            
                clean_tokens[i] = clean_tokens[i].replace(special_character, '')            
            
        clean_tokens = [token for token in clean_tokens if token]        
        
        self.remove_spec_text = " ".join(clean_tokens)        
        
        return self.remove_spec_text    


# In[7]:


Session = sessionmaker(bind=engine)
    
session = Session()


# In[ ]:


j = 0

for i, row in enumerate(df.itertuples(), 1):
    
    print(row)
    
    # Crea una instancia de la clase que representa tu tabla y asigna los valores
    documento = Documento(
        id_documento=row.index,  # Reemplaza 'columna1' con el nombre de tus columnas del CSV
        filename=row.filename,
        text=row.text
    )
    session.add(documento)
    
    seg = Segmentation(row.text).paraSegmentation()
    
    tam = 0
    
    for s in seg:
        
        j += 1
        
        init = tam
        
        length = len(s)
        
        segmento = Segmento(
            id_segmento=j,  
            segmento_texto=s,
            segmento_limpio=CleanText(s).removeSpecChars(),
            init_s=init,
            length=length,
        )
        
        segmento.documento = documento
        
        session.add(segmento)
        
        tam += length


# In[ ]:


session.commit()  # Realiza la transacción en la base de datos
session.close() 


# In[ ]:




