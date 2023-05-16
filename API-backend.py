from flask import Flask, jsonify
<<<<<<< Updated upstream
app = Flask(__name__)

devices = [{'TV':'true', 'lamp':'false', 'oven':'false'}]
data = {}
=======
import csv
#import csv_device as db

app = Flask(__name__)

devices = {'TV':'off', 'radio':'on', 'lamp':'off'}
>>>>>>> Stashed changes

def find_device_in_database(id):
    with open('devices.csv', 'r') as file:
        for line in file:
            if line.find(id) != -1:
                return 
                

@app.route('/api/devices', methods=['GET'])
def get_devices():
    # creation of response in JSON style
    response = {"devices":devices}
    
    # the return of the JSON response
    return jsonify(response)

# retrieves details of a specific smart device
@app.route('/api/devices/<id>', methods=['GET'])
def get_device(id):

    response = {}
    # the return of the JSON response
    return jsonify(response)
