distancia = float(input('Informe a distância em Km da viagem: '))
if distancia > 200:
    print(f'A passagem custará R${(distancia * 0.45):.2f}')
else:
    print(f'A passagem custará R${(distancia * 0.5):.2f}')
