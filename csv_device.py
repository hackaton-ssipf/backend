import json
import csv

def save_json_to_csv(data, filename):
    f = csv.writer(open(filename, "w+"))
    h = []
    a = []
    for i in list(data):
        if i != "COMMENTS":
            #print(i, " : ", data[i])
            h.append(i)
            a.append(data[i])
    #print(a)
    f.writerow(h)
    f.writerow(a)

def add_header(filename):
    if os.stat(filename).st_size == 0:
            writer = csv.writer(file)
            writer.writerow(['CONNECTION_ID', 'DEVICE_ID', 'DEVICE_TYPE', 'TIME_STAMP', 'METADATA')
    
