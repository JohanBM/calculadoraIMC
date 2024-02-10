cont = True
while cont == True:
    try:
        cantidadUsuarios = int(input('Ingrese la cantidad de usuarios a tratar '))
        if cantidadUsuarios > 0:
            cont = False
        else:
            print('Ingresa un valor mayor a 0')
    
    except ValueError:
        print('Ingresa un número válido')

while (cantidadUsuarios > 0):
    #nombre del usuario
    aux = True
    while aux == True:
        try:
            apellidoPaterno = str(input('Ingrese su apellido paterno '))
            #buscar si los caracteres son letras y retornarnos como resultado true or false con la etiqueta any
            buscaApellidoPaterno = [caracter.isalpha() for caracter in apellidoPaterno]

            if not any(buscaApellidoPaterno):
                print('Agregue un nombre valido')
            else:
                aux = False

        except ValueError:
            print('Agregue un nombre valido')

    aux = True
    while aux == True:
        try:
            apellidoMaterno = str(input('Ingrese su apellido Materno '))
            #buscar si los caracteres son letras y retornarnos como resultado true or false con la etiqueta any
            buscaApellidoMaterno = [caracter.isalpha() for caracter in apellidoMaterno]

            if not any(buscaApellidoMaterno):
                print('Agregue un nombre valido')
            else:
                aux = False

        except ValueError:
            print('Agregue un nombre valido')

    aux = True
    while aux == True:
        try:
            nombre = str(input('Ingrese su(s) nombre(s) '))
            #buscar si los caracteres son letras y retornarnos como resultado true or false con la etiqueta any
            buscaNombre = [caracter.isalpha() for caracter in nombre]

            if not any(buscaNombre):
                print('Agregue un nombre valido')
            else:
                aux = False

        except ValueError:
            print('Agregue un nombre valido')
    #Unir el nombre
    nombreCompleto = nombre + ' ' + apellidoPaterno + ' ' + apellidoMaterno
    #datos para realizar el imc
    cont = True
    while cont == True:
        try:
            edad = float(input('Ingrese su edad '))

            if 1 < edad < 18:
                print ('Aun eres menor, ven con tus padres')
            elif edad < 1:
                print ('Ingrese un numero correcto')
            else:
                cont = False

        except ValueError:
            print('Agregue un valor valido')

    cont = True
    while cont == True:
        try:
            peso = float(input('Ingrese su peso en KG '))

            if peso >= 1:
                cont = False
            else:
                print ('Ingrese un valor correcto')

        except ValueError:
            print('Agregue un valor valido')

    cont = True
    while cont == True:
        try:
            estatura = float(input('Ingrese su estatura en metros '))

            if estatura >= 2.5:
                print ('Ingrese su estatura en metros porfavor')
            elif estatura <= 0.4:
                print('Ingrese un valor correcto')
            else:
                cont = False

        except ValueError:
            print('Agregue un valor valido')

    #realizar operacion del IMC
    imc = peso / estatura ** 2
    
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

    #Entrega de resultados y diagnostico
    if (diagonostico is not None):
      #repr() funciona para concatenar float con string. Este se utiliza dentro de la etiqueta print.
      print(nombreCompleto + " usted mide " + repr(estatura) + " metros, y pesa " + repr(peso) + " kilogramos. Por lo que su IMC es " + repr(imc) + ", cuenta con " + diagonostico)
    else:
      print('No se que pasó')

    cantidadUsuarios = cantidadUsuarios - 1