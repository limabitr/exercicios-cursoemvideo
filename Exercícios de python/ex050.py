s = 0
count = 0
for repeat in range(1, 7):
    num = int(input(f'Digite o {repeat}º número: '))
    if num % 2 == 0:
        s += num
        count += 1
print(f'Você me informou {count} números \033[1;34mpares\033[m e a soma deles vale {s}')
