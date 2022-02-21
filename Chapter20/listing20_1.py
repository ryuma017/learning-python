import sys

print("<html><head><title>タイトル</title></head></body>")

ttl = True
for line in sys.stdin:
    line = line.strip()
    if line:
        if ttl:
            print("<h1>")
            print(line)
            print("</h1>")
            ttl = False
        else:
            print("<p>")
            print(line)
            print("</p>")

print("</body></html>")