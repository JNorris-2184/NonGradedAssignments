import requests

#work with status codes
#resp = requests.get("https://httpbin.org/status/404")
#print(resp.status_code)
#resp.raise_for_status()

#examine response encoding
#resp = requests.get("https://httpbin.org//html")
#print(resp.encoding)
#print(resp.text)
#print(resp.content)


#read JSON content, use json() function
resp = requests.get("https://httpbin.org/json")
print(resp.json())
print(resp.headers)
print(resp.headers['content-type'])