# sorteie 4 alunos em ordem
from random import shuffle
aluno1 = input('Digite o nome de um aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno4, aluno2, aluno3, aluno1]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')
