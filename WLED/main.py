import random
import requests
import time
def configure_wled(url, settings):
    try:
        response = requests.post(url, json=settings)
        response.raise_for_status()
        print(response)
        print("Konfigurace úspěšně odeslána.")
    except requests.exceptions.RequestException as e:
        print("Chyba při odesílání požadavku:", e)

wled_url = "http://10.10.3.24/json/state"  # Nahraďte <adresa_wled> IP adresou a portem WLED
wled_settings = {
        "seg": [
            
        ]
    }

for i in range(15):
    r = random.randint(10,255)
    g = random.randint(10,255)
    b = random.randint(10,255)
    wled_settings["seg"].append({
                "on": True,
                "bri": 255,
                "col": [[r,g,b,0],[],[]],
                "start": i,
                "len": 1
            })



print(wled_settings["seg"])
# Odeslat konfiguraci WLED
configure_wled(wled_url, wled_settings)

def change_state(device_id:int, state: bool, rgb: list ):
    pass