# Usando if: e else:

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
n3 = int(input('Informe mais um número: '))
if n1 < n2 < n3:
    print(f'{n3} é o maior\n {n1} é o menor')
else:
    if n2 < n1 < n3:
        print(f'{n3} é o maior\n {n2} é o menor')
    else:
        if n3 < n1 < n2:
            print(f'{n2} é o maior\n {n1} é o menor')
        else:
            if n1 < n3 < n2:
                print(f'{n2} é o maior\n {n3} é o menor')
            else:
                if n2 < n3 < n1:
                    print(f'{n1} é o maior\n {n3} é o menor')
                else:
                    print(f'{n1} é o maior\n {n2} é o menor')
