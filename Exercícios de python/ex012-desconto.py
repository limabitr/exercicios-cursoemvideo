# Algoritmo que lê preço e mostra seu novo preço com 5% de desconto
n = float(input('Insira o preço do produto: R$ '))
print(f'Este produto está com 10% de desconto, custando R$ {(n-(n/10)):.2f}')
