import os
import json
import csv

<<<<<<< Updated upstream
def save_json_to_csv(data, filename):
=======
load_dotenv("locales.env")
device_filename = str(os.getenv('deviceDatabase', default="devices.csv"))
signals_filename = str(os.getenv('deviceSignalsDatabase', default="databaze.csv"))
>>>>>>> Stashed changes

    if os.stat(filename).st_size == 0:
        f = csv.writer(open(filename, "w+"))
        h = list(data)
        print(len(h))
        for i in range(len(h)):
            print(i)
            if h[i] == "COMMENTS":
                h.pop(i)
                break
        f.writerow(h)
    
    f = csv.writer(open(filename, "a+"))
    a = []
    for i in list(data):
        if i != "COMMENTS":
            #print(i, " : ", data[i])
            a.append(data[i])
    #print(a)
    f.writerow(a)
    

