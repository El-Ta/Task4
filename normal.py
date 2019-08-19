import random
print("Зад1. Сгенерировать 2500-значное число, найти и вывести самую длинную последовательность одинаковых цифр.")
sp = [random.randint(0, 9) for _ in range(2500)]
sp = ''.join(list(map(lambda x: str(x), sp)))
print("Рандомное 2500-значное число:")
print(sp)
file = open('test.txt', 'w')
for index in sp:
    file.write(index)
file.close()
file = open('test.txt')
str = list(file.read())
file.close()
out = []
cnt = 0
last_x = str[0]
max = 1
for x in str:
    if x == last_x:
        cnt += 1
    else:
        if cnt != 1:
            out.append((last_x, cnt))
        if max <= cnt:
            max = cnt
        cnt = 1
    last_x = x
if cnt != 1:
    out.append((last_x, cnt))
if max <= cnt:
    max = cnt
print("Самые длинные последовательности одинаковых цифр:")
for i in range(len(out)):
    if out[i][1] == max:
        for j in range(out[i][1]):
            print(out[i][0], end='')
        print()


print("Зад2. Сгенерировать рандомную матрицу, в каждой строке которой находится ровно один ноль на случайном месте.")
import pprint
import random
k = int(input("Введите размер матрицы:"))
kl = []
for i in range(k):
    rl = []
    for j in range(k):
        rl.append(random.randint(1, 30))
    n = random.randint(0, 4)
    rl[n] = 0
    kl.append(rl)
print("Полученная матрица:")
pprint.pprint(kl)
