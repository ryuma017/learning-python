num = int(input("数字を入力してください: "))
 
for i in range(1, num+1):
    if num % i == 0:
        print(i) 