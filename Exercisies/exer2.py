url = input("文字列を入力してください:").strip()

if url[:4] == "http":
    print(0)
else:
    print(1)

print(url[:4])