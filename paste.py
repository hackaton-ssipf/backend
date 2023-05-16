import requests

url = 'http://localhost:5000/api/device/6'
headers = {'Content-Type': 'application/json'}
data = {'type': 'ahoj'}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)  # Output the status code
