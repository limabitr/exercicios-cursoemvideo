# Programa que lê largura e altura de uma parede, calcula a área e a quantidade necessária para pintá-la, sabendo
# que cada litro de tinta pinta 2m²

n1 = float(input('Qual a largura da parede? '))
n2 = float(input('Qual a altura da parede? '))
print(f'sua parede possui {(n1*n2):.3f} metros quadrados. Logo, você precisará de {(n1*n2)/2} litros de tinta')
