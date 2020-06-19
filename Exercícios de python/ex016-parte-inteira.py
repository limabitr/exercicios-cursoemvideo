# le numero Real e mostra parte inteira
#
# num = float(input('Insira um número Real qualquer: '))
# print(f'O número {num} tem a parte inteira {num:.0f}')
from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a porção inteira é {trunc(num)}')
