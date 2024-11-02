import tkinter as tk
from tkinter import messagebox

class VentanaRegistro(tk.Frame):
    def __init__(self, master, volver_a_inicio_sesion):
        super().__init__(master)
        self.master = master
        self.volver_a_inicio_sesion = volver_a_inicio_sesion
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Registro", font=("Arial", 16)).pack(pady=10)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=5)
        self.entry_usuario.insert(0, "Usuario")
        
        self.entry_contraseña = tk.Entry(self, show='*')
        self.entry_contraseña.pack(pady=5)
        self.entry_contraseña.insert(0, "Contraseña")

        self.boton_registrar = tk.Button(self, text="Registrarse", command=self.registrar)
        self.boton_registrar.pack(pady=10)

        self.boton_volver = tk.Button(self, text="Volver", command=self.volver_a_inicio_sesion)
        self.boton_volver.pack(pady=10)

    def registrar(self):
        # Aquí se puede agregar la lógica de registro
        messagebox.showinfo("Registro", "Registrado con éxito.")
        self.volver_a_inicio_sesion()
























