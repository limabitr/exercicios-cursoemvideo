# le angulo e mostra o valor do sen, cos e tg
from math import radians, sin, cos, tan
ang = int(input('Digite um ângulo: '))
print(f'O seno de {ang} vale {(sin(radians(ang))):.2f}\n'
      f'O cosseno de {ang} vale {(cos(radians(ang))):.2f}\n'
      f'A tangente de {ang} vale {(tan(radians(ang))):.2f}')
