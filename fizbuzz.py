# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

for i in range(1,101,1):
  #Si es multiplo de 3 hago esto
  if(i % 3 == 0 and i % 5 == 0):
    print("fizzbuzz")
  #Si no es multiplo de 3, pero si de 5 hago esto
  elif(i % 5 == 0):
    print("buzz")
  elif(i % 3 == 0):
    print("fizz")
  #Si no se cumple ninguna de las anteriores condiciones, imprimo el numero
  else:
    print(i)
print("Fin del programa finalmente")
