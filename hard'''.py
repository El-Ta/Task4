print("")
try:
    n = int(input("Введите размерность матрицы:"))
except ValueError:
    print("Параметр введен неверно.")
else:
     n = int(n)
     if n <1:
         print("Параметр введен неверно.")
     else:
         kl = [[None]*n for _ in range(n)]
         x = 0
         y = 0
         kly = 1
         klx = 0
         for i in range(1, n**2+1):
            kl[x][y] = i
            klxx = klx + x
            klyy = kly + y
            if  0 <= klxx < n and 0 <= klyy < n and not kl[klxx][klyy]:
                x = klxx
                y = klyy
            else:
                klx, kly = kly, -klx
                x += klx
                y += kly
         for i in range(len(kl)):
            for j in range(len(kl)):
                print(kl[i][j], end=' ')
            print()
