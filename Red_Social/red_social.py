from usuario import Usuario
from publicacion import Publicacion
from excepciones import UsuarioNoEncontrado, UsuarioYaExiste, ContraseñaIncorrecta

class RedSocial:
    def __init__(self):
        self.usuarios = []
        self.publicaciones = []

    def crear_usuario(self, username, email, password):
        if any(u.username == username for u in self.usuarios):
            raise UsuarioYaExiste("El usuario ya existe")
        usuario = Usuario(username, email, password)
        self.usuarios.append(usuario)

    def buscar_usuario(self, username):
        for usuario in self.usuarios:
            if usuario.username == username:
                return usuario
        raise UsuarioNoEncontrado("Usuario no encontrado")

    def iniciar_sesion(self, username, password):
        usuario = self.buscar_usuario(username)
        if not usuario.verificar_contrasena(password):
            raise ContraseñaIncorrecta("Contraseña incorrecta")
        return usuario

    def visualizar_feed(self, usuario):
        feed = []
        for publicacion in self.publicaciones:
            if publicacion.autor in usuario.amigos:
                feed.append(publicacion)
        return feed
