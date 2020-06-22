year = int(input('Informe o ano: '))
if ((year % 4 == 0) or (year % 400 == 0)) and not (year % 100 == 0):
    print(f'O ano {year} é bissexto')
else:
    print(f'O ano {year} não é bissexto')
