# Classe NodoFila - Nó de uma fila (FIFO)
# Guarda uma música e a referência para o próximo nó

from musica import Musica


class NodoFila:
    # Construtor - recebe uma música e armazena
    def __init__(self, musica):
        self.musica = musica   # A música que este nó guarda
        self.proximo = None    # Referência para o próximo nó (vazio no começo)
    
    # Método para mostrar o nó
    def __str__(self):
        return str(self.musica)
