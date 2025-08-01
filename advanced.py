import requests

#use a timeout value for a request
#resp = requests.get("https://httpbin.org/delay/0.5",timeout=1.0)
#print(resp.status_code)

#Introspect the redirection history
#resp = requests.get("http://github.com")
#print(resp.url)
#print(resp.history)
#orig = resp.history.pop()
#print(orig.status_code)
#print(orig.url)
#print(orig.reason)

#use session object to group requests and settings
sess = requests.Session()
sess.get("https://httpbin.org/cookies/set/sample/123456789")
resp = sess.get("http://httpbin.org/cookies")
print(resp.text)

#code to change session headers
sess.headers.update({"...."}
