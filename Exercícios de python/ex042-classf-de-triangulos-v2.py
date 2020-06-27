r = int(input('Digite o comprimento de um dos lados do triângulo: '))
s = int(input('Digite outro comprimento: '))
t = int(input('Digite o terceiro comprimento: '))

# Condição de existência
if (r > s + t) or (s > t + r) or (t > r + s):
    print('O triângulo não existe')
else:
    print('O triângulo existe', end=" ")
    if r == s == t:
        print(', é equilátero')
    elif r == s or r == t or s == t:
        print(', é isósceles')
    elif r != s != t:
        print(', é escaleno')

    #  Síntese de Clairut
    if (r**2 == s**2 + t**2) or (s**2 == r**2 + t**2) or (t**2 == s**2 + r**2):
        print('e retângulo')
    elif (r**2 < s**2 + t**2) or (s**2 < r**2 + t**2) or (t**2 < s**2 + r**2):
        print('e acutângulo')
    elif (r**2 > s**2 + t**2) or (s**2 > r**2 + t**2) or (t**2 > s**2 + r**2):
        print('e obtusângulo')
