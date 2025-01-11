import requests
import pyttsx3
import json

city = input("Enter the name of the city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=0ede0845e1534af8a61133148251101&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
print(wdic["current"]["humidity"])

engine = pyttsx3.init()
engine.say("The current temperature in " + city + " is " + str(wdic["current"]["temp_c"]))
engine.runAndWait()
engine.say("The current humidity in " + city + " is " + str(wdic["current"]["humidity"]))
engine.runAndWait()
