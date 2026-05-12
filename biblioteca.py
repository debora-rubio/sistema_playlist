# Classe Biblioteca - Lista encadeada simples de músicas
# Ela guarda todas as músicas cadastradas no sistema.
from musica import Musica
from nodo_lista import NodoLista

class Biblioteca:
                                                     # Construtor: Cria a biblioteca vazia.
    def __init__(self):
        self.inicio = None                 # Indica o começo da lista. Se for None, a lista está vazia.

                            # Adicionar Música: Insere sempre no FINAL da lista encadeada. [linha 17]
    def adicionar_musica(self, musica):
        novo_nodo = NodoLista(musica)                    # Cria o "elo" com a nova música.
        
                                                    # Se não tiver nada, a nova música vira o início.
        if self.inicio is None:
            self.inicio = novo_nodo
        else:
                                # Se já tiver músicas, caminha até a última para colocar a nova no final.
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo                       # O último agora aponta para a nova música.

                                                       # Remover Música: Busca pelo ID e remove o nó. 
    def remover_musica(self, id_alvo):
        atual = self.inicio
        anterior = None

        while atual is not None:
                                                               # Se achou o ID que quer apagar:
            if atual.musica.id == id_alvo:
                if anterior is None:
                                                # Caso especial: remover a primeira música da lista.
                    self.inicio = atual.proximo
                else:
                                              # "Pula" o nó atual, ligando o anterior direto no próximo.
                    anterior.proximo = atual.proximo
                
                print(f"Música ID {id_alvo} removida com sucesso!")
                return True
            
                                                         # Se não achou ainda, continua caminhando:
            anterior = atual
            atual = atual.proximo

        print(f"Erro: O ID {id_alvo} não existe.")
        return False

                                  # Buscar Música: Procura tanto por ID quanto por Título. [linha: 22]
    def buscar_musica(self, termo):
        atual = self.inicio
        
        while atual is not None:
                                    # Lower() Converte tudo para texto e minúsculo para facilitar a busca.
            if str(atual.musica.id) == str(termo) or \
               atual.musica.titulo.lower() == str(termo).lower():
                return atual.musica                             # Retorna os dados da música encontrada.
            atual = atual.proximo
            
        return None                                      # Se percorrer tudo e não achar, retorna nada.

                     # Listar Biblioteca: Percorre do início ao fim exibindo as músicas. [linhas: 23, 25]
    def listar_musicas(self):
        if self.inicio is None:
            print("Biblioteca vazia.")
            return

        atual = self.inicio
        while atual is not None:
            print(atual.musica)                             # Usa o __str__ que definido em musica.py
            atual = atual.proximo

                                      # Contar: Função auxiliar para as estatísticas do menu. [linha: 39]
    def contar(self):
        total = 0
        atual = self.inicio
        while atual is not None:
            total += 1
            atual = atual.proximo
        return total