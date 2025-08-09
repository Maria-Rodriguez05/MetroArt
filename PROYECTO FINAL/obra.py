class Obra:
    """Representa una obra de arte del museo."""
    def __init__(self, id_obra, titulo, artista, nacionalidad, nacimiento, muerte, tipo, anio_creacion, imagen):
        self.id_obra = id_obra  # ID de la obra
        self.titulo = titulo  # Título de la obra
        self.artista = artista  # Nombre del artista
        self.nacionalidad = nacionalidad  # Nacionalidad del artista
        self.nacimiento = nacimiento  # Fecha de nacimiento del artista
        self.muerte = muerte  # Fecha de muerte del artista
        self.tipo = tipo  # Tipo de obra
        self.anio_creacion = anio_creacion  # Año de creación
        self.imagen = imagen  # URL de la imagen

        
