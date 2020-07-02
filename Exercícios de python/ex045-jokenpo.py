# Bibliotecas
from random import choice
from time import sleep
print('\n')

# Título
print(4 * '-\033[1;30m紙\033[m-\033[1;34m石\033[m-\033[1;31m鋏\033[m')
jkp = 'Jokenpô'
print(str(f'\033[1;34m{jkp:^33}\n'))

# Jogo
lista = ['PEDRA', 'PAPEL', 'TESOURA']
player = str(input('\033[1;30mFaça a sua escolha, Samurai:\n PEDRA, PAPEL ou TESOURA?\033[m ')).strip().upper()

# Proteção
if player != 'PEDRA' and player != 'TESOURA' and player != 'PAPEL':
    print('\033[1;31mOpção Inválida. Tente novamente.\033[m')
else:
    # Jo...Ken...PO!
    print('\033[1;31mJO')
    sleep(0.6)
    print('\033[1;30mKEN')
    sleep(0.6)
    print('\033[1;34mPÔ!')
    sleep(0.6)
    pc = choice(lista)
    print(pc)

    # Colorindo resultados
    print(f'\033[1;31m')

    # Estrutura de decisão
    if player == 'PEDRA' and pc == 'PAPEL':
        print(f'\nConheça a sua morte!\nVocê: {player}\nEu: {pc}')
    elif player == 'PEDRA' and pc == 'TESOURA':
        print(f'Morrerei com a honra de um guerreiro.\nVocê: {player}\nEu: {pc}')
    elif player == 'PAPEL' and pc == 'TESOURA':
        print(f'Conheça a sua morte!\nVocê: {player}\nEu: {pc}')
    elif player == 'PAPEL' and pc == 'PEDRA':
        print(f'Morrerei com a honra de um guerreiro.\nVocê: {player}\nEu: {pc}')
    elif player == 'TESOURA' and pc == 'PEDRA':
        print(f'Conheça a sua morte!\nVocê: {player}\nEu: {pc}')
    elif player == 'TESOURA' and pc == 'PAPEL':
        print(f'Morrerei com a honra de um guerreiro.\nVocê: {player}\nEu: {pc}')

    # Empate com animação
    elif player == pc:
        print(f'Empate.', end='')
        sleep(0.6)
        print('.', end='')
        sleep(0.6)
        print('.', end=' ')
        sleep(0.6)
        print(f'Parece que voltaremos às nossas famílias dessa vez')
        sleep(0.6)
        print(f'Você: {player}')
        sleep(0.3)
        print(f'Eu: {pc}')
