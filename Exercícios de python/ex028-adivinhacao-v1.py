# O computador escolhe um número de 0 a 5 e o usuário tenta advinhar o número escolhido.

# --------------------------------------------Forma complexa-------------------------------------------------------

"""from random import choice
from time import sleep


# Pc escolhe um numero
num = range(0, 5)
computer = choice(num)

#Estrutura de decisão
player = int(input('Escolhi um numero de 0 a 5. Adivinha qual é?\n >>>'))
if player == computer:  # player == (num = randint(0, 5))
    print('Aposto que você faria sucesso como adivinho. Parabéns!')
else:
    print('Parece que não. Tente novamente.')"""

# --------------------------------------Forma simples com uma animação de 3 pontinhos------------------------
from random import randint
from time import sleep

computer = randint(0, 5)
player = int(input('Escolhi um numero de 0 a 5. Adivinha qual é?\n>>> '))

# Fluxo True e Proteção básica
if not (0 <= player <= 5):
    print('Heey, esse número não está entre 0 e 5')
else:
    # Fluxo False e Animação 3 pontinhos
    print(f'Analisando.', end="")
    sleep(0.6)
    print('.', end="")
    sleep(0.6)
    print('.')
    sleep(0.5)

    # Estrutura de decisão
    if player == computer:
        print('Você acertou!')
    else:
        print(f'Você errou. Tente novamente.\n'
              f'Você escolheu: {player}\n'
              f'Eu escolhi: {computer}')

# ------------------------------------------ideia de implementação posterior-----------------------------------------
# estrutura de repetição com tentativas
