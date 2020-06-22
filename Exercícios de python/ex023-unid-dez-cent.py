num = int(input('Digite um número de 0 a 9999: '))
print(f'unidade: {num//1%10}\n'
      f'dezena: {num//10%10}\n'
      f'centena: {num//100%10}\n'
      f'milhar: {num//1000%10}')
