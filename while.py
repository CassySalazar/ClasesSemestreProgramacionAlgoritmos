#EJERCICIO 01
#SUMAR 5 NUMEROS POSITIVOS Y MOSTRAR RESULTADO POR PANTALLA

#1 inicializar variables suma en 0 e i en 1 (suma es la que me hara el calculo e i sera el incrementador)
""" suma = 0
i = 1

#2 crear un ciclo while con la condicion de que se repita tantas veces como i sea menor o igual en este caso a 5
while i <= 5:
    #3 creo una variable num de tipo int solicitando el numero por teclado
    num = int(input("ingrese numero: "))
    #4 verifico que el o los numero(s) ingresado(s) sean positivos
    if num > 0 :
        #5 si se resuelve el if, realizaremos la suma y aumentaremos el contador 
        suma = suma + num
        i = i + 1
    #5.1 si no se resuelve el if, caeremos en el else y este nos informará que el numero no cumple
    else:
        print("Numero ingresado no es valido")
#6 luego de que el ciclo while no tenga mas datos a comparar, mostrara el ultimo valor adquirido en la variable 'suma'        
print("el resultado de tus numeros es: ", suma) """
    
#EJERCICIO 02 
""" divisor = 1
numero_final=0
num = int(input("ingrese numero"))
if num >= 103 and num <= 987:
    while divisor <=100:
        resto = int(num/divisor)%10
        divisor = divisor*10
        numero_final = ((numero_final + resto)*10)
    print(numero_final)
else:
    print("el numero ingresado, debe ser entre 103 y 987")
"""
#EJERCICIO 03
total_pan = 0
pan = 0
i = 0
suma_pan = 0
cantidad = int(input("cuanto pan quiere comprar?: \n"))
print("que tipo de pan desea comprar?")
while i < cantidad:
    pan = int(input("1- AMASADO\t2- MOLDE\t3- Baguette\t4 - Integral"))
    if pan == 1:
        precio_pan = 1500
        i = i + 1
    elif pan == 2:
        precio_pan = 1000
        i = i + 1
    elif pan == 3:
        precio_pan = 2000
        i = i + 1
    elif pan == 4:
        precio_pan = 1000
        i = i + 1
    else:
        print("No hay ese tipo de pan")
        precio_pan = 0
    total_pan = total_pan + precio_pan 
    
print(f"el total a pagar es:  {total_pan}")
