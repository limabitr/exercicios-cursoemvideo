nome = str(input('Digite o seu nome: ')).strip()
print(f'{nome.upper()}\n'
      f'{nome.lower()}\n'
      f'Seu nome ao todo possui {len(nome) - nome.count(" ")} letras\n'
      f'Seu primeiro nome possui {len(nome.split()[0])} letras')
#
# é possível saber quantas letras tem o primeiro nome, identificando
# onde fica o primeiro espaço. Ex:
# print('Seu primeiro nome possui {} letras'.format(nome.find(" ")))
