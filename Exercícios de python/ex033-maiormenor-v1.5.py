# usando a function sorted() que coloca em ordem crescente

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
lista = [n1, n2, n3]
sorteio = sorted(lista)
print(f'O maior número é {sorteio[2]}\n'
      f'O menor número é {sorteio[0]}')
