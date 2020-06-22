num = float(input('Digite um número: '))

# Condição de existência
if not (num % 2 == 0) and not (num % 2 == 1):
    print('Esse número não pode ser considerado Par nem Ímpar. Lembre-se que somente números inteiros podem ser '
          'classificados dessa forma')
else:
    # Verificação par-ímpar
    if num % 2 == 0:
        print('Esse número é Par')
    else:
        print('Esse número é ímpar')
