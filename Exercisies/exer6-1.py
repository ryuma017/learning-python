def minimize(a, b, c):
    if a < b and a < c:        #あ、min関数使えばええやん。このやり方泥臭
        result = a
    elif b < a and b < c:
        result = b
    else:
        result = c
    return result
    
#実行
a,b,c = (int(x) for x in input("スペース区切りで整数を3つ入力: ").split())
print(minimize(a, b, c))