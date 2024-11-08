import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

resp_json=response.json()




print(resp_json['name'])
# Your code here