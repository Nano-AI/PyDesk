from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json


def weather_setup():
    global driver, url
    url = "https://www.google.com/search?q=what+is+the+weather+right+now"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    with open('./config/settings.json', 'r') as f:
        data = json.load(f)
        if data['driver-dir'] == "":
            print("Didn't find Chrome driver... Installing...")
            data['driver-dir'] = ChromeDriverManager().install()
            print("Chrome Driver installed at " + data['driver-dir'])
        else:
            print("Chrome Driver found in settings.json")
        print('Running Driver')
        driver = webdriver.Chrome(data['driver-dir'], chrome_options=options)


def get_weather() -> str:
    driver.get(url)
    with open('./config/settings.json') as weatherF:
        weatherData = json.load(weatherF)
        if weatherData['weather-settings']['weather-type'].lower() == 'f':
            weather = driver.find_elements_by_id("wob_tm")
        elif weatherData['weather-settings']['weather-type'].lower() == 'c':
            weather = driver.find_elements_by_id("wob_tmm")
        else:
            raise Exception(f'Unknown value {weatherData["weather-type"]}')
        return_arr = []
        for post in weather:
            return_arr.append(post.text)
    return return_arr[0]
