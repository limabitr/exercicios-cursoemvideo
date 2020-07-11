num = int(input('Digite um número: '))

b = 0
for c in range(1, num + 1):
    if num % c == 0:
        b += 1

if b == 2:
    print('É primo')
else:
    print('Não é primo')
