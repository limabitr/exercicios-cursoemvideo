# Programa que lê a quantidade de Km percorridos por um carro alugado e a qnt de dias pelos quais foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado
#
km = float(input('Quantos Km foram percorridos? '))
d = int(input('Por quantos dias o carro ficou alugado? '))
print(f'O valor correspondente ao seu aluguel foi de R$ {(d*60+km*0.15):.2f}')
