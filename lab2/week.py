import requests
s_city = "Moscow,RU"
appid = "809dc40577ce3e5eb5aea1cf8617c844"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], ">" )
    print("Температура <", '{0:+3.0f}'.format(i['main']['temp']),">")
    print("Погодные условия <", i['weather'][0]['description'], ">")
    print("Скорость ветра <", i['wind']['speed'], ">")
    print("Видимость <", i['visibility'], ">")
    print("__________________________________")