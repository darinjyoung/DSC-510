# DSC 510
# Week 12
# Final Project
# Author Darin Young
# 5/28/2024

import requests


weather_url = "http://api.openweathermap.org/data/2.5/weather"
headers = {'cache-control': 'no-cache'}
userAPI = "5d7de6ef59ebd0545016ef186d137b6d"


def location_getter(query, unitSelection, url):
    response = requests.request("GET", url, headers=headers, params=query)

    data = response.json()

    if response.status_code == 200:
        latitude = data['lat']
        longitude = data['lon']

        query_string = {"lat": latitude,
                        "lon": longitude,
                        "units": unitSelection,
                        "APPID": userAPI}

        forecast_getter(query_string)
    else:
        print(f"Error {response.status_code}: {data.get('message', 'Failed to retrieve data')}")


def forecast_getter(query):
    response = requests.request("GET", weather_url, headers=headers, params=query)
    data = response.json()

    if response.status_code == 200:
        pretty_print(data)
    else:
        print(f"Error {response.status_code}: {data.get('message', 'Failed to retrieve data')}")


def unit_selector():
    done = False

    unitMenu = """
            1: Fahrenheit
            2: Celsius
            3: Kelvin"""

    while not done:

        print(unitMenu)

        menuSelection = input("\nPlease select how you want the temperature to be displayed: ")

        if menuSelection == "1":
            unitSelection = "imperial"
            done = True
        elif menuSelection == "2":
            unitSelection = "metric"
            done = True
        elif menuSelection == "3":
            unitSelection = "standard"
            done = True
        else:
            print("Please make a valid selection.")

    return unitSelection


def weather_by_zip():
    zip_geocode_url = "http://api.openweathermap.org/geo/1.0/zip"

    done = False

    while not done:
        try:
            userZipCode = input("Please enter the zip code for which you want to know the forecast: ")
            if len(userZipCode) == 5 and userZipCode.isdigit():
                userZipCode = int(userZipCode)

                query_string = {"zip": userZipCode,
                                "APPID": userAPI}

                unitSelection = unit_selector()
                location_getter(query_string, unitSelection, zip_geocode_url)

                done = True
            else:
                print("Please enter exactly 5 digits.")
        except ValueError:
            print("Please enter a valid 5-digit number.")


def weather_by_citystate():
    citystate_url = "http://api.openweathermap.org/geo/1.0/direct"

    done = False

    while not done:
        userCity = input("Please enter the name of the city for which you want to know the forecast: ")
        userState = input("Please enter the state of the city for which you want to know the forecast: ")

        query_string = {"q": userCity + "," + userState + ",US",
                        "APPID": userAPI}

        unitSelection = unit_selector()
        location_getter(query_string, unitSelection, citystate_url)

        done = True


def pretty_print(data):
    temp = data["main"]["temp"]
    city = data["name"]
    feelsLike = data["main"]["feels_like"]
    highTemp = data["main"]["temp_max"]
    lowTemp = data["main"]["temp_min"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"""
City name: {city}
Current Temperature: {temp} degrees
Feels Like: {feelsLike} degrees
High Temperature: {highTemp} degrees
Low Temperature: {lowTemp} degrees
Pressure: {pressure} hPa
Humidity: {humidity}%
Description: {description.title()}
""")


menu = """\nWeather Forecast Helper

        0: Exit Program
        1: Use Zip Code
        2: Use City/State"""


def main():
    done = False

    while not done:
        print(menu)

        menuSelection = input("\nPlease make a selection: ")

        if menuSelection == "0":
            done = True
        elif menuSelection == "1":
            weather_by_zip()
        elif menuSelection == "2":
            weather_by_citystate()
        else:
            print("Please make a valid selection.")


if __name__ == "__main__":
    main()

