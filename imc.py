print ('Ingrese la cantidad de usuarios a tratar')
cantidadUsuarios = int(input())

while (cantidadUsuarios > 0):
    #nombre del usuario
    print ('Ingrese su apellido paterno')

    apellidoPaterno = input()

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
    if (edad < 18):
        print ('Aun eres menor, ven con tus padres')
    else:
        print ('Usted es mayor de edad')
        print ('Su IMC es: ' + imc)

    if imc >= 0 and imc < 16 :
        diagonostico = 'delgadez severa'
    elif imc >= 16.00 and imc < 17 :
        diagonostico = 'delgadez moderada'
    elif imc >= 17.00 and imc < 18.50:
        diagonostico = 'delgadez leve'
    elif imc >= 18.50 and imc < 25 :
        diagonostico = 'peso normal'
    elif imc >= 25.00 and imc < 30:
        diagonostico = 'obrepeso'
    elif imc >= 30.00 and imc < 35:
        diagonostico = 'obesidad leve'
    elif imc >= 35.00 and imc < 40:
        diagonostico = 'obesidad media'
    elif imc >= 40.00:
        diagonostico = 'obesidad morbida'

    print (nombreCompleto + ' usted mide ' + estatura + ' metros, y pesa ' + peso + ' kilogramos. Por lo que su IMC es ' + imc + ', cuenta con' + diagonostico)  
cantidadUsuarios = cantidadUsuarios - 1