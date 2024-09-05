import aritmetica 

def test_sumar():
    assert aritmetica.sumar(4,5) ==9
    assert aritmetica.sumar(4.84,5) ==9.84
    assert aritmetica.sumar(-7.5, 1.5) == -6


def test_resta():
    assert aritmetica.resta(4,5) ==-1
    assert aritmetica.resta(5,2.5) == 2.5
    assert aritmetica.resta(-7.5, 1.5) == -9

def test_multiplicar():
    assert aritmetica.multiplicar(4,5) ==20
    assert aritmetica.multiplicar(5,2.5) == 12.5
    assert aritmetica.multiplicar(-7.5, 1) == -7.5

def test_dividir():
    assert aritmetica.dividir(20,5) ==4
    assert aritmetica.dividir(1,2.5) == 0.4
    assert aritmetica.dividir(2.5,2.5) == 1
    assert aritmetica.dividir(2.5,2) == 1.25

def test_sumar_n():
    assert aritmetica.sumar_n(4,5,8,1,2) ==20
    assert aritmetica.sumar_n(10,15.5,33.33) == 58.83
    assert aritmetica.sumar_n(-7.5, 1,44) == 37.5

def test_promedio_n():
    assert aritmetica.promedio_n(4,5) ==4.5
    assert aritmetica.promedio_n(5,2.5,54.99) == 20.83
    assert aritmetica.promedio_n(-7.5, 1,-5,8.8) == -0.67


    

if __name__=='__main__':
    test_sumar()
    test_resta()
    test_multiplicar()
    test_dividir()
    test_sumar_n()
    test_promedio_n()
