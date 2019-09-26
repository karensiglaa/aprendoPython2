entrada = input()
print (type(entrada))
#en le valor booleana contiene la asignacion que se verificara
#si lo que se escribe es numero, y si no se encunetra en un punto
#lo que se escribe, se va indicar de lo tratado
#es un munero decimal, ers decir,float. si find renorna -1
#entonces muestra que lo encontro. si esentero es true, el escribe es entero

esentero= (entrada.isdigit() and entrada.find(".") == -1)

if (esentero):
    #este se ejecturar si el nuemro es verdadero (true)
    print("dato entero. muy bien")
else:
    #este se ejecutara se el numero falso (false)
    print("dato no es entero. intetar de nuevo")
