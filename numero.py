numero=input ("dame un numero del 1 al 10")
numero=int(numero)
#ejecutamos un bloque de numeros para que se corra un rango mde valores
#El parametro rangwe no se incluye en la serie de valores
for i in range (1,11):
    #i va variando a cada interacion 
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))