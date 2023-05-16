from dotenv import load_dotenv
import os
import json
import csv

load_dotenv("locales.env")
device_filename = str(os.getenv('deviceDatabase', default="devices.csv"))
signals_filename = str(os.getenv('deviceSignalsDatabase', default="databaze.csv"))

# This function gets gets a json input from a device post request and appends the json data onto the database.
def save_json_to_csv(data):

    # If the file is new, give it a header.
    open(signals_filename, "a+")
    if os.stat(signals_filename).st_size == 0:
        file = csv.writer(open(signals_filename, "w+"))
        header = ["CONNECTION_ID", "DEVICE_ID", "DEVICE_TYPE", "TIME_STAMP", "METADATA"]
        file.writerow(header)

    # Check if the device specified in the post request exists in our database.
    save = False
    file = csv.reader(open(device_filename, "r"))
    next(file)
    for i in file:
        if i[0] == str(data["DEVICE_ID"]):
            save = True
            break
    if not save:
        return 1

    # Append the file with the new data. 
    file = csv.writer(open(signals_filename, "a+"))
    new_row = []
    for i in list(data):
        if i != "COMMENTS":
            new_row.append(data[i])
    file.writerow(new_row)
    return 0

# This function will load our database in a way that is usefull for other functions functionality.
def load_database():
    file = csv.reader(open(signals_filename, "r"))
    next(file)
    return_data = []
    for i in file:
        return_data.append(i)
    
    return return_data
    
# This function outpus a database with only data from the specified timeframe.
def timeframe(data, start: int, end: int):
    return_data = []
    for i in data:
        if int(i[3]) >= start and int(i[3]) <= end:
            return_data.append(i)
    return return_data

# This function outputs a database with only the rows that have the specified value under the specified columb.
def lookup(data, column: int, value: str):
    return_data = []
    for i in data:
        if i[column] == value:
            return_data.append(i)
    return return_data

# This function is a debugging function that prints the database in a easier to read way.
def print_database(data):
    for i in data:
        print(i)

