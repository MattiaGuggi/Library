
class Utente:
    def __init__(self,nome):
        self.nome = nome
        self.libri_prestiti = []

    #Metodo per aggiungere un libro alla lista di quelli in prestito
    def prendi_libro(self,libro):
        self.libri_prestiti.append(libro)
    
    #Metodo per restituire un libro alla biblioteca
    def restituisci_libro(self,libroDaTogliere):
        self.libri_prestiti.remove(libroDaTogliere)