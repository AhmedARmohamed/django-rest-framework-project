import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"

get_request = requests.get(endpoint) # HTTP Request
# print(get_request.json())
print(get_request.text)
print(get_request.status_code)