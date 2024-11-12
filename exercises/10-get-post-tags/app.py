import requests

def get_post_tags(post_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    resp_json=response.json()
    for post in resp_json['posts']:
        if post['id'] == post_id:
            return post['tags']


print(get_post_tags(146))