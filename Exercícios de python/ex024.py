cidade = input('Qual o nome da sua cidade? ')
a = cidade.upper().split()
print(f'Se sua cidade começa com Santo o resultado será True, caso contrário será False:\n {"SANTO" in a[0]}')