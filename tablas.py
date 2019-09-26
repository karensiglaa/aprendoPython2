for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #definir
    print ()
    #se puede poner un for dentro de otro
    for j in range(1,11):
     #i tiene el número base de tabla y j el elemento
     salida="{} x {} ={}"
     print (salida.format(i,j,i*j))
    else:
     #al cumplir todo esto se ejecuta el código
     print ()
