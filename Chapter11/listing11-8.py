with open("sample.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end="\n")