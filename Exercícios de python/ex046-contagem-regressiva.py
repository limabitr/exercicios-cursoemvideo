from time import sleep
import emoji
print(emoji.emojize('Contagem regressiva para :tada::two::zero::two::one::tada:', use_aliases=True))
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':tada::fireworks:FELIZ ANO NOVO!:fireworks::tada:', use_aliases=True))
