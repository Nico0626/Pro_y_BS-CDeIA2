import random
from aritmetica_carpeta import aritmetica

class Captcha:
    def __init__(self):
        self.operaciones = ['+', '-', '*', '/']
        self.numero1 = 0
        self.numero2 = 0
        self.operacion = ''
    
    def generar_operacion(self):
        """Genera una operación aritmética aleatoria y devuelve los operandos y la operación."""
        self.operacion = random.choice(self.operaciones)
        self.numero1 = round(random.uniform(-100, 100), 2)
        self.numero2 = round(random.uniform(-100, 100), 2)

        # Asegúrate de que no haya división por cero
        if self.operacion == '/':
            self.numero2 = round(random.uniform(0.1, 100), 2)
        
        return self.numero1, self.numero2, self.operacion

    def calcular_resultado(self):
        """Calcula el resultado de la operación aritmética."""
        if self.operacion == '+':
            return aritmetica.sumar(self.numero1, self.numero2)
        elif self.operacion == '-':
            return aritmetica.resta(self.numero1, self.numero2)
        elif self.operacion == '*':
            return aritmetica.multiplicar(self.numero1, self.numero2)
        elif self.operacion == '/':
            return aritmetica.dividir(self.numero1, self.numero2)

    def resolver_captcha(self):
        """Genera un captcha y valida la respuesta del usuario."""
        while True:
            self.generar_operacion()
            resultado_correcto = self.calcular_resultado()
            
            print(f"Resuelve la siguiente operación aritmética:")
            print(f"{self.numero1} {self.operacion} {self.numero2}")
            
            try:
                respuesta_usuario = float(input("Ingresa el resultado (con dos dígitos decimales): "))
            except ValueError:
                print("Entrada inválida. Inténtalo de nuevo.")
                continue
            
            if round(respuesta_usuario, 2) == resultado_correcto:
                print("¡Captcha resuelto correctamente!")
                return True
            else:
                print(f"Respuesta incorrecta. El resultado correcto era {resultado_correcto}.")
                opcion = input("¿Quieres intentar de nuevo? (s/n): ")
                if opcion.lower() != 's':
                    print("Registro cancelado.")
                    return False
                
    def captcha():
        captcha_instance = Captcha()
        captcha_instance.resolver_captcha()
