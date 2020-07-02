s = 0
count = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        s += c
        count += 1
print(f'A soma de todos os {count} números solicitados é {s}')

# Acumuladores:
