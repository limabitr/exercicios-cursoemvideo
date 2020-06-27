valor = float(input('Insira o valor do lote: R$'))
salario = float(input('Insira o salário do cliente: R$'))
anos = float(input('Em quantos anos o lote será pago?'))

if valor/(anos * 12) <= 3 * salario/10:
    print(f'O lote, no valor de R${valor:.2f}, deverá ser pago em prestações '
          f'mensais no valor de R${valor/(anos * 12):.2f}\n'
          f'\033[1;32mO empréstimo foi APROVADO\033[m')
else:
    print('\033[1;31mO empréstimo foi NEGADO\033[m')
