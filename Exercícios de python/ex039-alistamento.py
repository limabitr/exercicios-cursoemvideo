from datetime import date
nome = str(input('Digite seu nome: ')).strip()
nasc = int(input(f'Candidato {nome}, informe seu ano de nascimento: '))
ano = date.today().year
if ano - nasc == 18:
    print('Está na hora de você se alistar')
elif ano - nasc > 18:
    print('Seu tempo de se alistar já passou faz {} ano(s)'.format((ano - nasc) - 18))
elif ano - nasc < 18:
    print('Seu tempo de se alistar ainda não chegou. Faltam {} anos'.format(18 - (ano - nasc)))
