Sistema de Playlist - Matéria de Estrutura de Dados - FATEC.

Este projeto é um sistema de gestão de biblioteca musical e filas de reprodução por humor, desenvolvido como requisito para a disciplina de Estrutura de Dados. O sistema utiliza estruturas de dados clássicas (Lista Encadeada Simples e Fila FIFO) implementadas manualmente, sem o uso de estruturas prontas do Python (como listas ou bibliotecas externas).

# Funcionalidades:

O sistema permite gerir uma biblioteca de músicas e organizá-las dinamicamente:

1.  Gestão da Biblioteca: Cadastro, remoção, busca e listagem de músicas (Lista Encadeada).
2.  Filas de Humor: Geração automática de filas de reprodução baseadas no BPM (Batidas Por Minuto):
    * Relaxar: Até 80 BPM
    * Focar: 81 a 120 BPM
    * Animar: 121 a 160 BPM
    * Treinar: Acima de 160 BPM
3.  Reprodução: Sistema de reprodução que consome a fila e guarda a música num Histórico.
4.  Estatísticas: Contagem de elementos para demonstrar o percurso nas estruturas.

# Estruturas de Dados Utilizadas:

* Lista Encadeada Simples: Utilizada na `Biblioteca`. Cada `NodoLista` aponta para o próximo, permitindo inserções no final e remoções em qualquer ponto.
* Fila FIFO (First In, First Out): Utilizada para as `Filas de Humor` e o `Histórico`. Implementada com ponteiros para o `inicio` e o `fim`, garantindo que a primeira música a entrar seja a primeira a ser reproduzida.

# Estrutura do Projeto:

* `main.py`: Ponto de entrada do sistema e gestão do menu.
* `musica.py`: Classe que representa a entidade Música.
* `biblioteca.py`: Lógica da Lista Encadeada.
* `fila.py`: Lógica da Fila FIFO.
* `nodo_lista.py` / `nodo_fila.py`: Definição dos nós das estruturas.

# Como Executar:

1.  Certifique-se de ter o Python 3 instalado.
2.  Faça o download ou clone todos os ficheiros para a mesma pasta.
3.  Execute o comando:
    ```bash
    python main.py
    ```

# Regras de Negócio Implementadas:

* IDs Sequenciais: Gerados automaticamente para cada nova música.
* Prevenção de Duplicados: O sistema verifica se uma música com o mesmo título e artista já existe antes de adicionar.
* Tratamento de Erros: Validação de entradas numéricas para BPM e IDs.
