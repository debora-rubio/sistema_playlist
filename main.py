from musica import Musica
from biblioteca import Biblioteca
from fila import Fila

def inicializar_dados(biblioteca):
    """
    Cadastra as músicas iniciais sugeridas para a apresentação.
    """
    # Lista de tuplas (Título, Artista, Gênero, BPM)
    musicas_iniciais = [
        ("Fix You", "Coldplay", "Pop Rock", 67),
        ("Bohemian Rhapsody", "Queen", "Rock", 72),
        ("Starway to Heaven", "Led Zeppelin", "Rock", 80),
        ("Hotel California", "Eagles", "Rock", 110),
        ("Every Breath You Take", "The Police", "Rock", 117),
        ("Animals", "Maroon 5", "Pop", 120),
        ("Shake it Off", "Taylor Swift", "Pop", 150),
        ("Thunder", "Imagine Dragons", "Pop Rock", 155),
        ("Natural", "Imagine Dragons", "Pop Rock", 157),
        ("Can't Stop", "Red Hot Chili Peppers", "Rock", 171),
        ("Back in Black", "AC/DC", "Rock", 175),
        ("Sex on Fire", "Kings of Leon", "Rock", 176),
    ]
    
    id_atual = 1
    for titulo, artista, genero, bpm in musicas_iniciais:
        nova = Musica(id_atual, titulo, artista, genero, bpm)
        biblioteca.adicionar_musica(nova)
        id_atual += 1
    
    return id_atual # Retorna o próximo ID disponível

def exibir_menu():
    print("\n" + "="*30)
    print("      Playlist da Debs")
    print("="*30)
    print("1. Adicionar música")
    print("2. Remover música (por ID)")
    print("3. Buscar música (ID ou Título)")
    print("4. Listar Biblioteca")
    print("5. Gerar Filas por Humor")
    print("6. Reproduzir Próxima (Humor)")
    print("7. Ver Fila de Humor")
    print("8. Ver Histórico")
    print("9. Estatísticas")
    print("10. Sair")
    return input("\nEscolha uma opção: ")

def main():
    minha_biblioteca = Biblioteca()
    historico = Fila()
    
    # Filas de humor
    fila_relaxar = Fila()
    fila_focar = Fila()
    fila_animar = Fila()
    fila_treinar = Fila()
    
    # Inicia com as músicas sugeridas
    proximo_id = inicializar_dados(minha_biblioteca)

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            titulo = input("Título: ")
            artista = input("Artista: ")
            genero = input("Gênero: ")
            try:
                bpm = int(input("BPM: "))
                nova = Musica(proximo_id, titulo, artista, genero, bpm)
                minha_biblioteca.adicionar_musica(nova)
                proximo_id += 1
            except ValueError:
                print("Erro: BPM deve ser um número inteiro.")

        elif opcao == "2":
            try:
                id_alvo = int(input("ID da música para remover: "))
                minha_biblioteca.remover_musica(id_alvo)
            except ValueError:
                print("Erro: Digite um ID válido.")

        elif opcao == "3":
            termo = input("Digite o ID ou Título: ")
            resultado = minha_biblioteca.buscar_musica(termo)
            if resultado:
                print(f"\nEncontrada: {resultado}")
            else:
                print("\nMúsica não encontrada.")

        elif opcao == "4":
            minha_biblioteca.listar_musicas()

        elif opcao == "5":
            # Limpa as filas para não duplicar se apertar o botão de novo
            fila_relaxar = Fila()
            fila_focar = Fila()
            fila_animar = Fila()
            fila_treinar = Fila()
            
            atual = minha_biblioteca.inicio
            while atual is not None:
                m = atual.musica
                if m.bpm <= 80:
                    fila_relaxar.enqueue(m)
                elif m.bpm <= 120:
                    fila_focar.enqueue(m)
                elif m.bpm <= 160:
                    fila_animar.enqueue(m)
                else:
                    fila_treinar.enqueue(m)
                atual = atual.proximo
            print("\nFilas de humor geradas com sucesso!")

        elif opcao == "6":
            print("\nEscolha o Humor: 1-Relaxar | 2-Focar | 3-Animar | 4-Treinar")
            h = input("Opção: ")
            alvo = None
            if h == "1": alvo = fila_relaxar
            elif h == "2": alvo = fila_focar
            elif h == "3": alvo = fila_animar
            elif h == "4": alvo = fila_treinar

            if alvo and not alvo.esta_vazia():
                tocando = alvo.dequeue()
                print(f"\n>>> TOCANDO AGORA: {tocando.titulo} - {tocando.artista}")
                historico.enqueue(tocando)
            else:
                print("\nFila vazia ou opção inválida!")

        elif opcao == "7":
            print("\n1-Relaxar | 2-Focar | 3-Animar | 4-Treinar")
            h = input("Ver qual fila? ")
            if h == "1": fila_relaxar.exibir_fila()
            elif h == "2": fila_focar.exibir_fila()
            elif h == "3": fila_animar.exibir_fila()
            elif h == "4": fila_treinar.exibir_fila()

        elif opcao == "8":
            print("\n--- HISTÓRICO DE REPRODUÇÃO ---")
            historico.exibir_fila()

        elif opcao == "9":
            print(f"\n--- ESTATÍSTICAS ---")
            print(f"Total na Biblioteca: {minha_biblioteca.contar()}")
            print(f"Já ouvidas: {historico.tamanho()}")

        elif opcao == "10":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()