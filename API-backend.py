from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import csv
import csv_device as db
import prompt_generator
import AI_API
import database_management
import WLED.main as WLED
import requests

load_dotenv("locales.env")
device_filename = str(os.getenv('deviceDatabase', default="devices.csv"))

app = Flask(__name__)

# fuction for locating specific devices in the database using device_id
def find_device_in_database(id:int):
    with open(device_filename, 'r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            if line[0] == id:
                return line[1]
            
# function for locating device metadata in the database using device_id
def find_metadata_in_database(id:int):
    with open('databaze.csv', 'r') as file:
        main_list = []
        metadata = {}
        csv_file = csv.reader(file)
        # "turns" the file into a list
        for i in csv_file:
            main_list.append(i)
        # locates the requested device_id and returns the newest metadata
        for line in range(len(main_list) - 1):
            if (int(main_list[-1-line][1]) == int(id)):
                metadata = main_list[-1-line][4]
                return metadata
        return "error"

# locates connected devices in the database 
def connected_devices():
    devices = []
    with open(device_filename, 'r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            if (line[1] == "device_type" ):
                continue
            devices.append(line[1])
        return devices

# prints out the name of all the connected devices
@app.route('/api/devices', methods=['GET'])
def get_devices():
    # turns all the connected devices into JSON format and returns
    devices = connected_devices()
    response = {"devices":devices}
    return jsonify(response)

# prints out the name and metadata of a specified device using device_id
@app.route('/api/device/<id>', methods=['GET'])
def get_device(id):
    device = find_device_in_database(id)
    device_metadata = find_metadata_in_database(id)

    # when there is no device with the provided device_id, error message will be displayed
    if device is None:
        response = {'error':'Device not found'}
        return jsonify(response)

    else:
        response = {'device':device, 'metadata':device_metadata}
        return jsonify(response)

# returns ai generated answer on how to improve electricity consumption 
@app.route('/api/suggestion/<device_type>', methods=['GET'])
def get_ai_suggestion(device_type):
    prompt = prompt_generator.generate_prompt(device_type, 0, 999999999999999)
    return AI_API.get_help(prompt)

# registers a new device with a new device_id
@app.route('/api/devices', methods=['POST'])
def post_device(data):
    id = data["device_id"]
    type = data["device_type"]
    connect_id = data["connect_id"]
    database_management.add_device(id, connect_id, type)

@app.route('/api/getbrightness/<id>', methods=['GET'])
def get_device_brightness(id):
    return str(WLED.LED_manager().leds[1].brightness)

# deletes specific devices using the device_id
@app.route('/api/device/<connect_id>/<type>/<id>', methods=['DELETE'])
def delete_device(connect_id, id, type):
    database_management.remove_device(id, connect_id, type)

@app.route('/api/wled_off/<led_state>', methods=['GET'])
def switch_led(led_state):
    WLED.LED_manager().change_state(1, led_state, [255,0,0])
    return "sucess"

@app.route('/api/brightness/<brightness>', methods=['GET'])
def switch_led2(brightness):
    argument = int(brightness)
    if argument > 0:
        argument = int(argument*2.55//1)
    WLED.LED_manager().change_state(1, True, [255,0,0], brightness=argument)
    return "sucess"

@app.route('/api/wled/<connect_id>/<id>/<led_state>/<led_rgb>/<brightness>', methods=['POST'])
def change_led_state(device_id: int, connection_id: int, led_state: bool, led_rgb: list):
    if connection_id != int(os.getenv('id', default= -1)):
        return 1
    f = csv.reader(device_filename, "r+")

    does_device_exit = False
    for i in f:
        if i[0] == str(device_id):
           does_device_exit = True
           break
    if not does_device_exit:
        return 2

    WLED.change_state(device_id, led_state, led_rgb)
    return 0