import os
import json
import csv

def save_json_to_csv(data, filename):

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
    

