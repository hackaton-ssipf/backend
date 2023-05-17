from dotenv import load_dotenv
import json
import csv_device as db
import AI_API

# This function will load the database, trim it according to the functions specifications and generate a OpenAI prompt out of the data.
def generate_prompt(device_type: str, start: int, end: int, device_id: int = -1):
    # Database searching
    database = db.load_database()
    database = db.timeframe(database, start, end)
    database = db.lookup(database, 2, device_type)
    if device_id != -1:
        database = db.lookup(database, 1, device_id)

    # If there are no results in the database, return info about that.
    if len(database) == 0:
        return None

    # Generate prompt from the found data
    prompt = "Smart Home Status Report\n\n" + device_type + " Usage Reports:\n\n"
    for report in database:
        time = convert_number_to_time(int(report[3]))
        prompt += " - " + time[0] + "-" + time[1] + "-" + time[2] + " " + time[3] + ":" + time[4] + ":" + time[5] + ", device " + report[1] +":"

        metadata = report[4]
        metadata = metadata.replace("'", '"')
        metadata = json.loads(metadata)

        for i in metadata.keys():
            match i:
                case "power_consumption":
                    prompt += " " + str(metadata[i]) + "kWh used since last report."
                case "brightness":
                    prompt += " Device was at " + str(metadata[i]) + "% brightness."
                case "temperature":
                    prompt += " Temperature was at " + str(metadata[i]) + "°C."
                case "humidity":
                    prompt += " Humidity was at " + str(metadata[i]) + "%."
                case "status":
                    prompt += ' Devices status: "' + str(metadata[i]) + '".'
                case "volume":
                    prompt += " The volume was at " + str(metadata[i]) + "%."
                # If need be you can easily add more special responses by adding more cases to this match statement
                case other:
                    prompt += ' "' + i + '" was "' + str(metadata[i]) + '".'
                    
        prompt += "\n"
    prompt += "\nQuestion: How can i optimize the usage of my smart house system based on these patterns?"
    return prompt

# This function converts numbers like this: 20230715153000 into an array with a info about the reports year, month, day, hour, minute and second.
def convert_number_to_time(number: int):
    return [
        str(number // 10000000000),
        str(number // 100000000 % 100),
        str(number // 1000000 % 100), 
        str(number // 10000 % 10) + str(number // 1000 % 10),
        str(number // 1000 % 10) + str(number // 100 % 10), 
        str(number // 10 % 10) + str(number % 10), 
    ]
