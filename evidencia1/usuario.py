import json
import re
from captcha import Captcha  # Asegúrate de que esta importación sea correcta

class gestorDeInicio:

    def __init__(self):
        self.__usuarios = self.cargar_usuarios()  # Cargar usuarios desde el archivo
        self.intentos_fallidos = {}

    def cargar_usuarios(self):
        """Carga los usuarios desde el archivo 'usuariosCreados.txt'."""
        try:
            with open('usuariosCreados.txt', 'r') as archivo:
                usuarios = json.load(archivo)
                return usuarios
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def validar_usuario(self, nombre_usuario):
        """Valida si el nombre de usuario tiene entre 6 y 12 caracteres y no está en uso."""
        if 6 <= len(nombre_usuario) <= 12 and nombre_usuario not in self.__usuarios:
            return True
        return False

    def validar_password(self, password):
        """Valida que la contraseña tenga al menos 8 caracteres y contenga al menos dos de las siguientes condiciones."""
        if len(password) < 8:
            return False
        condiciones = [
            re.search(r'[a-z]', password),  # al menos 1 minúscula
            re.search(r'[A-Z]', password),  # al menos 1 mayúscula
            re.search(r'[0-9]', password),  # al menos 1 número
            re.search(r'[^a-zA-Z0-9]', password)  # al menos 1 carácter especial
        ]
        return sum(bool(cond) for cond in condiciones) >= 2

    def registrar_usuario(self):
        """Solicita y registra un nuevo usuario"""
        print("Registro de nuevo usuario")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        correo = input("Correo electrónico: ")
        fecha_nacimiento = input("Fecha de nacimiento (DD/MM/YYYY): ")
        
        while True:
            nombre_usuario = input("Nombre de usuario (6-12 caracteres, único): ")
            if self.validar_usuario(nombre_usuario):
                break
            print("Nombre de usuario inválido o ya existe. Inténtelo de nuevo.")
        
        while True:
            password = input("Contraseña (mínimo 8 caracteres, debe cumplir con al menos dos de las siguientes condiciones: 1 minúscula, 1 mayúscula, 1 número, 1 carácter especial): ")
            if self.validar_password(password):
                break
            print("Contraseña inválida. Inténtelo de nuevo.")
        
        self.__usuarios[nombre_usuario] = {
            'nombre': nombre,
            'apellido': apellido,
            'dni': dni,
            'correo': correo,
            'fecha_nacimiento': fecha_nacimiento,
            'password': password
        }
        # Abre el archivo en modo de escritura ('w') para sobrescribir el archivo
        with open('usuariosCreados.txt', 'w') as archivo:
            json.dump(self.__usuarios, archivo, indent=4)
        
        print("Usuario registrado exitosamente!")

    def ingresar_contraseña(self):
        """Método para ingresar contraseña"""
        intentos = self.intentos_fallidos.get(self.nombre_usuario, 0)
        while intentos < 3:
            password = input("Contraseña: ")
            captcha = Captcha()  # Crear una instancia de Captcha
            if captcha.captcha():  # Verificar el captcha
                if self.__usuarios.get(self.nombre_usuario, {}).get('password') == password:
                    print("¡Inicio de sesión exitoso!")
                    self.intentos_fallidos[self.nombre_usuario] = 0  # Resetear los intentos fallidos
                    return self.menu()
                else:
                    intentos += 1
                    self.intentos_fallidos[self.nombre_usuario] = intentos
                    print(f"Contraseña incorrecta. Intentos restantes: {3 - intentos}")
            else:
                print("Captcha fallido. Inténtalo de nuevo.")
                continue
        print("Número máximo de intentos fallidos alcanzado. El acceso ha sido bloqueado temporalmente.")

    def recuperar_contraseña(self):
        """Método para recuperar contraseña"""
        pass
    
    def iniciar_sesion(self):
        """Permite al usuario iniciar sesión con su nombre de usuario y la contraseña."""
        self.nombre_usuario = input("Ingrese nombre de usuario: ")
    
        if self.nombre_usuario not in self.__usuarios:
            print("Nombre de usuario incorrecto.")
            return
        while True:
            print("\nOpciones:")
            print("1. Ingresar contraseña")
            print("2. ¿Olvidaste tu contraseña?")
        
            opcion = input("Seleccione una opción (1/2): ")

            if opcion == "1":
                self.ingresar_contraseña()
            elif opcion == "2":
                self.recuperar_contraseña()

    def menu(self):
        """Función principal que muestra un menú y maneja las opciones de inicio de sesión y registro."""
        print("----Bienvenido----")
    
        while True:
            print("\nOpciones:")
            print("1. Iniciar sesión")
            print("2. Registrar usuario")
            print("3. Salir")
        
            opcion = input("Seleccione una opción (1/2/3): ")

            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                print("Saliendo de la aplicación.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")