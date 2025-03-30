import requests

endpoint = "https://www.httpbin.org/status/200/"
endpoint = "https://www.httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint,json={"product_id":123}) # API ( Application programming interface )-> Method 
# print(get_response.json())
# print(get_response.status_code)

# get_response = requests.get(endpoint, json={"product_id":123})
get_response = requests.post(endpoint, json={"title":"Hello world"})
print(get_response.json())

# get_response = requests.get(endpoint,json={"product_id":123})
# print(get_response.text)