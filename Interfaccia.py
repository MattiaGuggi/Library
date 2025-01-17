from Libro import Libro
from Utente import Utente
from Biblioteca import Biblioteca

class Interfaccia:

    def __init__(self):
        self.biblioteca = Biblioteca()

    def menu_principale(self):
        self.biblioteca.crea_libri()
        while True:
            print("\nMenu principale:")
            print("1)Aggiungi un nuovo libro")
            print("2)Aggiungi un nuovo utente")
            print("3)Cerca un libro nella biblioteca")
            print("4)Prendi in prestito un libro")
            print("5)Restituisci un libro")
            print("6)Esci")
            scelta = int(input("Scegli un'opzione: "))
            
            if scelta == 1:
                self.aggiungi_libro_interattivo()
            elif scelta == 2:
                self.aggiungi_utente()
            elif scelta == 3:
                self.cerca_libro()
            elif scelta == 4:
                self.prendi_in_prestito()
            elif scelta == 5:
                self.restituisci_libro()
            elif scelta == 6:
                print("Uscita dal programma")
                break
            else:
                print("Opzione non valida, riprova.")

    def aggiungi_libro_interattivo(self):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        anno_pubblicazione = int(input("Inserisci l'anno di pubblicazione del libro: "))
        libro = Libro(titolo, autore, anno_pubblicazione)
        self.biblioteca.aggiungi_libro(libro)

    def aggiungi_utente(self):
        nome = input("Inserisci il nome dell'utente: ")
        utente = Utente(nome)
        self.biblioteca.aggiungi_utente(utente)

    def cerca_libro(self):
        titolo = input("Inserisci il titolo del libro che vuoi cercare: ")
        trovato = self.biblioteca.cerca_libro(titolo)
        if trovato:
            print("Il libro è stato trovato.")
        else:
            print("Il libro non è presente nella biblioteca")

    def prendi_in_presto(self):
        trovato = False
        nome_utente = input("inserire il nome dell'utente: ")
        titolo = input("Inserisci il titolo del libro che vuoi prendere in prestito: ")
        autore = input("Inserisci l'autore del libro: ")
        anno_pubblicazione = int(input("Inserisci l'anno di pubblicazione del libro: "))
        libro = Libro(titolo, autore, anno_pubblicazione)
        for utente in self.biblioteca.lista_utenti:
            if utente.nome == nome_utente:
                trovato = True
                preso = self.biblioteca.prestito(utente, libro)
                if preso:
                    print("Libro preso in prestito")
                else:
                    print("Errore nella presa in prestito del libro")
                break
        if trovato == False:
            print("utente non trovato")

    def restituisci_libro(self):
        trovato = False
        nome_utente = input("inserire il nome dell'utente: ")
        titolo = input("Inserisci il titolo del libro che vuoi restituire: ")
        autore = input("Inserisci l'autore del libro: ")
        anno_pubblicazione = int(input("Inserisci l'anno di pubblicazione del libro: "))
        libro = Libro(titolo, autore, anno_pubblicazione)
        for utente in self.biblioteca.lista_utenti:
            if utente.nome == nome_utente:
                trovato = True
                restituito = self.biblioteca.restituzione(utente, libro)
                if restituito:
                    print("Libro restituito")
                else:
                    print("Errore nella restituzione del libro")
                break
        if trovato == False:
            print("utente non trovato")


if __name__ == "__main__":
    interfaccia = Interfaccia()
    interfaccia.menu_principale()
