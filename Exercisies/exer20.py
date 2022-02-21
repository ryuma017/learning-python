import sys

print("<html><head><title>ワールド・ワイド・スパムのホームページ</title></head><body>")

title = True
itemize  = False
for line in sys.stdin:
    line = line.strip()
    if line:
        if title:
            print("<h>")
            print(line)
            print("</h>")
            title = False
        elif line.startswith("-"):
            if not itemize:
                print("<ul>")
                itemize = True
            print("<li>")
            print(line[1:])
            print("</li>")
        else:
            if itemize:
                print("</ul>")
                itemize = False
            if line[-1] != "。" and line[-1] != "）":
                print("<h2>")
                print(line)
                print("</h2>")
            else:
                print("<p>")
                print(line)
                print("</p>")

print("</body></html>")