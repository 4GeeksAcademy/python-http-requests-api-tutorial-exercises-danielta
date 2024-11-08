import requests


response=requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

resp_json=response.json()

print(resp_json[1]['name'])
# Your code here