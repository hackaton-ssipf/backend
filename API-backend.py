from flask import Flask, jsonify
import csv
import csv_device as db

app = Flask(__name__)

# funkce pro hledani zarizeni podle device_id
def find_device_in_database(id:int):
    with open('databaze.csv', 'r') as file:
        read = csv.reader(file)
        for line in read:
            if line[1] == id:
                return line[2]

# funkce pro hledani zarizeni podle device_id
def find_metadata_in_database(id:int):
    with open('databaze.csv', 'r') as file:
        read = csv.reader(file)
        for line in read:
            if line[1] == id:
                return line[4]

#funcke pro zjisteni pripojenych zarizeni
def connected_devices():
    devices = []
    with open('devices.csv', 'r') as file:
        read = csv.reader(file)
        for row in read:
            if (row[1] == "device_type" ):
                continue
            devices.append(row[1])
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
        