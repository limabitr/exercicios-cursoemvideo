# Algoritmo que mostra todos os termos de uma PA

a1 = int(input("Digite o primeiro termo: "))
razao = int(input('Digite a razão: '))
termos = int(input('Digite a quantidade de termos: '))

for i in range(a1, a1 + razao*(termos - 1), razao):
    print(i, end=', ')
print(f'são os {termos} termos da sua PA.')
