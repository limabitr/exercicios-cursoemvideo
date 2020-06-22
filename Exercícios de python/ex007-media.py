# Programa que lê notas de um aluno e mostra sua média
n = int(input('\033[35mDigite sua nota do primeiro bimestre: \033[m'))
n2 = int(input('\033[35mDigite sua nota do segundo bimestre: \033[m'))
n3 = int(input('\033[35mDigite sua nota do terceiro bimestre: \033[m'))
n4 = int(input('\033[35mDigite sua nota do quarto bimestre: \033[m'))
print(f'\033[1;36mSua média é {((n+n2+n3+n4)/4):.1f}\033[m')
