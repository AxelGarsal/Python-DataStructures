print('Al considerar los términos en la secuencia de Fibonacci '
      'cuyos valores no excedan los cuatro millones, '
      'encuentre la suma de los términos pares.')
# 1 2 3 5 8 13 21 34 55 89 ...
a = 1
b = 2
suma = 0
while b <= 4000000:
    aux = a + b
    a = b
    b = aux
    #print(a, end =', ')
    if a % 2 == 0:
        suma = suma + a
print(suma)


