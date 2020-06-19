# n = input('Digite uma frase qualquer: ')
#
# count = n.count('a')
# print(f'Nessa frase há {count} letras a')
#
# find = n.find('a')
# print(f'Nessa frase, o caractere "a" está na {find}ª posição')
#
#
frase = 'Curso em Vídeo Python'
# print(f'{frase[:]}\n'
#      f'{frase[2::2]}\n'
#      f'{frase[:18:3]}\n'
#      f'{frase[::2]}')
#
#
print(f'{frase.upper()}\n'
      f'{frase.title()}\n'
      f'{frase.lower()}\n'
      f'A frase possui {len(frase)} caracteres\n'
      f'A frase sem espaços inutilizados contém {len(frase.strip())} caracteres\n'
      f'{frase.upper().count("O")}\n'
      f'{frase.replace("Python", "Android")}\n'
      f'{frase.replace("o", "a")}\n'
      f'{"curso" in frase}\n'
      f'{frase.lower().find("curso")}\n'
      f'{frase.split()}\n')
dividido = frase.split()
print(f'A quarta letra da terceira palavra é "{dividido[2][3]}"')
