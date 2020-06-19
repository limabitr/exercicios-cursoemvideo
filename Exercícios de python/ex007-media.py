# Programa que lê notas de um aluno e mostra sua média
n = int(input('Digite sua nota do primeiro bimestre: '))
n2 = int(input('Digite sua nota do segundo bimestre: '))
n3 = int(input('Digite sua nota do terceiro bimestre: '))
n4 = int(input('Digite sua nota do quarto bimestre: '))
print(f'Sua média é {((n+n2+n3+n4)/4):.1f}')
