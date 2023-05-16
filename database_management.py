from dotenv import load_dotenv
import os
import json
import csv
import requests

load_dotenv("locales.env")
device_filename = str(os.getenv("deviceDatabase"))

# following code will get the data from API and add the device into the database
def add_device(device_id: int, connection_id: int, device_type: str):
    server_connection_id = int(os.getenv('id'))

    if connection_id != server_connection_id:
        print("Connection id is not valid")
        return False
    
    with open(device_filename, 'a+', newline='') as file:
        # if there is none, here will be added the header of the csv
        if os.stat(device_filename).st_size == 0:
            writer = csv.writer(file)
            writer.writerow(['device_id', 'device_type'])
        #if device with the device id already exists it wont be added again
        file.seek(0)
        for row in csv.reader(file):
            if row[0] == str(device_id):
                print("Device already exists")
                return False
        file.seek(0,2)
                


        # here will be added the device into the csv
        writer = csv.writer(file)
        writer.writerow([device_id, device_type])
        print("Device added successfully")
        return True

def remove_device(device_id: int, connection_id: int):
    server_connection_id = int(os.getenv('id'))
    if connection_id != server_connection_id:
        print("Connection id is not valid")
        return False
    # following code removes the device from the csv
    with open(device_filename, 'r+', newline='') as file:
        reader = csv.reader(file)
        lines = list(reader)
        file.seek(0)
        for row in lines:
            if row[0] != str(device_id):
                writer = csv.writer(file)
                writer.writerow(row)
        print("Device removed successfully")
        return True

def get_device(device_id: int) -> list:
    with open(device_filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(device_id):
                print(type(row))
                return row
