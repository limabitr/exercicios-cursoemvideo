# Aqui, o IDE verifica se é possível escrever como float
# Conversão de String para Float
# Se o valor recebido for de uma String alpha, dará erro
n = float(input('Digite um número: '))
print(n)
print(type(n))
#
# Aqui, como o valor da variável já é string, resulta no próprio
n2 = str(input('Digite algo: '))
print(n2)
print(type(n2))
# nesse caso, é possível fazer sem especificar o tipo primitivo:
# n2 = (input('digite algo: ')
# print(type(n2))-> o resultado sempre será String
#
# Aqui, se houver qualquer valor será True. O oposto também vale
n3 = bool(input('Digite algo: '))
print(n3)
print(type(n3))
#
#
n = input('digite algo: ')
print(n.isnumeric(), "num")
print(n.isalpha(), 'alpha')
print(n.isalnum(), 'alphanum')
