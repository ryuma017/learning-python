import requests

response = requests.get("http://www.python.org/downloads/")
text = response.text
print(text)