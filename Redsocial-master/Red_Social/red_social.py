from .usuario import Usuario
from .publicacion import Publicacion

class RedSocial:
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []

    def registrar_usuario(self, username, password):
        if username in self.usuarios:
            raise Exception("El nombre de usuario ya está en uso.")
        self.usuarios[username] = Usuario(username, password)

    def iniciar_sesion(self, username, password):
        usuario = self.usuarios.get(username)
        if usuario and usuario.contraseña == password:
            return usuario
        raise Exception("Credenciales incorrectas.")

    def agregar_publicacion(self, publicacion):
        self.publicaciones.append(publicacion)

    def obtener_publicaciones(self):
        return self.publicaciones

#PRINCIPAL


