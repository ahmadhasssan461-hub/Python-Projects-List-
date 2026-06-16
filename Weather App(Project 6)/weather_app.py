import requests
class weather:
        def __init__(self):
            self.api = "use your own "
            city = input("Enter Your City Name:")
            if city.lower() == "exit":
                print("Allah Hafiz! 👋")
                return False
            try:
                response = requests.get(
                    self.url,
                    params ={
                        "q" :city,
                        "appid" : self.api,
                        "units" : "metric",
                    }
                )
                data = response.json()
                city  = data["name"]
                temp  = data["main"]["temp"]
                humidity  = data["main"]["humidity"]
                description  = data["weather"][0]["description"]
                print(f"City: {city}")
                print(f"Temperature: {temp}°C")
                print(f"Humidity: {humidity}%")
                print(f"Weather: {description}")
            
            except:
                print("City Does Not Found :")
                return True
app = weather()
while True:
    result = app.get_weather()
    
    if result == False:
        break
            
