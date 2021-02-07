#The prime factors of 13195 are 5, 7, 13 and 29.

print('What is the largest prime factor of the number 600851475143 ?')

numero = 600851475143
factor = 2
while factor <= numero:
    if numero % factor == 0:
        print(factor, numero)
        numero = numero / factor
    else:
        factor = factor + 1
#Este solo leyo hasta el 60085147514#3 le falto un digito
'''while numero % factor == 0:
    numero = numero / factor
    print(factor, numero)
    while numero % factor != 0:
        factor = factor + 1'''

