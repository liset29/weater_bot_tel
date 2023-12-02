import os
import requests

API_KEY="b9acf1c430fb055964b398061d6c5f11"
send_message="sendMessage"
token="6680899279:AAErsnZiHy8rUTaQLbJDcM3kvKYTQT4614c"
g="хз"
def get_weather(city,chat_id,API_KEY):
    try:
        response=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}")
        city_data=response.json()[0]

        lat=city_data["lat"]
        lon=city_data["lon"]

        r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric")
        city_temp=r.json()

        temp=int(city_temp["main"]["temp"])
        return f"Температура в городе {city} : {temp} граудсов цельсия"

    except Exception as ex:
        print(ex)
        requests.get(f"https://api.telegram.org/bot{token}/{send_message}?chat_id={chat_id}&text=напиши город")

def main(city,chat_id):
    result=get_weather(city,chat_id,API_KEY)
    return result



