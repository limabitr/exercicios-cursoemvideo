r = int(input('Digite o comprimento de um dos lados do triângulo: '))
s = int(input('Digite outro comprimento: '))
t = int(input('Digite o terceiro comprimento: '))

# Condição de existência
if (r < s + t) and (s < t + r) and (t < r + s):
    print('O triângulo existe', end='')
    #  Classificação e condição aninhada
    if r == s == t:
        print(', é equilátero', end=' ')
    elif r == s or r == t or s == t:
        print(', é isósceles', end=' ')
    else:
        print(', é escaleno', end=' ')

    #  Síntese de Clairut
    if (r**2 == s**2 + t**2) or (s**2 == r**2 + t**2) or (t**2 == s**2 + r**2):
        print(f'e retângulo')
    elif (r**2 < s**2 + t**2) or (s**2 < r**2 + t**2) or (t**2 < s**2 + r**2):
        print(f'e acutângulo')
    elif (r**2 > s**2 + t**2) or (s**2 > r**2 + t**2) or (t**2 > s**2 + r**2):
        print(f'e obtusângulo')

else:
    print('O triângulo não existe')
