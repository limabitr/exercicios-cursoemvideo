from datetime import date
year = int(input('Informe o ano. Pressione 0 para ver se o ano atual é ou não bissexto: '))
if year == 0:
    var = year = date.today().year  # Se uma variavel ja estiver sendo usada pelo sistema, use -> var =
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:  # O símbolo diferença é !=
    print(f'O ano {year} é bissexto')
else:
    print(f'O ano {year} não é bissexto')
