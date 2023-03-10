import webbrowser
import requests
pageurl = input("Podaj link: ")
date = input("Podaj date w formacie YYYYMMDD: ")

url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(url)

