r = float(input('Informe o comprimento da primeira reta: '))
s = float(input('Informe o comprimento da segunda reta: '))
t = float(input('Informe o comprimento da terceira reta: '))

# Condição de existência
if (s + t < r) or (s + r < t) or (r + t < s):
    print('Esse triângulo não existe.')
else:

    # Classificação quanto aos lados
    if r == s == t:
        print('Esse triângulo é equilátero', end=' ')
    else:
        if r == s or r == t or s == t:
            print('Esse triangulo é isósceles', end=' ')
        else:
            if not r == s == t:
                print('Esse triângulo é escaleno', end=' ')

# Classificação quanto aos ângulos segundo a Síntese de Clairut
    if (r**2 == s**2 + t**2) or (s**2 == r**2 + t**2) or (t**2 == s**2 + r**2):
        print('e retângulo')
    else:
        if (r**2 < s**2 + t**2) or (s**2 < r**2 + t**2) or (t**2 < s**2 + r**2):
            print('e acutângulo')
        else:
            if (r**2 > s**2 + t**2) or (s**2 > r**2 + t**2) or (t**2 > s**2 + r**2):
                print('e obtusângulo')
