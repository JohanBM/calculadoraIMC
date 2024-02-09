print ('Ingrese la cantidad de usuarios a tratar')
cantidadUsuarios = int(input())

while (cantidadUsuarios > 0):
    #nombre del usuario
    aux = True
    while aux == True:
        try:
            apellidoPaterno = str(input('Ingrese su apellido paterno'))
            buscaApellidoPaterno = [caracter.isalpha() for caracter in apellidoPaterno]

            if buscaApellidoPaterno == False:
                print('Agregue un nombre valido')
            else:
                aux = False

        except ValueError:
            print('Agregue un nombre valido')

    print ('Ingrese su apellido materno')

    apellidoMaterno = input()

    print ('Ingrese su nombre')

    nombre = input()

    nombreCompleto = nombre + ' ' + apellidoPaterno+ ' ' + apellidoMaterno

    #datos para realizar el imc
    edad = int (input ('Ingrese su edad: '))

    peso = float (input ('Ingrese su peso: '))

    estatura = float (input ('Ingrese su estatura en metros: '))
    #realizar operacion del IMC
    imc = peso / estatura ** 2

    #Entregar los resultados
    cont = True
    while == True:
        try:
            edad = float(input('Ingrese su edad'))

            if 1 < edad < 18:
                print ('Aun eres menor, ven con tus padres')
            elif edad < 1:
                print ('Ingrese un numero correcto')
            elif:
                cont = False
        
        except ValueError:
            print('Ingrese un numero correcto')

#Diagnostico en base al IMC
    if imc >= 0 and imc < 16 :
        diagonostico = 'delgadez severa'
    elif imc >= 16.00 and imc < 17 :
        diagonostico = 'delgadez moderada'
    elif imc >= 17.00 and imc < 18.50:
        diagonostico = 'delgadez leve'
    elif imc >= 18.50 and imc < 25 :
        diagonostico = 'peso normal'
    elif imc >= 25.00 and imc < 30:
        diagonostico = 'sobrepeso'
    elif imc >= 30.00 and imc < 35:
        diagonostico = 'obesidad leve'
    elif imc >= 35.00 and imc < 40:
        diagonostico = 'obesidad media'
    elif imc >= 40.00:
        diagonostico = 'obesidad morbida'

    if (diagonostico is not None):
      #repr() funciona para concatenar float con string. Este se utiliza dentro de la etiqueta print.
      print(nombreCompleto + " usted mide " + repr(estatura) + " metros, y pesa " + repr(peso) + " kilogramos. Por lo que su IMC es " + repr(imc) + ", cuenta con " + diagonostico)
    else:
      print('No se que pasó')

    cantidadUsuarios = cantidadUsuarios - 1