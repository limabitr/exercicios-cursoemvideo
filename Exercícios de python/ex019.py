# programa que escolhe aleatoriamente um aluno para ser sorteado
from random import choice
print('Digite os 4 alunos a serem sorteados.')
aluno1 = input('Digite o primeiro aluno : ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'{choice(lista)}')
