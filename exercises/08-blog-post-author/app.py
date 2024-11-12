import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

resp_json=response.json()

print(resp_json['posts'][0]['author']['name'])
# Your code here