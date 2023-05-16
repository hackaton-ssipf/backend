from flask import Flask, jsonify
import csv
import csv_device as db

app = Flask(__name__)

devices = {'TV':'off', 'radio':'on', 'lamp':'off'}

# funkce pro hledani zarizeni podle device_id
def find_device_in_database(id):
    with open('devices.csv', 'r') as file:
        for line in file:
            if line[0] == id:
                return line[1]
                
# vrati nazvy zarizeni
@app.route('/api/devices', methods=['GET'])
def get_devices():
    # tvorba odpovedi v JSON formatu
    response = {"devices":devices}
    
    # vraci hodnoty v JSON formatu
    return jsonify(response)

# zobrazi detaily specifickeho podle zadane device_id
@app.route('/api/devices/<id>', methods=['GET'])
def get_device(id):

    # prirazeni zarizeni podle id do promenne device
    device = find_device_in_database(id)

    # when there is no device with the provided device_id, error message will be displayed
    if device is None:
        response = {'error':'Device not found'}
        return jsonify(response)

    else:
        # the return of the JSON response
        return jsonify(response)