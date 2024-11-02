import tkinter as tk
from Red_Social.ventana_feed import VentanaFeed
from Red_Social.ventana_inicio_sesion import VentanaInicioSesion
from Red_Social.ventana_registro import VentanaRegistro
from Red_Social.red_social import RedSocial

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi Red social")
        self.geometry("400x400")

        self.red_social = RedSocial()
        self.usuario_actual = None

        def iniciar_sesion():
            username = self.ventana_inicio_sesion.entry_usuario.get()
            password = self.ventana_inicio_sesion.entry_contraseña.get()
            try:
                self.usuario_actual = self.red_social.iniciar_sesion(username, password)
                print(f"Usuario {self.usuario_actual.username} ha iniciado sesión.")
                self.ventana_inicio_sesion.pack_forget()
                self.ventana_feed.mostrar_feed()
                self.ventana_feed.pack(fill="both", expand=True)
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

        def ir_a_registro():
            self.ventana_inicio_sesion.pack_forget()
            self.ventana_registro.pack(fill="both", expand=True)

        def cerrar_sesion():
            self.usuario_actual = None
            self.ventana_feed.pack_forget()
            self.ventana_inicio_sesion.pack(fill="both", expand=True)

        self.ventana_inicio_sesion = VentanaInicioSesion(self, iniciar_sesion, ir_a_registro)
        self.ventana_inicio_sesion.pack(fill="both", expand=True)

        self.ventana_feed = VentanaFeed(self, cerrar_sesion)
        self.ventana_registro = VentanaRegistro(self, self.red_social, self.volver_a_inicio_sesion)

    def volver_a_inicio_sesion(self):
        self.ventana_feed.pack_forget()
        self.ventana_registro.pack_forget()
        self.ventana_inicio_sesion.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()




