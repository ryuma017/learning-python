# うるう年を判定する

year = int(input("西暦4桁を入力してください:"))

if year % 100 == 0 and year % 400 != 0:
    print("うるう年ではありません")
elif year % 4 == 0:
    print("うるう年です")
else:
    print("うるう年ではありません")



"""
num = int(input())

if num % 4 == 0:
    if num % 100 ==0:
        if num % 400 == 0:
            print("うるう年です")
        else:
            print("うるう年ではありません")
    else:
        print("うるう年です")
else:
    print("うるう年ではありません")
"""