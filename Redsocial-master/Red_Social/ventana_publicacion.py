import tkinter as tk

class VentanaPublicacion(tk.Frame):
    def __init__(self, master, agregar_publicacion):
        super().__init__(master)
        self.master = master
        self.agregar_publicacion = agregar_publicacion
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Nueva Publicación", font=("Arial", 16)).pack(pady=10)
        self.entry_publicacion = tk.Entry(self)
        self.entry_publicacion.pack(pady=5)

        self.boton_publicar = tk.Button(self, text="Publicar", command=self.publicar)
        self.boton_publicar.pack(pady=10)

    def publicar(self):
        contenido = self.entry_publicacion.get()
        if contenido:
            self.agregar_publicacion(contenido)
            self.pack_forget()
        else:
            tk.messagebox.showwarning("Advertencia", "No se puede publicar contenido vacío.")















