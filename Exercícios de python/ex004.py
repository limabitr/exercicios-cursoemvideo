n = (input('digite algo: '))
print(f'', type(n), '\n' 
                    f'É alfabético? {n.isalpha()}\n'
                    f'É  alfanumérico? {n.isalnum()}\n'
                    f'É um número? {n.isnumeric()}\n'
                    f'Está em minúscula? {n.islower()}\n'
                    f'Está em maiúscula? {n.isupper()}\n'
                    f'Está capitalizada? {n.istitle()}\n'
                    f'Só tem espaços? {n.isspace()}')
#
# outra forma
#
# n = (input('digite algo: ')
# print(type(n))
# print('É alfabético? {}'.format(n.isalpha))
# print('É maiúscula{}'.format(n.isupper))
#
# FIM
