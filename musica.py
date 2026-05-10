# Classe Musica - Representa uma música na biblioteca
# Atributos: id, titulo, artista, genero, bpm

class Musica:
    """Classe que representa uma música na biblioteca."""
    
    def __init__(self, id, titulo, artista, genero, bpm):
        """
        Inicializa uma música com seus atributos.
        
        Args:
            id: Identificador único da música
            titulo: Nome da música
            artista: Nome do artista
            genero: Gênero musical
            bpm: Batidas por minuto (velocidade)
        """
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm
    
    def __str__(self):
        """Retorna uma representação legível da música."""
        return f"[{self.id}] {self.titulo} - {self.artista} ({self.genero}) - {self.bpm} BPM"
    
    def __repr__(self):
        """Retorna uma representação técnica da música."""
        return f"Musica({self.id}, '{self.titulo}', '{self.artista}', '{self.genero}', {self.bpm})"
