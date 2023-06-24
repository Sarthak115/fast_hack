import requests
import datetime

api = "3f18fbf7c3bb74f06997a9895159c35e"  # API key
city = input("Enter the name of the city: ")
base = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
response = requests.get(base).json()

print("Weather report for", city)
temperature = response["main"]["temp"] - 273
temperature_max = response["main"]["temp_max"] - 273
temperature_min = response["main"]["temp_min"] - 273

print("Temperature: {:.2f} Celsius".format(temperature))
print("Maximum temperature: {:.2f} Celsius".format(temperature_max))
print("Minimum temperature: {:.2f} Celsius".format(temperature_min))

print("Pressure:", response["main"]["pressure"], "hPa")
print("Humidity:", response["main"]["humidity"], "%")
print("Wind Speed:", response["wind"]["speed"], "m/s")
print("Wind direction:", response["wind"]["deg"])
print("Cloudiness:", response["clouds"]["all"], "%")
print("Country:", response["sys"]["country"])

sunrise_timestamp = response["sys"]["sunrise"]
utc_datetime = datetime.datetime.utcfromtimestamp(sunrise_timestamp)
offset = datetime.timedelta(hours=5, minutes=30)  # IST offset is +05:30
sunrise_datetime_local = utc_datetime + offset
sunrise_time = sunrise_datetime_local.strftime("%H:%M:%S")

sunset_timestamp = response["sys"]["sunset"]
utc_datetime = datetime.datetime.utcfromtimestamp(sunset_timestamp)
sunset_datetime_local = utc_datetime + offset
sunset_time = sunset_datetime_local.strftime("%H:%M:%S")

print("Sunrise time (IST):", sunrise_time)
print("Sunset time (IST):", sunset_time)

print("City:", response["name"])
print("Timezone:", response["timezone"])
print("Location id:", response["id"])
print("Coordinates: {lon}, {lat}".format(lon=response["coord"]["lon"], lat=response["coord"]["lat"]))