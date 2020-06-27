num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para a conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
base = int(input('>>> '))
if base == 1:
    print(f'O número {num} em BINÁRIO corresponde a {bin(num)[2:]}')
elif base == 2:
    print(f'O número {num} em OCTAL equivale a {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num} em HEXADECIMAL equivale a {hex(num)[2:]}')

# Proteção

else:
    print('Opção inválida. Tente novamente.')