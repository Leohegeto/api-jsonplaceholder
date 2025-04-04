import requests

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return {
        "status_code": response.status_code,
        "data": response.json() if response.status_code == 200 else []
    }
