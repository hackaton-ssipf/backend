from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import csv
import csv_device as db
import prompt_generator
import AI_API
import database_management
import WLED.main as WLED

load_dotenv("locales.env")
device_filename = str(os.getenv('deviceDatabase', default="devices.csv"))

app = Flask(__name__)

# funkce pro hledani zarizeni podle device_id
def find_device_in_database(id:int):
    with open(device_filename, 'r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            if line[1] == id:
                return line[2]

# funkce pro hledani zarizeni podle device_id
def find_metadata_in_database(id:int):
    with open(device_filename, 'r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            if line[1] == id:
                return line[4]    
        # Prochazi zezadu vsechny pozice csv_file listu
        for line in csv_file:
            if line[-1] == id:
                return line[4]

#funcke pro zjisteni pripojenych zarizeni
def connected_devices():
    devices = []
    with open(device_filename, 'r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            if (line[1] == "device_type" ):
                continue
            devices.append(line[1])
        return devices

# vrati nazvy vsech momentalne pripojenych zarizeni
@app.route('/api/devices', methods=['GET'])
def get_devices():
    # tvorba odpovedi v JSON formatu
    devices = connected_devices()
    response = {"devices":devices}
    
    # vraci hodnoty v JSON formatu
    return jsonify(response)


# zobrazi detaily specifickeho zarizeni podle zadane device_id
@app.route('/api/device/<id>', methods=['GET'])
def get_device(id):

    # prirazeni zarizeni podle id do promenne device
    device = find_device_in_database(id)
    device_metadata = find_metadata_in_database(id)

    # when there is no device with the provided device_id, error message will be displayed
    if device is None:
        response = {'error':'Device not found'}
        return jsonify(response)

    else:
        # the return of the JSON response
        response = {'device':device, 'metadata':device_metadata}
        return jsonify(response)

# vrati ai generovany napad na zlepseni elektricke otazky
@app.route('/api/suggestion', methods=['GET'])
def get_ai_suggestion(device_type, start, end, device_id = -1):
    prompt = prompt_generator.generate_prompt(device_type, start, end, device_id)
    return AI_API.get_help(prompt)

@app.route('/api/device/<id>', methods=['POST'])
def post_device(connect_id, id, type):
    database_management.add_device(id, connect_id, type)

@app.route('/api/wled/<id>', methods=['POST'])
def change_led_state(device_id: int, connection_id: int, led_state: bool, led_rgb: list):
    if connection_id != int(os.getenv('id', default= -1)):
        return 1
    f = cvs.reader(device_filename, "r+")

    does_device_exit = false
    for i in f:
        if i[0] == str(device_id):
           does_device_exit = true
           break
    if not does_device_exit:
        return 2

    WLED.change_state(device_id, led_state, led_rgb)
    return 0

    
           
    
    
        
        
