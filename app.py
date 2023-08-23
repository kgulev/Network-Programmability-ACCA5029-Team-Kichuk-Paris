from datetime import time
from flask import Flask, render_template, request
import requests
import json
from time import ctime

app = Flask(__name__)

# Weather API key
WEATHER_API_KEY = 'bb21adf986c50e7b733e0aafb1e010d6'

# Fact API key (if needed)
FACT_API_KEY = 'eKmKcsLdh/+gNnghYGRy5w==Qqn8BzisSdtfzWIM'



@app.route('/', methods=['GET', 'POST'])
def index():
    location = None
    weather_data = None
    fact = None

    if request.method == 'POST':
        location = request.form['location']

        # Fetch weather data from the API
        weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={WEATHER_API_KEY}')
        weather_data = weather_response.json()

        # Fetch an interesting fact about the location (optional)
        # if FACT_API_KEY:
        #     fact_response = requests.get(f'http://api.example.com/facts?location={location}&apiKey={FACT_API_KEY}')
        #     fact_data = fact_response.json()
        #     fact = fact_data.get('fact')

    
    CITY_URL = (f'https://api.api-ninjas.com/v1/city?name={location}')

    city = requests.get(CITY_URL, headers={'X-Api-Key': FACT_API_KEY}).json()

    cc = json.dumps(city)

    country_code = ''

    for i in city:
        for k in i:
            if k == 'country':
                country_code = i[k]

    COUNTRY_URL = (f'https://api.api-ninjas.com/v1/country?name={country_code}')


    icon_code = ''

    HISTORICAL_EVENT_URL = (f'https://api.api-ninjas.com/v1/historicalevents?text={location}')
    
    historical_events = requests.get(HISTORICAL_EVENT_URL, headers={'X-Api-Key': FACT_API_KEY}).json()

    ICON_URL = (f'https://openweathermap.org/img/wn/{icon_code}')

    #country = country_code
    country = requests.get(COUNTRY_URL, headers={'X-Api-Key': FACT_API_KEY}).json()

    #return render_template('index.html', location=location, weather_data=weather_data, fact=fact)
    return render_template('index.html', location=location, weather_data=weather_data, city=city, country=country,historical_events=historical_events)

@app.template_filter('ctime')
def timectime(s):
    return ctime(s)

if __name__ == '__main__':
    app.run(debug=True)
