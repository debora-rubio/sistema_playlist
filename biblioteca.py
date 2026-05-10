# Classe Biblioteca - Lista encadeada de músicas
# Gerencia inserção, remoção e busca de músicas

from musica import Musica
from nodo_lista import NodoLista


class Biblioteca:
    # Construtor - inicializa a biblioteca vazia
    def __init__(self):
        self.inicio = None  # Primeiro nó da lista (vazio no começo)

    # Adiciona uma música ao final da biblioteca
    def adicionar_musica(self, musica):
        novo_nodo = NodoLista(musica)
        
        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
        
        print(f"Música '{musica.titulo}' adicionada com sucesso!")

    # Lista todas as músicas da biblioteca
    def listar_musicas(self):
        if self.inicio is None:
            print("A biblioteca está vazia.")
            return

        print("Biblioteca Completa")
        atual = self.inicio
        while atual is not None:
            print(atual.musica)
            atual = atual.proximo

    # Busca uma música pelo ID
    def buscar_por_id(self, id_procurado):
        atual = self.inicio
        
        while atual is not None:
            if atual.musica.id == id_procurado:
                print(f"Música encontrada: {atual.musica}")
                return atual.musica
            atual = atual.proximo
        
        print(f"Música com ID {id_procurado} não encontrada.")
        return None
    
    # Busca uma música por ID ou por título
    def buscar_musica(self, termo):
        atual = self.inicio
        
        while atual is not None:
            if str(atual.musica.id) == str(termo) or atual.musica.titulo.lower() == str(termo).lower():
                return atual.musica
            atual = atual.proximo
            
        return None

    # Verifica se uma música já existe (evita duplicatas)
    def existe_duplicada(self, titulo, artista):
        atual = self.inicio
        while atual is not None:
            if atual.musica.titulo.lower() == titulo.lower() and atual.musica.artista.lower() == artista.lower():
                return True
            atual = atual.proximo
        return False

    # Retorna o total de músicas na biblioteca
    def contar(self):
        total = 0
        atual = self.inicio
        while atual is not None:
            total += 1
            atual = atual.proximo
        return total

    # Remove uma música pelo ID
    def remover_musica(self, id_alvo):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.musica.id == id_alvo:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                
                print(f"Música '{atual.musica.titulo}' removida com sucesso!")
                return True
            
            anterior = atual
            atual = atual.proximo

        print("Erro: ID não encontrado.")
        return False
