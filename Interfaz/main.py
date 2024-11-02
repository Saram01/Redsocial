import tkinter as tk
from Ventanas import ventana_inicio_sesion, ventana_feed, ventana_registro

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación de Redes Sociales")
        self.geometry("400x400")
        
        self.ventana_inicio_sesion = ventana_inicio_sesion.VentanaInicioSesion(self, self.switch_to_feed, self.switch_to_register)
        self.ventana_inicio_sesion.pack(fill="both", expand=True)

    def switch_to_feed(self):
        self.ventana_feed = ventana_feed.VentanaFeed(self, self.switch_to_login)
        self.ventana_feed.pack(fill="both", expand=True)
        self.ventana_inicio_sesion.pack_forget()

    def switch_to_login(self):
        self.ventana_feed.pack_forget()
        self.ventana_inicio_sesion.pack(fill="both", expand=True)

    def switch_to_register(self):
        self.ventana_registro = ventana_registro.VentanaRegistro(self, self.switch_to_login)
        self.ventana_registro.pack(fill="both", expand=True)
        self.ventana_inicio_sesion.pack_forget()

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()























