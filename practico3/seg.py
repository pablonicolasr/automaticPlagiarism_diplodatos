from nltk.tokenize import sent_tokenize

class Segmentation:
    
    def __init__(self, text):
        
        self.text = text
        
    def sentSegmentation(self):
        
        return sent_tokenize(self.text)
    
    def paraSegmentation(self):
        
        texto = self.text.split("\n\n")
        
        return list(filter(bool, texto))