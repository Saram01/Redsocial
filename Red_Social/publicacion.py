class Publicacion:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.me_gusta = 0
        self.comentarios = []

    def dar_me_gusta(self):
        self.me_gusta += 1

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)



