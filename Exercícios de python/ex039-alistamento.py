from datetime import date
ano = date.today().year
nasc = int(input(f'Candidato, informe seu ano de nascimento: '))
idadep = ano - nasc
sexo = int(input('''Informe seu sexo
[1] Masculino
[2] Feminino
>>> '''))
# Proteção
if sexo == 2:
    print('Infelizmente, mulheres não podem se alistar no momento.')
else:
    if sexo != 1:
        print('Opção inválida. Tente novamente')

    # Fluxo normal
    else:
        if ano - nasc == 18:
            print('Você deve se alistar \033[1;31mimediatamente\033[m')
        elif ano - nasc > 18:
            print('Seu tempo de se alistar já passou faz {} ano(s)'.format((ano - nasc) - 18))
        elif ano - nasc < 18:
            prev = 18 - idadep + ano
            print('Seu tempo de se alistar será no ano de {}'.format(prev))
