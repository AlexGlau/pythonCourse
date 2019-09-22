import requests

def weather_by_city(city_name):
    weather_url = 'https://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': 'e39d72d9963143fd95d125731192109',
        'query': city_name,
        'format': 'json',
        'num_of_days': 1
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if 'data' in weather:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    except(requests.RequestException):
        print('Network error')
        return False
    return False

if __name__ == '__main__':
    w = weather_by_city('Yekateringburg,Russia')
    print(w)
