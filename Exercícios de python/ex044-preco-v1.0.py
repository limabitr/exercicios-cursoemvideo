preco = float(input('Informe o preço do produto: R$'))
var = int(input(f'\033[1;30mInsira o número correspondente à forma de pagamento\n'
                f'\033[1;31m1\033[m - \033[1;30mÀ vista no \033[1;36mdinheiro/cheque\033[m: \033[1;33m10%\033[m \033['
                f'1;30mde desconto\n'
                f'\033[1;31m2\033[m - \033[1;30mÀ vista no \033[1;36mcartão\033[m: \033[1;33m5%\033[m \033[1;30mde'
                f'desconto\n'
                f'\033[1;31m3\033[m - \033[1;30mEm até \033[1;36m2x no cartão\033[m: \033[1;30mpreço original\n'
                f'\033[1;31m4\033[m - \033[1;30mno cartão, em \033[1;36m3x ou mais\033[m : \033[1;33m20%\033[m \033['
                f'1;30mde juros\n'
                f'\033[1;31mDigite o número: \033[1;32m'))

if var == 1:
    print(f'Valor da compra: R${(preco - (preco * 1/10)):.2f}\033[m')
elif var == 2:
    print(f'Valor da compra: R${(preco - (preco * 1/20)):.2f}\033[m')
elif var == 3:
    print(f'Valor da compra: R${preco:.2f}\033[m')
elif var == 4:
    print(f'Valor da compra: R${(preco * 0.2 * 3):.2f}\033[m')
