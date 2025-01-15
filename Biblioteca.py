class Biblioteca:
    def __init__(self, lista_utenti, lista_libri):
        self.lista_utenti = lista_utenti
        self.lista_libri = lista_libri
        
    def aggiungi_libro(self):
        print('Aggiungi un libro')
    
    def aggiungi_utente(self):
        print('Aggiungi un utente')
    
    def cerca_libro(self):
        print('Cerca un libro')
    
    def prestito(self):
        print('Prestito')
    
    def restituzione(self):
        print('Restituisci')
        
def main():
    biblioteca = Biblioteca([], [])
    
if __name__ == '__main__':
    main()