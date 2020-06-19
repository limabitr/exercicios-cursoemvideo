n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1+n2

g# print('a soma entre', n1, 'e', n2, 'vale', s) ->
# é possível usar várias máscaras
# desde que seja atribuído os valores na ordem.

# print('a soma entre {} e {} vale {}'.format(n1, n2, s))

# versão mais atual python:
print(f'A soma entre {n1} e {n2} é igual a {s}.')
