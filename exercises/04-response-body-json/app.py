import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

resp_json = response.json()

print(f"Current time: {resp_json['hours']} hrs {resp_json['minutes']} min and {resp_json['seconds']} sec")