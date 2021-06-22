import requests
from flask import Flask, render_template, request
import json
import time

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method=='POST':
        city=request.form['city']
        country=request.form['country']
        api_key='8fc42965aec6de6020e358eb9cc33f3d'
        weather_url=requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}, {country}&units=imperial')
        weather_data=weather_url.json()
        test=(weather_data['main']['temp']-32)
        temp=round(test/9*5)
        humidity=weather_data['main']['humidity']
        wind_speed=round(weather_data['wind']['speed']/1.6)
       
        return render_template('result.html', temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)


    return render_template('weather.html')

if __name__=='__main__':
    app.run(debug=True)
