# le comprimento dos catetos e calcula a hipotenusa

""" from math import sqrt, pow
cat1 = float(input('Insira um dos lados do triângulo: '))
cat2 = float(input('Insira o outro lado: '))
print(f'A hipotenusa desse triângulo vale {sqrt(pow(cat1, 2)+pow(cat2, 2)):.2f}')"""

# uma outra forma é incluir o método hypot(cat1, cat2)

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print(f'A hipotenusa desse triângulo vale {hypot(co, ca)}')
