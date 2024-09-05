import tkinter as tk
from tkinter import messagebox
import re


class GestorDeInicio:
    def __init__(self, root):
        self.__usuarios = {}
        self.intentos_fallidos = {}
        self.root = root
        self.nombre_usuario = None

        

        self.root.title("Gestor de Inicio")
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=300, pady=200)

        self.menu()

    def validar_usuario(self, nombre_usuario):
        if 6 <= len(nombre_usuario) <= 12 and nombre_usuario not in self.__usuarios:
            return True
        return False

    def validar_password(self, password):
        if len(password) < 8:
            return False
        condiciones = [
            re.search(r'[a-z]', password),
            re.search(r'[A-Z]', password),
            re.search(r'[0-9]', password),
            re.search(r'[^a-zA-Z0-9]', password)
        ]
        return sum(bool(cond) for cond in condiciones) >= 2

    def registrar_usuario(self):
        def registrar():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            dni = entry_dni.get()
            correo = entry_correo.get()
            fecha_nacimiento = entry_fecha_nacimiento.get()

            nombre_usuario = entry_nombre_usuario.get()
            password = entry_password.get()

            if self.validar_usuario(nombre_usuario) and self.validar_password(password):
                self.__usuarios[nombre_usuario] = {
                    'nombre': nombre,
                    'apellido': apellido,
                    'dni': dni,
                    'correo': correo,
                    'fecha_nacimiento': fecha_nacimiento,
                    'password': password
                }
                messagebox.showinfo("Registro", "Usuario registrado exitosamente!")
                registration_window.destroy()
            else:
                messagebox.showerror("Error", "Nombre de usuario o contraseña inválidos.")

        registration_window = tk.Toplevel(self.root)
        registration_window.title("Registrar Usuario")
        
        tk.Label(registration_window, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(registration_window, text="Apellido:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(registration_window, text="DNI:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(registration_window, text="Correo electrónico:").grid(row=3, column=0, sticky=tk.W)
        tk.Label(registration_window, text="Fecha de nacimiento (DD/MM/YYYY):").grid(row=4, column=0, sticky=tk.W)
        tk.Label(registration_window, text="Nombre de usuario (6-12 caracteres, único):").grid(row=5, column=0, sticky=tk.W)
        tk.Label(registration_window, text="Contraseña (mínimo 8 caracteres, debe cumplir con al menos dos de las siguientes condiciones: 1 minúscula, 1 mayúscula, 1 número, 1 carácter especial):").grid(row=6, column=0, sticky=tk.W)

        entry_nombre = tk.Entry(registration_window)
        entry_apellido = tk.Entry(registration_window)
        entry_dni = tk.Entry(registration_window)
        entry_correo = tk.Entry(registration_window)
        entry_fecha_nacimiento = tk.Entry(registration_window)
        entry_nombre_usuario = tk.Entry(registration_window)
        entry_password = tk.Entry(registration_window, show='*')

        entry_nombre.grid(row=0, column=1)
        entry_apellido.grid(row=1, column=1)
        entry_dni.grid(row=2, column=1)
        entry_correo.grid(row=3, column=1)
        entry_fecha_nacimiento.grid(row=4, column=1)
        entry_nombre_usuario.grid(row=5, column=1)
        entry_password.grid(row=6, column=1)

        tk.Button(registration_window, text="Registrar", command=registrar).grid(row=7, column=0, columnspan=2)

    def ingresar_contraseña(self):
        def verificar():
            password = entry_password.get()
            if self.__usuarios[self.nombre_usuario]['password'] == password:
                messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
                self.intentos_fallidos[self.nombre_usuario] = 0
                login_window.destroy()
            else:
                self.intentos_fallidos[self.nombre_usuario] = self.intentos_fallidos.get(self.nombre_usuario, 0) + 1
                intentos = self.intentos_fallidos[self.nombre_usuario]
                if intentos >= 3:
                    messagebox.showwarning("Advertencia", "Número máximo de intentos fallidos alcanzado. El acceso ha sido bloqueado temporalmente.")
                    login_window.destroy()
                else:
                    messagebox.showerror("Error", f"Contraseña incorrecta. Intentos restantes: {3 - intentos}")

        login_window = tk.Toplevel(self.root)
        login_window.title("Ingresar Contraseña")
        
        tk.Label(login_window, text="Contraseña:").grid(row=0, column=0, sticky=tk.W)
        entry_password = tk.Entry(login_window, show='*')
        entry_password.grid(row=0, column=1)
        tk.Button(login_window, text="Ingresar", command=verificar).grid(row=1, column=0, columnspan=2)
        
        #boton para recuperar contraseña
        tk.Button(login_window, text="Recuperar Contraseña",command=self.iniciar_sesion ).grid(row=3, column=2, columnspan=2)    
    
    #funcionalidad para recuperar contraseña, para terminar
    def recuperar_contraseña(self):
        messagebox.showinfo("Recuperar Contraseña", "Funcionalidad de recuperación de contraseña aún no implementada.")            

    def iniciar_sesion(self):
        def iniciar():
            self.nombre_usuario = entry_nombre_usuario.get()
            if self.nombre_usuario not in self.__usuarios:
                messagebox.showerror("Error", "Nombre de usuario incorrecto.")
            else:
                login_window.destroy()
                self.ingresar_contraseña()

        login_window = tk.Toplevel(self.root)
        login_window.title("Iniciar Sesión")
        
        tk.Label(login_window, text="Nombre de usuario:").grid(row=0, column=0, sticky=tk.W)
        entry_nombre_usuario = tk.Entry(login_window)
        entry_nombre_usuario.grid(row=0, column=1)
        tk.Button(login_window, text="Iniciar sesión", command=iniciar).grid(row=1, column=0, columnspan=2)

    def menu(self):
        tk.Label(self.main_frame, text="Bienvenido a la aplicación.").pack(pady=10)

        tk.Button(self.main_frame, text="Iniciar sesión", command=self.iniciar_sesion).pack(pady=5)
        tk.Button(self.main_frame, text="Registrar usuario", command=self.registrar_usuario).pack(pady=5)
        tk.Button(self.main_frame, text="Salir", command=self.root.quit).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorDeInicio(root)
    root.mainloop()
    

