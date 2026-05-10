# Classe Fila - Fila FIFO (First In, First Out)
# Implementa enqueue (adiciona), dequeue (remove), e outras operações

from nodo_fila import NodoFila


class Fila:
    # Construtor - inicializa uma fila vazia
    def __init__(self):
        self.inicio = None  # Primeiro nó (cabeça da fila)
        self.fim = None     # Último nó (cauda da fila)
    
    # Adiciona uma música ao final da fila (ENQUEUE)
    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)
        
        if self.fim is None:  # Fila vazia
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
    
    # Remove e retorna a música do início da fila (DEQUEUE)
    def dequeue(self):
        if self.inicio is None:  # Fila vazia
            return None
        
        musica = self.inicio.musica
        self.inicio = self.inicio.proximo
        
        # Se fila ficou vazia após remoção
        if self.inicio is None:
            self.fim = None
        
        return musica
    
    # Verifica se a fila está vazia
    def esta_vazia(self):
        return self.inicio is None
    
    # Retorna o número de músicas na fila
    def tamanho(self):
        contador = 0
        nodo_atual = self.inicio
        
        while nodo_atual is not None:
            contador += 1
            nodo_atual = nodo_atual.proximo
        
        return contador
    
    # Exibe todas as músicas da fila de forma formatada
    def exibir_fila(self):
        if self.esta_vazia():
            print("  (fila vazia)")
            return
        
        nodo_atual = self.inicio
        posicao = 1
        
        while nodo_atual is not None:
            print(f"  {posicao}. {nodo_atual.musica}")
            nodo_atual = nodo_atual.proximo
            posicao += 1
