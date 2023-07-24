import requests
import random

# Kullanıcıdan bir URL adresi isteyin.
url = input("Bir URL adresi girin: ")

# URL'yi kısaltmak için bir API'yi kullanın.
response = requests.get("https://api.bitly.com/v4/shorten", params={"longUrl": url})

# API yanıtını işleyin.
shortUrl = response.json()["shortUrl"]

# Kullanıcıya kısaltılmış URL'yi gösterin.
print("Kısaltılmış URL: " + shortUrl)
