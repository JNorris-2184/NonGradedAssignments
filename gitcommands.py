import requests

response = requests.get('https://api.github.com/users/gvanrossum')

data = response.json()
type(data)
#print(data)

# Find GitHub users with most followers
url = f"https://api.github.com/search/users?q=followers:%3E0&sort=followers&order=desc"
response = requests.get(url)
if response.status_code == 200:
    results = response.json()
    print(type(results))
    for repo in results["items"][:1]:  # Display top 5 results
        print(f"Name: {repo['login']}")
#        print(repo)
else:
    print(f"Error: {response.status_code}, {response.json()}")