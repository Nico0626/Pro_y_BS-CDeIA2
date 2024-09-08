

def sumar (numero1,numero2):
    resultado=(numero1 + numero2)
    return round(float(resultado),2)

def resta (numero1,numero2):
    resultado=(numero1 - numero2)
    return round(float(resultado),2) 

def multiplicar (numero1,numero2):
    resultado=(numero1 * numero2)
    return round(float(resultado),2)

def dividir(numero1,numero2):
    """if numero2==0:
        raise ValueError("No se puede dividir un numero entre 0")
    else:"""
    resultado=(numero1/numero2)
    return round(float(resultado),2)

def sumar_n(*numeros):
    resultado=(sum(numeros))
    return round(float(resultado),2)

def promedio_n(*numeros):
    if len(numeros)==0:
        raise ValueError ("No se puede calcular el promedio de cero números.")
    else:
        resultado=(sum(numeros)/len(numeros))
    return round(float(resultado),2)



