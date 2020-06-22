velocidade = float(input('Velocidade em Km/h: '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print(f'\033[1;31mmulta:\033[m R${multa:.2f}')
else:
    print('\033[1;36mVeículo dentro dos limites de velocidade')
