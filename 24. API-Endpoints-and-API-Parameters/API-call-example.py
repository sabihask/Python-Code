import requests


response = requests.get("http://api.open-notify.org/iss-now.json")

print(response)
print(response.status_code)
# data = response.json()
data = response.json()["iss_position"]
longitude = data = response.json()["iss_position"]["longitude"]
latitude = data = response.json()["iss_position"]["latitude"]
address = (longitude, latitude)
print(data)
print(address)
