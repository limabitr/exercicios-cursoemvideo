# Programa que lê saldo e mostre quantos Dólares ela pode comprar
n = float(input('Digite seu saldo: R$ '))
print(f'Com R$ {n:.2f}, você pode comprar U${(n/5.05):.2f}')
