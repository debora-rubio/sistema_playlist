# Classe Musica - Armazena os dados de uma música

class Musica:
    # Construtor - recebe os dados da música e armazena
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id              # Número único da música
        self.titulo = titulo      # Nome da música
        self.artista = artista    # Quem canta
        self.genero = genero      # Tipo de música
        self.bpm = bpm            # Velocidade da música
    
    # Método para mostrar a música
    def __str__(self):
        return self.titulo + " - " + self.artista
