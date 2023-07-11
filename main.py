import requests 



data = requests.get("https://www.google.com")


print("hola mundo!")

print(data.text)