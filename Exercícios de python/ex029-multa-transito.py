velocidade = float(input('Velocidade em Km/h: '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print(f'multa: R${multa:.2f}')
else:
    print('Veículo dentro dos limites de velocidade')
