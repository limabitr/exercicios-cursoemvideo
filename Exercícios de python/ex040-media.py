n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

if m < 5.0:
    print(f'A média do aluno foi {m:.1f} \n\033[1;31mREPROVADO\033[m')
elif 5.0 <= m < 7.0:
    print(f'A média do aluno foi {m:.1f} \n\033[1;33mRECUPERAÇÃO\033[m')
elif m >= 7.0:
    print(f'A média do aluno foi {m:.1f} \n\033[1;34mAPROVADO\033[m')
