from random import randrange

num   = int(input("サイコロの個数: "))
sides = int(input("各サイコロの面の数: "))
sum = 0
for i in range(num):
    j = randrange(sides) + 1
    print(f"{i+1}個目: {j}")
    sum += j
print(f"---------\n合計: {sum}")