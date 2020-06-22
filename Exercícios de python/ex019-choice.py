# programa que escolhe aleatoriamente um aluno para ser sorteado
from random import choice
print('Digite os 4 alunos a serem sorteados.')
aluno1 = input('\033[1;31mDigite o primeiro aluno : ')
aluno2 = input('\033[1;34mDigite o nome do segundo aluno: ')
aluno3 = input('\033[1;32mDigite o nome do terceiro aluno: ')
aluno4 = input('\033[1;36mDigite o nome do quarto aluno: \033[m')
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'{choice(lista)}')
