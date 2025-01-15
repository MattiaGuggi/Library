class Biblioteca:
    def __init__(self, lista_utenti, lista_libri):
        self.lista_utenti = lista_utenti
        self.lista_libri = lista_libri
        
    def aggiungi_libro(self, libro):
        self.lista_libri.append(libro)
        print('Aggiungi un libro')
    
    def aggiungi_utente(self, utente):
        self.lista_utenti.append(utente)
    
    def cerca_libro(self, title):
        print('Cerca un libro')
        for libro in self.lista_libri:
            if libro.titolo == title:
                return True
            
        return False
    
    def prestito(self, utente, title, author, year):
        print('Prestito')
        for libro in self.lista_libri:
            if libro.titolo == title and libro.autore == author and libro.anno_pubbl == year:
                self.lista_libri.remove(libro)
                utente.prendi_libro(libro)
                return True
            
        return False
    
    def restituzione(self, utente, title, author, year):
        print('Restituisci')
        for libro in self.lista_libri:
            if libro.titolo == title and libro.autore == author and libro.anno_pubbl == year:
                self.lista_libri.append(libro)
                utente.restituisci_libro(libro)
                return True
            
        return False