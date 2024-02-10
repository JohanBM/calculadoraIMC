# calculadoraIMC

 Para iniciar, estructuré el programa pidiendo todos los datos
 y realizar los los calculos correspondientes, entregando el
 resultado esperado.

 Se tuvieron problemas con el if de la linea 127 para evitar
 algun valor Null o None. Se corrigio dicho problema con
 "is not".

 para buscar si hay letras dentro de los caracteres y así 
 determinar si el nombre es válido es con la siguiente linea.
 "buscaApellidoPaterno = [caracter.isalpha() for caracter in
 apellidoPaterno]"

 Con "any(buscaApellidoPaterno)" si hay letras nos devuelve
 true y con esto podemos hacer que nos den un nombre valido,
 aunque con mucha libertad siempre que haya letras. Así
 podiendo pedir el nombre de nuevo si no es valido.

 Repetimos el procedimiento para apellido materno y el nombre.
 Posteriormente se agrega otro ciclo para la edad dando unos
 parametros y haciendo en caso de no ser correctos o utilizable
 nos pida de nuevo el dato numerico y lo mismo para la estatura
 y el peso, como para la cantidad de pacientes.

# Despues se agregó un while para para que se repita el codigo
# dependiendo del numero de pacientes.

# Durante el modulo en el bootcamp he aprendido sobre las 
# condicionales y los ciclos while. Además para ciertos 
# problemas de que surgieron durante el proyecto me ayudaron
# a buscar soluciones adicionales a los temas del mismo, 
# aprendiendo más sobre el python.