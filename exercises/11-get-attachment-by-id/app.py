import requests

def get_attachment_by_id(attachment_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    resp_json=response.json()
    for post in resp_json['posts']:
        for attch in post['attachments']:
            if attch['id'] == attachment_id:
                return attch['title']

print(get_attachment_by_id(137))