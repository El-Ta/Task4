print("Зад1. Куб состоит из прозрачных и непрозрачныхэлементарных кубиков. "
      "Имеется ли хотя бы один просветпо каждому из трех измерений?")
import random
import pprint
n = 3
a = 0
b = 0
cu = []
for i in range(n):
    cu2 = []
    for j in range(n):
        cu3 = []
        for k in range(n):
            cu3.append(random.randint(0, 1))
        cu2.append(cu3)
    cu.append(cu2)
pprint.pprint(cu)
cu1 = True
for i in range(n):
    for j in range(n):
        k = 0
        if cu[i][j][k] == cu[i][j][k+1] and cu[i][j][k+1] == cu[i][j][k+2] and cu[i][j][k+2] == 1:
            print("Просвет", i, j, k)
            cu1 = False
for k in range(n):
    for i in range(n):
        j = 0
        if cu[i][j][k] == cu[i][j+1][k] and cu[i][j+1][k] == cu[i][j+2][k] and cu[i][j+2][k] == 1:
            print("Просвет", i, j, k)
            cu1 = False
for k in range(n):
    for j in range(n):
        i = 0
        if cu[i][j][k] == cu[i+1][j][k] and cu[i+1][j][k] == cu[i+2][j][k] and cu[i+2][j][k] == 1:
            print("Просвет", i, j, k)
            cu1 = False
if cu1 == True:
    print("Просветов нет")




