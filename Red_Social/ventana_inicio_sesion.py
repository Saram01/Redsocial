import tkinter as tk
from tkinter import messagebox

class VentanaInicioSesion(tk.Frame):
    def __init__(self, master, iniciar_sesion, ir_a_registro):
        super().__init__(master)
        self.master = master
        self.iniciar_sesion = iniciar_sesion
        self.ir_a_registro = ir_a_registro
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Iniciar Sesión", font=("Arial", 16)).pack(pady=10)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=5)
        self.entry_usuario.insert(0, "Usuario")
        
        self.entry_contraseña = tk.Entry(self, show='*')
        self.entry_contraseña.pack(pady=5)
        self.entry_contraseña.insert(0, "Contraseña")

        self.boton_iniciar = tk.Button(self, text="Iniciar Sesión", command=self.iniciar)
        self.boton_iniciar.pack(pady=10)

        self.boton_registrar = tk.Button(self, text="Registrarse", command=self.ir_a_registro)
        self.boton_registrar.pack(pady=10)

    def iniciar(self):
        self.iniciar_sesion()

























