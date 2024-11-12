import requests



def get_titles():
    titles = []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    resp_json=response.json()
    for post in resp_json['posts']:
        titles.append(post['title'])

    return titles


print(get_titles())