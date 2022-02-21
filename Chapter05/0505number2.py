number = int(input("1以上10以下の整数を入力してください: "))
if number <= 10:
    if number >= 1:
        print("よくできました！")
    else:
        print("残念でした。")
else:
    print("残念でした。")