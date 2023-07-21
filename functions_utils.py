import requests 


def get_google_info():
    data = requests.get("https://www.google.com")
    return data.text


print ("cambio en funcion")

print("nuevo cambio...")