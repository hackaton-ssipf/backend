from flask import Flask, jsonify
import csv
import csv_device

app = Flask(__name__)

devices = [{'TV':'true', 'lamp':'false', 'oven':'false'}]

def find_device_in_database(id:str):
    with open('soubor.txt', 'r') as file:
    for i in 



@app.route('/api/devices', methods=['GET'])
def get_devices():
    # tvorba odpovedi v JSON formatu
    response = {"devices":devices}
    
    # vraci hodnoty v JSON formatu
    return jsonify(response)

@app.route('/api/devices/')

# retrieves details of a specific smart device
@app.route('/api/devices/<id>', methods=['GET'])
def get_device(id):

    device = find_device_in_database(id)
    if device is None:
        response = {'error':'Device not found'}
        return jsonify(response)

    else:
        # the return of the JSON response
        return jsonify(response)

