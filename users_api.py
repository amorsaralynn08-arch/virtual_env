import requests
 
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

posts = response.json()

for items in posts[0:6]:
    print(items["id"])
    print(items["title"])

