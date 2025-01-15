class Libro:
    def __init__(self,titolo, autore, anno_pubbl):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubbl = anno_pubbl
    
    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno di pubblicazione: {self.anno_pubbl}"
