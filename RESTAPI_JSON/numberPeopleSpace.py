import requests

url = "http://api.open-notify.org/astros.json"
datos = requests.get(url).json()

num = datos["number"]
personas = datos["people"]

print("Ahora mismo hay", num, "personas en el espacio.")
print("Sus nombres son: ",end="")
nombres = ""

for p in personas:
    nombres += p["name"]+", "
nombres = nombres[0:-2]
print(nombres)
