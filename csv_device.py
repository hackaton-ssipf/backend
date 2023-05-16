from enum import Enum
from dotenv import load_dotenv
import os
import json
import csv

load_dotenv("locales.env")
device_filename = str(os.getenv('deviceDatabase'), default="devices.csv")
signals_filename = str(os.getenv('deviceSignalsDatabase'), default="databaze.csv")

def save_json_to_csv(data):

    open(signals_filename, "a+")
    if os.stat(signals_filename).st_size == 0:
        f = csv.writer(open(signals_filename, "w+"))
        h = ["CONNECTION_ID", "DEVICE_ID", "DEVICE_TYPE", "TIME_STAMP", "METADATA"]
        #print(len(h))
        #for i in range(len(h)):
            #print(i)
        #    if h[i] == "COMMENTS":
         #       h.pop(i)
         #       break
        f.writerow(h)

    save = 0
    f = csv.reader(open(device_filename, "r"))
    for i in f:
        #print(i[0], type(i[0]) is int)
        if i[0] != "device_id" and i[0] == str(data["DEVICE_ID"]):
            save = 1
            #print("Device Exists")
            break

    if save == 1:
        f = csv.writer(open(signals_filename, "a+"))
        a = []
        for i in list(data):
            if i != "COMMENTS":
                #print(i, " : ", data[i])
                a.append(data[i])
        #print(a)
        f.writerow(a)

def load_database():
    f = csv.reader(open(signals_filename, "r"))
    data = []
    skip = 0
    for i in f:
        if skip == 0:
            skip = 1
            continue
        data.append(i)
    
    return data
    

def timeframe(data, start, end):
    return_data = []
    for i in data:
        if int(i[3]) >= start and int(i[3]) <= end:
            #print(i)
            return_data.append(i)
    return return_data

def lookup(data, header, value):
    #print(type(f))
    return_data = []
    for i in data:
        #print(type(i))
        if i[header] == value:
            #print(i)
            return_data.append(i)
    return return_data
            
def print_database(data):
    for i in data:
        print(i)
    
    
    

