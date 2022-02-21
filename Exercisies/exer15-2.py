import requests
from bs4 import BeautifulSoup

categories_dict = {
    "1":  "",
    "2":  "categories/domestic",
    "3":  "categories/world",
    "4":  "categories/business",
    "5":  "categories/entertainment",
    "6":  "categories/sports",
    "7":  "categories/it",
    "8":  "categories/science",
    "9":  "categories/life",
    "10": "categories/local"
}


category_num = input("[1:主要 2:国内 3:国際 4:経済 5:エンタメ 6:スポーツ 7:IT 8:科学 9:ライフ 10:地域]\nカテゴリーの番号を入力: ")

try:
    text = requests.get("https://news.yahoo.co.jp/" + categories_dict[category_num]).text
except:
    print("不適切な値が入力されました。")
    exit()

soup = BeautifulSoup(text, "html.parser")

jobs = []
for job in soup.body.section.ul("a"):
    jobs.append(f"{job.text} ({job['href']})")

print("\n".join(jobs))