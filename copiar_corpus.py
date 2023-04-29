# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:04:20 2022

@author: pablonicolasr
"""

import os
import shutil

path = os.path.join(os.getcwd(), "intrinsic", "pan-plagiarism-corpus-2011", "intrinsic-detection-corpus", "suspicious-document")

corpus_path = os.path.join(os.getcwd(), "corpus")

if not os.path.exists(corpus_path):
    os.makedirs(corpus_path)

for folder, sub_folders, files in os.walk(path):
    
    print("Currently looking at folder: "+ folder)
    print("\n")
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold )
    print("\n")
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+ f)
        absolute_path = os.path.join(path, folder, f)
        shutil.copy2(absolute_path, "./corpus" + "/" + f)
        
    
    print("\n")
    


