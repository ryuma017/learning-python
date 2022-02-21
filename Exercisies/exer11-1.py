pref = input("都道府県を入力: ")
ad   = input("西暦を入力: ")

f = open("c03.csv", "r", encoding="shift_jis")

running = True
while running:
    line   = f.readline().strip()
    line_l = line.split(",")
    
    if (pref in line_l) and (ad in line_l) and ("総数" in line_l):
        population = line_l[6]
        running = False
    
    if not line:
        break

if running == False:
    print(f"{ad}年の{pref}の人口は{population}人です")
else:
    print("Not found")