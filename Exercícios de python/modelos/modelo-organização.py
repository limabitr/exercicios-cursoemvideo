from random import randint
from time import sleep

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
    sleep(1)

    # Estrutura de decisão
    if player == (randint(0, 5)):
        print('Você acertou!')
    else:
        print('Você errou. Tente novamente.')

