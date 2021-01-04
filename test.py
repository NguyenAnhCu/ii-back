import requests

Base = "http://127.0.0.1:5000/"
response = requests.get(Base + "Questions/Questions2")
print(response.json())