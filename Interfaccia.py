from Libro import Libro
from Utente import Utente
from Biblioteca import Biblioteca

class Interfaccia:
    
    def menu_principale(self):
        print("1)Aggiungi un nuovo libro")
        print("2)Aggiungi un nuovo utente")
        print("3)Cerca un libro nella biblioteca")
        print("4)Prendi in prestito un libro")
        print("5)Restituisci un libro")
        scelta = int(input("Scegli un 'opzione: "))
        while scelta < 1 or scelta > 5:
            print("Scegli un'opzione valida")
            scelta = int(input("Scegli un 'opzione: "))
        if scelta == 1:
            self.aggiungi_libro_interattivo()
        elif scelta == 2:
            self.aggiungi_utente()
        elif scelta == 3:
            self.cerca_libro()
        elif scelta == 4:
            self.prendi_in_presto()
        elif scelta == 5:
            self.restituisci_libro()
    
    
    def aggiungi_libro_interattivo(self):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        data_pubblicazione = int(input("Inserisci la data di pubblicazione del libro"))

    def aggiungi_utente(self):
        nome = input("Inserisci il nome dell'utente: ")
        libri_prestiti = []

    def cerca_libro(self):
        titolo = input("Inserisci il titolo del libro che vuoi cercare:")


    