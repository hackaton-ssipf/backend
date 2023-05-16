from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import csv
import csv_device as db
import prompt_generator
import AI_API
import database_management

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
    with open('databaze.csv', 'r') as file:
        main_list = []
        line_list = []
        metadata = {}
        csv_file = csv.reader(file)
        
        for i in csv_file:
            main_list.append([i])
        print(main_list)

        for line in main_list:
            line_list.append(line)

        for line in main_list:
            if (main_list[0-line][3] == id):
                metadata = main_list[0-line][4]
            return  

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
    
        
        
