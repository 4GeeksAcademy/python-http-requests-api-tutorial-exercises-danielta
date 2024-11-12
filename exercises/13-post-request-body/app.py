import requests

body = {
    "id": 2323,
    "title": "Very big project"
}

response = requests.post(
    "https://assets.breatheco.de/apis/fake/sample/save-project-json.php",
    json=body,
    # headers={'Content-Type': 'application/json'}
    )

print(response.text)