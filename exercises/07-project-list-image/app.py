import requests

response=requests.get("https://image.shutterstock.com/image-vector/trophy-cup-award-vector-icon-260nw-592525184.jpg")

resp_json=response.json()

print(resp_json[-1]['images'][-1])
# Your code here