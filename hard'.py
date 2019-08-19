print("Зад2. Вывести из файла топ-10 самых популярных паролей")
f = open('pwd.txt')
str = f.read()
f.close()
z = str.split('\n')
rez = []
for i in range(len(z)):
    n = z[i].split(';')
    if z[i] != '':
        rez.append(n)
m = []
for i in range(len(rez)):
    m.append(rez[i][1])
m.sort()
out = []
cnt = 0
last_x = m[0]
for x in m:
    if x == last_x:
        cnt += 1
    else:
        out.append((cnt, last_x))
        cnt = 1
    last_x = x
out.append((cnt, last_x))
out.sort(reverse=True)
print("Топ 10 паролей:")
for i in range(10):
    print('{0}.{1}({2} раз)'.format(i + 1, out[i][1], out[i][0]))

