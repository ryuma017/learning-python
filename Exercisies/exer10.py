import time

print("<<10秒ゲーム>>")
input("Enterキーでスタート")
start = time.time()
input("Enterキーでストップ")
stop = time.time()

result = stop - start

print(f"結果は{result}秒です")

if abs(result-10) <= 0.5:
    print("grate")
else:
    print("boo")

print(f"誤差:{abs(result-10)}")