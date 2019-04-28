from itertools import permutations
 
str = '1234'
 
# obtenemos todas las permutaciones posibles de la cadena recibida
permList = permutations(str)
 
# mostramos las permutaciones
for perm in list(permList):
    print (''.join(perm))
