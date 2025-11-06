import tkinter as tk
from tkinter import messagebox
from .ventana_publicacion import VentanaPublicacion
from .publicacion import Publicacion

class VentanaFeed(tk.Frame):
    def __init__(self, master, cerrar_sesion):
        super().__init__(master)
        self.master = master
        self.cerrar_sesion = cerrar_sesion
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Este es el Feed", font=("Arial", 16)).pack(pady=10)
        self.lista_publicaciones = tk.Listbox(self)
        self.lista_publicaciones.pack(fill="both", expand=True)
        self.boton_like = tk.Button(self, text="Dar Like", command=self.dar_like)
        self.boton_like.pack(pady=10)


        self.boton_nueva_publicacion = tk.Button(self, text="Crear Nueva Publicación", command=self.abrir_publicacion)
        self.boton_nueva_publicacion.pack(pady=10)

        self.boton_cerrar_sesion = tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.pack(pady=10)

    def mostrar_feed(self):
        self.lista_publicaciones.delete(0, tk.END)
        for publicacion in self.master.red_social.obtener_publicaciones():
            self.lista_publicaciones.insert(tk.END, f"{publicacion.autor.username}: {publicacion.texto} (Likes: {publicacion.me_gusta})")

    def abrir_publicacion(self):
        if hasattr(self, 'ventana_publicacion') and self.ventana_publicacion.winfo_ismapped():
            self.ventana_publicacion.pack_forget()
            del self.ventana_publicacion

        self.ventana_publicacion = VentanaPublicacion(self.master, self.agregar_publicacion)
        self.ventana_publicacion.pack(fill="both", expand=True)

    def agregar_publicacion(self, texto):
        publicacion = Publicacion(self.master.usuario_actual, texto)
        self.master.red_social.agregar_publicacion(publicacion)
        self.mostrar_feed()
        if hasattr(self, 'ventana_publicacion'):
            self.ventana_publicacion.pack_forget()


    def dar_like(self):
        seleccion = self.lista_publicaciones.curselection()
        if seleccion:
            idx = seleccion[0]
            publicacion = self.master.red_social.obtener_publicaciones()[idx]
            publicacion.dar_me_gusta()
            self.mostrar_feed()
        else:
            tk.messagebox.showinfo("Info", "Selecciona una publicación para dar Like.")


    def cerrar_sesion(self):
        self.usuario_actual = None
        self.ventana_feed.pack_forget()
        if hasattr(self.ventana_feed, 'ventana_publicacion') and self.ventana_feed.ventana_publicacion.winfo_ismapped():
            self.ventana_feed.ventana_publicacion.pack_forget()
            del self.ventana_feed.ventana_publicacion
        self.ventana_inicio_sesion.pack(fill="both", expand=True)
































