import requests

def get_weather_info(city_name):
    # Endpoint
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=fc3586f528eb37570d7a83b0744fa23b&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temp = weather_data['main']['temp']
        hp_temp = weather_data['main']['feels_like']        
        humid = weather_data['main']['humidity']
        cloudiness = weather_data['clouds']['all']
        city = weather_data['name']

        print()
        print("              WEATHER DETAILS")
        print("City: ", city)
        print("Temperature: ", temp, "     Feels like: ", hp_temp)
        print("Humidity: ", humid)
        print("Cloudiness %: ", cloudiness)

    else:
        print(response.status_code)
        print("ERROR: Data is not ready for display!")


def main():
    print("Welcome to Weather Detection AI - YOUR TRUSTED WEATHER DETECTOR")

    while True:
        user_input = input("Please enter the name of the city to get its weather, or type 'exit' to quit: ")

        if user_input.lower() == "exit":
            print("Alright! See you later!")
            break
        elif not user_input.strip():
            print("Error! Kindy enter an appropriate city name.")
        else:
            get_weather_info(user_input)

main()