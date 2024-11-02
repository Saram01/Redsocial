from comentario import Comentario
from excepciones import PublicacionNoEncontrada

class Publicacion:
    def __init__(self, autor: str, texto: str, me_gusta=0, imagen=None):
        self.autor = autor
        self.texto = texto
        self.imagen = imagen
        self.me_gusta = me_gusta
        self.comentarios = []

    def dar_megusta(self):
        self.me_gusta += 1

    def agregar_comentario(self, autor: str, texto: str):
        comentario = Comentario(autor, texto)
        self.comentarios.append(comentario)
        return comentario

    def eliminar_publicacion(self, publicacion, publicaciones):
        if publicacion in publicaciones:
            publicaciones.remove(publicacion)
            self.autor.eliminar_publicacion_usuario(publicacion)
        else:
            raise PublicacionNoEncontrada("Publicacin no encontrada")
