# Algoritmo que lê salário e mostra novo salário
# com 15% de aumento
n = float(input('Digite o seu salário: R$ '))
print(f'Parabéns! você recebeu um aumento de 15% no seu salário\n'
      f'Agora, você passará a receber R$ {(n+(n*3/20)):.2f}')
