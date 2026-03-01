import requests

url = "https://tejas.vridhihomefinancen"

response = requests.get(url)

if response.status_code == 200:
    print(f"Successfully accessed {url}")
else:    
    print(f"Failed to access {url} with status code: {response.status_code}")