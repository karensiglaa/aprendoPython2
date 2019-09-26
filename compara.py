numero1=input("numero 1:")
numero2=input("numero 2:")
salida="numeros proporcionados {} y {}. {}."
#solo si los números capturados entran
if (numero1==numero2):
    print(salida.format(numero1, numero2, "los numeros son iguales"))
    #si los numeros no son iguales
else:
    if numero1>numero2:
        #cual numero es mayor
        print(salida.format(numero1,numero2, "El mayor es el primero"))
    else:
     #o si el mayor es el segundo
     print(salida.format(numero1,numero2, "el mayor es el segundo"))