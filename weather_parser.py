import pyowm # https://github.com/csparpa/pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")

place = input("В каком городе?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp_current = w.get_temperature('celsius')["temp"]
wind = w.get_wind()["speed"]
hum = w.get_humidity()


#print(w)                      
print("\nВ городе {} сейчас {}\n".format(place, w.get_detailed_status()))
print("Температура: {}\N{DEGREE SIGN}C\n".format(str(temp_current)))
print("Скорость ветра: {} м/c\n".format(str(wind)))
print("Относительная влажность воздуха: {}%\n".format(str(hum)))

if temp_current < 10:
	print("Прохладно, оденься теплее! На улице, чай, не Франция!")
elif (temp_current > 10 and temp_current < 25):
	print("Температура норм.")
else:
	print("Очень жарко! Не выходи из комнаты! Не совершай ошибку!")
	