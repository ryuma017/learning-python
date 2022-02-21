import requests
from bs4 import BeautifulSoup

text = requests.get("https://news.yahoo.co.jp/").text
soup = BeautifulSoup(text, "html.parser")

jobs = []
for job in soup.body.section.ul("a"):
    jobs.append(f"{job.text} ({job['href']})")

print("\n".join(jobs))