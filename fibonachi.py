# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */
i = 2
n = 0
m = 1
print(n)
print(m)
while (i<50):
  fib = n + m
  print(fib)
  n = m
  m = fib
  i = i + 1 
