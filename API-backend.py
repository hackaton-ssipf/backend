from flask import Flask, jsonify
app = Flask(__name__)

devices = [{'TV':'true', 'lamp':'false', 'oven':'false'}]
data = {}


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
