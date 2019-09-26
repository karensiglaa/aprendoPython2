#importamos un módulo con la función import
import random
#se define variable y asignamos valor
numero1=float(17.5)
#declaramos def todo el código
def mifuncion():
    #se convierte a float el numero aleatorio generado por andom.randrage
    numero2=float(random.randrange(1,20))
    #sustituimos para mostrar el resultado
    mensaje="Lasuma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1*numero2))
    #se ejecuta la funcion 
    