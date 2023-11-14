import pyowm

#enter your API
#введите свой API
owm = pyowm.OWM('6c20fc419dd52500c805c0a677f05447')


observation = owm.weather_at_place("Rostov-on-Don")
w = observation.get_weather()

#узнаем градусы с помощью w.get_
#find out degrees using w.get_
temp = w.get_temperature('celsius')["temp"]

#проверка погоды, как нам одется?
#checking the weather, how should we dress?
if temp < 10:
    print("Cold")
    
elif temp < 18:
    print("cool")
    
elif temp > 18:
    print("heat")
