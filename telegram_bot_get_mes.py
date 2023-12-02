import weather_get

import requests


token="6680899279:AAErsnZiHy8rUTaQLbJDcM3kvKYTQT4614c"
get_updates="getUpdates"
send_message="sendMessage"

getting_updates=requests.get(f"https://api.telegram.org/bot{token}/{get_updates}")
offset=getting_updates.json()["result"][-1]["update_id"]
getting_updates=requests.get(f"https://api.telegram.org/bot{token}/{get_updates}?offset={offset}")




def get_message(chat_id,i):
     try:
         text=(i["message"]["text"])
         city_tepmp=weather_get.main(text,chat_id)

        
         if city_tepmp:
            requests.get(f"https://api.telegram.org/bot{token}/{send_message}?chat_id={chat_id}&text={city_tepmp}")
            requests.get(f"https://api.telegram.org/bot{token}/{send_message}?chat_id={chat_id}&text=напиши город")
            return i["update_id"]+1
     except Exception as ex:
        print(ex)
        requests.get(f"https://api.telegram.org/bot{token}/{send_message}?chat_id={chat_id}&text=напиши город")
         
     

         

while True:
    getting_updates=requests.get(f"https://api.telegram.org/bot{token}/{get_updates}")

    for i in getting_updates.json()["result"]:
         chat_id=i["message"]["chat"]["id"]

         if  "message" in i and i["update_id"] == offset:         
            offset=get_message(chat_id,i)


