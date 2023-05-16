from dotenv import load_dotenv
import json
import csv_device as db

def generate_prompt(device_type, start, end, device_id = -1):
    database = db.load_database()
    database = db.timeframe(database, start, end)
    database = db.lookup(database, 2, device_type)
    if device_id != -1:
        database = db.lookup(database, 1, device_id)
    #db.print_database(database)
    
    if len(database) == 0:
        return "No Smart Home Status Report for " + device_type + "."
    
    prompt = "Smart Home Status Report\n\n" + device_type + " Usage Reports:\n\n"
    for report in database:
        time = convert_number_to_time(int(report[3]))
        prompt += " - " + time[0] + "-" + time[1] + "-" + time[2] + " " + time[3] + ":" + time[4] + ":" + time[5] + ", device " + report[1] +":"

        j = report[4]
        j = j.replace("'", '"')
        j = json.loads(j)

        for i in j.keys():
            match i:
                case "power_consumption":
                    prompt += " " + str(j[i]) + "kWh used since last report."
                case "brightness":
                    prompt += " Device was at " + str(j[i]) + "% brightness."
                case "temperature":
                    prompt += " Temperature was at " + str(j[i]) + "°C."
                case "humidity":
                    prompt += " Humidity was at " + str(j[i]) + "%."
                case "status":
                    prompt += ' Devices status: "' + str(j[i]) + '".'
                case "volume":
                    prompt += " The volume was at " + str(j[i]) + "%."
                # If need be you can easily add more special responses by adding more cases to this match statement
                case other:
                    prompt += ' "' + i + '" was "' + str(j[i]) + '".'
                    
                
        #else:
        #    prompt += "Power consumption wasn't specified or isn't applicable."
        
        prompt += "\n"
    prompt += "\nQuestion: How can i optimize the usage of my smart house system based on these patterns?"
    return prompt

# 2023 05 23 11 38 02

def convert_number_to_time(number):
    return [
        str(number // 10000000000),
        str(number // 100000000 % 100),
        str(number // 1000000 % 100), 
        str(number // 10000 % 10) + str(number // 1000 % 10),
        str(number // 1000 % 10) + str(number // 100 % 10), 
        str(number // 10 % 10) + str(number % 10), 
    ]

print(generate_prompt("TV", 0, 20231230235959))
print("")
print(generate_prompt("LIGHT", 0, 20231230235959))
print("")
print(generate_prompt("DOOR_SENSOR", 0, 20231230235959))
print("")
print(generate_prompt("HEATING", 0, 20231230235959))
    
