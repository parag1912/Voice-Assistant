import requests

api_address='https://api.openweathermap.org/data/2.5/weather?q=delhi&appid=a3bece8ba1177f29b8e3c8ed37d4c3f7'
json_data=requests.get(api_address).json()

def temp():
    temperature= round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description=json_data["weather"][0]["description"]   
    return description

print(temp())
print(des())
