# importing requests and json
import requests, json


def weather():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # City Name 
    CITY = "Mysore"
    # API key 
    API_KEY = "API KEY"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request

    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        
        weather_report = f"temperature is {temperature} humidity is {humidity} pressure is {pressure} and weather is {report[0]['description']}"
        # print(weather_report)
        return weather_report   
    else:
        # showing the error message
        return "Error in the HTTP request"

# weather()

