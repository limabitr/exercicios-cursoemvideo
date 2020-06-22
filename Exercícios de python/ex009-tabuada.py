# Programa que lê um número inteiro e mostra a sua tabuada. A sintaxe \033[;m indica código de cor. Ignore.
a = str('TABUADA')
print(f'\033[33m {a:=^40}\033[m')
n = int(input('Digite um número inteiro: '))
print(f'\033[36m{n} x {1:2} = {(n*1):2}\n'
      f'{n} x {2:2} = {(n*2):2}\n'
      f'{n} x {3:2} = {(n*3):2}\n'
      f'{n} x {4:2} = {(n*4):2}\n'
      f'{n} x {5:2} = {(n*5):2}\n'
      f'{n} x {6:2} = {(n*6):2}\n'
      f'{n} x {7:2} = {(n*7):2}\n'
      f'{n} x {8:2} = {(n*8):2}\n'
      f'{n} x {9:2} = {(n*9):2}\n'
      f'{n} x 10 = {(n*10):2} \033[m'
      )
