tc = float(input('Informe a sua temperatura em ºC: '))
print(f'A\033[31m temperatura\033[m de {tc}ºC corresponde a {((9*tc+160)/5):.1f}ºF')
