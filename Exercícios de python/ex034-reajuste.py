valor = float(input('Informe seu salário: R$'))
if valor > 1250:
    print(f'Seu salário foi reajustado, passando a ser no valor de R$ {(valor + (valor * 1/10)):.2f}')
else:
    print(f'Seu salário foi reajustado, passando a ser no valor de R$ {(valor + (valor * 3/20)):.2f}')
