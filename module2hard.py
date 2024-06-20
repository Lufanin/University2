m = []
i = int(input('Введите число от 3 до 20: '))
for j in range(1, 21):
    for k in range(2, 11):
        n = j + k
        if i % n == 0 and j < k:
            m.append(j)
            m.append(k)

print(i, '-', *m)