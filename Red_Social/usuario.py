from publicacion import Publicacion

class Usuario:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password = password
        self.publicaciones = []
        self.amigos = []

    def cambiar_contrasena(self, new_password):
        self._password = new_password

    def verificar_contrasena(self, password):
        return self._password == password

    def seguir_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)

    def crear_publicacion(self, texto, imagen=None):
        publicacion = Publicacion(self, texto, me_gusta=0, imagen=imagen)
        self.publicaciones.append(publicacion)
        return publicacion
