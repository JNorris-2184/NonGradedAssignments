import requests

#Create basic request for data
#response = requests.get("http://httpbin.org/xml")
#print(response.status_code)
#print(response.text)

#Create request using parameters
#args = {"key1":1,"key2":"two","key3":False}
#response = requests.get("http://httpbin.org/get", params=args)
#print(response.status_code)
#print(response.text)
#print(response.url)

#Create a request using POST
#response = requests.post("http://httpbin.org/post",data={"key","value"})
#print(response.text)

#Create a request using custom header
heads = {"my-custom-header": "This is a custom header"}
response = requests.get("http://httpbin.org/get", headers=heads)
print(response.text)
