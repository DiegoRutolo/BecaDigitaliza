"""https://sunrise-sunset.org/api"""

import requests
import datetime

# datos
url = "https://api.sunrise-sunset.org/json"

# Santiago de Compostela
lugar = "Santiago de Compostela"
lat = "42.8844"
lon = "-8.545"
url += "?lat="+lat+"&lng="+lon

datos = requests.get(url).json()
resultado = datos["results"]
alba = resultado["sunrise"]
ocaso = resultado["sunset"]
hoy = datetime.datetime.now().date()

print("Hoy, día ", hoy.day, "del", hoy.month, "de", hoy.year, "en", lugar, "amaneció a las", alba, "y anochecerá a las", ocaso)