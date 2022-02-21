fruits = {"apple":152, "banana":200, "grape":308}

key = input("どれを買いますか:").strip()

print(f"お値段は{int(fruits[key] * 1.1)}円です")