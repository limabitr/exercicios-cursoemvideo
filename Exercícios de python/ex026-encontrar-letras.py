frase = str(input('Digite uma frase: ')).strip().upper()
print(f'frase contém {frase.count("A")} letras "a"\n'
      f'\033[1;36mA letra "a" aparece primeiro na frase na \033[1;31m{(frase.find("A")+1)}ª\033[36m posição\n'
      f'A letra "a" aparece na frase pela última vez na \033[1;31m{frase.rfind("A")+1}ª\033[1;36m posição')
