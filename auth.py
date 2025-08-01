import requests
from requests.auth import HTTPDigestAuth

user = "theuser"
passwd = "thepass"

url = "https://httpbin.org/basic-auth/theuser/thepass"
#resp = requests.get(url, auth=(user, passwd))
#print(resp.status_code)
#print(resp.text)

#User Digest Auth
url = "https://httpbin.org/digest-auth/auth/theuser/thepass"
resp = requests.get(url, auth=HTTPDigestAuth(user,passwd))
print(resp.status_code)
print(resp.text)

