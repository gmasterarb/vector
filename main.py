#importo el modulo random
import random

#creo el vector
vector = []

#estructura de iteración de 0 a 100-1
for i in range(0,100):
  #por cada iteración se añade un elemento aleatorio al vector entre 1 y 100001-1
  vector.append(random.randrange(1, 100001))

#organizo los elemento del vector de mayor a menor
vector.sort(reverse=True)

#estructura de iteración que recorre el arreglo ordenado
for i in vector:
  #imprimo cada elemento del arreglo
  print(i)