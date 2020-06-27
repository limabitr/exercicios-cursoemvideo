from random import random, choice
from time import sleep
print('\n')
print(4 * '-\033[1;30m紙\033[m-\033[1;34m石\033[m-\033[1;31m鋏\033[m')
jkp = 'Jokenpô'
print(str(f'\033[1;34m{jkp:^33}\n'))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
player = str(input('\033[1;30mFaça a sua escolha, Samurai:\n PEDRA, PAPEL ou TESOURA?\033[m ')).strip().upper()
print('\033[1;31mJO')
sleep(0.6)
print('\033[1;30mKEN')
sleep(0.6)
print('\033[1;34mPÔ')
sleep(0.6)
pc = choice(lista)
print(f'\033[1;31m')
if player == 'PEDRA' and pc == 'PAPEL':
    print(f'\n Conheça a sua morte!\nVocê: {player}\nEu: {pc}')
elif player == 'PEDRA' and pc == 'TESOURA':
    print(f'Morrerei com a honra de um guerreiro.\nVocê: {player}\nEu: {pc}')
elif player == pc:
    print(f'Empate.', end='')
    sleep(0.6)
    print('.', end='')
    sleep(0.6)
    print('.', end=' ')
    sleep(0.6)
    print(f'Parece que voltaremos às nossas famílias dessa vez\nVocê: {player}\nEu: {pc}')
elif player == 'PAPEL' and pc == 'TESOURA':
    print(f'Conheça a sua morte!\nVocê: {player}\nEu: {pc}')
elif player == 'PAPEL' and pc == 'PEDRA':
    print(f'Morrerei com a honra de um guerreiro.\nVocê: {player}\nEu: {pc}')
elif player == 'TESOURA' and pc == 'PEDRA':
    print(f'Conheça a sua morte!\nVocê: {player}\nEu: {pc}')
elif player == 'TESOURA' and pc == 'PAPEL':
    print(f'Morrerei com a honra de um guerreiro.\nVocê: {player}\nEu: {pc}')
