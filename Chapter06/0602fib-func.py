def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print(fibs(int(input("数字を入力: "))))