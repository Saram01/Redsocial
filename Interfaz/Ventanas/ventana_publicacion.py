import tkinter as tk
from tkinter import messagebox

class VentanaPublicacion(tk.Frame):
    def __init__(self, master, agregar_publicacion, volver_al_feed):
        super().__init__(master)
        self.master = master
        self.agregar_publicacion = agregar_publicacion
        self.volver_al_feed = volver_al_feed
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Crear Nueva Publicación", font=("Arial", 16)).pack(pady=10)
        self.texto_publicacion = tk.Text(self, height=10, width=40)
        self.texto_publicacion.pack(pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar Publicación", command=self.guardar_publicacion)
        self.boton_guardar.pack(pady=5)

        self.boton_volver = tk.Button(self, text="Volver al Feed", command=self.volver_al_feed)
        self.boton_volver.pack(pady=5)

    def guardar_publicacion(self):
        contenido = self.texto_publicacion.get("1.0", tk.END).strip()  # Obtiene el contenido del texto
        if contenido:  # Asegura que no esté vacío
            self.agregar_publicacion(contenido)  # Llama a la función para agregar la publicación
            messagebox.showinfo("Éxito", "Publicación guardada.")
            self.volver_al_feed()  # Vuelve a mostrar el feed
        else:
            messagebox.showwarning("Error", "La publicación no puede estar vacía.")





