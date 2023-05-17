import random
import requests
import time



class LED_manager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LED_manager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        self.leds = []
        self.create_leds()
    
    def configure_wled(self,url, settings):
        print(settings)
        try:
            response = requests.post(url, json=settings)
            response.raise_for_status()
            print(response)
            print("Konfigurace úspěšně odeslána.")
        except requests.exceptions.RequestException as e:
            print("Chyba při odesílání požadavku:", e)

    def create_leds(self,count=15):
        for i in range(count):
            self.leds.append(LED(i))
    
    def set_color(self,led_id,rgb):
        self.leds[led_id].color = rgb
    
    def set_brightness(self,led_id,brightness):
        self.leds[led_id].brightness = brightness
    
    def  set_state(self,led_id,state):
        self.leds[led_id].state = state
    
    def settings(self):
        settings = {"seg": []}
        for led in self.leds:
            settings["seg"].append({
                "on":led.state,
                "bri":led.brightness,
                "col":[[led.color[0],led.color[1],led.color[2],0],[],[]],
                "start":led.position,
                "stop": led.position+1
            })
        return settings
    def change_state(self,device_id:int, state: bool, rgb: list, brightness=128 ):
        wled_url = "http://10.10.3.24/json/state"  # Nahraďte <adresa_wled> IP adresou a portem WLED
        for i in range(15):
            self.set_state(i,state)
            self.set_color(i,rgb)
            self.set_brightness(i,brightness)
        self.configure_wled(wled_url,self.settings())


class LED():
    def __init__(self,position) -> None:
        self.state = False
        self.color = [255,255,255]
        self.brightness=128
        self.position = position










manager = LED_manager()

time.sleep(1)
manager.change_state(1,False,[255,0,0])
time.sleep(1)
manager.change_state(1,True,[0,255,0],brightness=255)

time.sleep(1)
manager.change_state(1,True,[0,0,255])
manager.set_color(2,[0,0,0])
manager.change_state(2,True,[255,0,0])
manager.change_state(3,True,[0,255,0])