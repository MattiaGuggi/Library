from Libro import Libro # type: ignore

class Biblioteca:
    def __init__(self, lista_utenti, lista_libri):
        self.lista_utenti = lista_utenti
        self.lista_libri = lista_libri
        
    def crea_libri(self):
        self.lista_libri = [
            Libro("1984", "George Orwell", 1949),
            Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954),
            Libro("Orgoglio e Pregiudizio", "Jane Austen", 1813),
            Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943),
            Libro("Moby Dick", "Herman Melville", 1851),
            Libro("Il Nome della Rosa", "Umberto Eco", 1980),
            Libro("La Divina Commedia", "Dante Alighieri", 1320),
            Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling", 1997),
            Libro("Il Grande Gatsby", "F. Scott Fitzgerald", 1925),
            Libro("Cime Tempestose", "Emily Brontë", 1847),
            Libro("Don Chisciotte della Mancia", "Miguel de Cervantes", 1605),
            Libro("Guerra e Pace", "Lev Tolstoj", 1869),
            Libro("Anna Karenina", "Lev Tolstoj", 1877),
            Libro("Il Processo", "Franz Kafka", 1925),
            Libro("Le Cronache di Narnia", "C.S. Lewis", 1950)
        ]
        
    def aggiungi_libro(self, libro):
        self.lista_libri.append(libro)
    
    def aggiungi_utente(self, utente):
        self.lista_utenti.append(utente)
    
    def cerca_libro(self, title):
        for libro in self.lista_libri:
            if libro.titolo == title:
                return True
            
        return False
    
    def prestito(self, utente, title, author, year):
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