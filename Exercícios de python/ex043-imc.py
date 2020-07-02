p = float(input('Insira seu peso em Kg: '))
a = float(input('Insira sua altura em metros: '))

imc = p/pow(a, 2)
if imc < 18.5:
    print('\033[1;31mAbaixo do peso normal\033[m')
elif 18.5 <= imc < 25:
    print('\033[1;32mPeso ideal\033[m')
elif 25 <= imc <= 30:
    print('\033[7;37mSobrepeso\033[m')
elif 30 < imc <= 40:
    print('\033[1;33mObesidade\033[m')
elif imc > 40:
    print('\033[1;31mObesidade mórbida\033[m')