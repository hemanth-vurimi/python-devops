import requests
import json


name = input("Enter the name: ")
api_url = f"https://api.agify.io/?name={name}"
response = requests.get(url= api_url)

# print(dir(response))          # just to check what operations we can perform on the responses
for key,value in response.json().items():
    print(key,value)
    data = response.json()