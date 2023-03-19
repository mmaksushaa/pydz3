import random
n = int(input("Введите кол-во элементов в массиве: "))
list_1 = [random.randint(-50, 50) for i in range(n)]
x = int(input("Введите число, которое хотите найти: "))
print(list_1)
c = 0
for i in range(n):
    if(list_1[i] == x):
        c = c + 1
print(c)
