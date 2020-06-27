ano = int(input('Informe a idade: '))
print('\n\033[7;36mCategoria:\033[m')
if 9 >= ano:
    print('\033[1;30mMIRIM\033[m')
elif ano <= 14:
    print('\033[1;32mINFANTIL\033[m')
elif ano <= 19:
    print('\033[1;33mJUNIOR\033[m')
elif ano <= 25:
    print('\033[1;35mSÊNIOR\033[m')
else:
    print('\033[1;31mMASTER\033[m')
