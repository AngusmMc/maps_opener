import requests # allows us to download files from the web
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))
print(len(res.text))
print(res.text)
