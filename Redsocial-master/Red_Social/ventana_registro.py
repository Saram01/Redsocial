import tkinter as tk
from tkinter import messagebox

class VentanaRegistro(tk.Frame):
    def __init__(self, master, red_social, volver_a_inicio_sesion):
        super().__init__(master)
        self.master = master
        self.red_social = red_social
        self.volver_a_inicio_sesion = volver_a_inicio_sesion
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Registro de Usuario", font=("Arial", 16)).pack(pady=10)
        
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=5)
        self.entry_usuario.insert(0, "Usuario")
        
        self.entry_contraseña = tk.Entry(self, show='*')
        self.entry_contraseña.pack(pady=5)
        self.entry_contraseña.insert(0, "Contraseña")

        self.boton_registrar = tk.Button(self, text="Registrar", command=self.registrar_usuario)
        self.boton_registrar.pack(pady=10)

        self.boton_volver = tk.Button(self, text="Volver", command=self.volver_a_inicio_sesion)
        self.boton_volver.pack(pady=10)

    def registrar_usuario(self):
        username = self.entry_usuario.get()
        password = self.entry_contraseña.get()
        try:
            self.red_social.registrar_usuario(username, password)
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.volver_a_inicio_sesion()
        except Exception as e:
            messagebox.showerror("Error", str(e))






























