import requests


# getting the data from the Calgary Open Data API
url = "https://data.calgary.ca/resource/35ra-9556.json"

# making a GET request to the API
response = requests.get(url)

# error handling for the request
if response.status_code == 200:
    data = response.json()
    with open("calgary_traffic_incidents.json", "w") as f:
        f.write(response.text)
    print(data)
else:
    print(f"Error: {response.status_code}")