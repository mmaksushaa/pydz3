import random
n = int(input("Введите кол-во элементов в массиве: "))
list_1 = [random.randint(-50, 50) for i in range(n)]
print(list_1)
x = int(input("Введите целое число: "))
diff = 10000000000000000
c = 0 
for i in range(n):
    if(abs(x - list_1[i]) < diff):
        c = list_1[i]
        diff = abs(x - list_1[i])
print("Ближайшее к", x, "число:", c)
