frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Sua frase contém {frase.count("A")} letras "a" \n'
      f'A letra "a" aparece primeiro na frase na {(frase.find("A")+1)}ª posição\n'
      f'A letra "a" aparece na frase pela última vez na {frase.rfind("A")+1}ª posição')
