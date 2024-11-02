import tkinter as tk
from tkinter import messagebox
from .ventana_publicacion import VentanaPublicacion

class VentanaFeed(tk.Frame):
    def __init__(self, master, volver_a_inicio_sesion):
        super().__init__(master)
        self.master = master
        self.volver_a_inicio_sesion = volver_a_inicio_sesion
        self.publicaciones = []  # Lista para almacenar publicaciones
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Este es el Feed", font=("Arial", 16)).pack(pady=10)
        self.lista_publicaciones = tk.Listbox(self)
        self.lista_publicaciones.pack(fill="both", expand=True)

        self.boton_nueva_publicacion = tk.Button(self, text="Crear Nueva Publicación", command=self.abrir_publicacion)
        self.boton_nueva_publicacion.pack(pady=10)

        self.volver_btn = tk.Button(self, text="Volver a Iniciar Sesión", command=self.volver_a_inicio_sesion)
        self.volver_btn.pack(pady=10)

    def abrir_publicacion(self):
        self.ventana_publicacion = VentanaPublicacion(self.master, self.agregar_publicacion, self.mostrar_feed)
        self.ventana_publicacion.pack(fill="both", expand=True)

    def agregar_publicacion(self, contenido):
        self.publicaciones.append(contenido)
        self.lista_publicaciones.insert(tk.END, contenido)  # Muestra la nueva publicación

    def mostrar_feed(self):
        self.ventana_publicacion.pack_forget()  # Oculta la ventana de publicación
        self.pack(fill="both", expand=True)  # Muestra la ventana del feed
























