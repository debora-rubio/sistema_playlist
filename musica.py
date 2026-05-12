class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):        # Exibe o ID antes dos dados da música.
        
        return f"ID: {self.id} | {self.titulo} - {self.artista} ({self.bpm} BPM)"
