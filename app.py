from datetime import datetime
from flask import Flask, render_template, request
import requests
from time import ctime

app = Flask(__name__)

# OpenWeatherMap API key
WEATHER_API_KEY = 'bb21adf986c50e7b733e0aafb1e010d6'

# api-ninja API key 
FACT_API_KEY = 'eKmKcsLdh/+gNnghYGRy5w==Qqn8BzisSdtfzWIM'

@app.route('/', methods=['GET', 'POST'])
def index():
    location = None
    weather_data = None

    if request.method == 'POST':
        location = request.form['location']

        # Fetch weather data from OpenWeatherMap API and converts it to JSON string
        weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={WEATHER_API_KEY}')
        weather_data = weather_response.json()

    CITY_URL = (f'https://api.api-ninjas.com/v1/city?name={location}')

    city = requests.get(CITY_URL, headers={'X-Api-Key': FACT_API_KEY}).json()

    country_code = ''

    # Unpacking the API response from api-ninja to get the country code
    for i in city:
        for k in i:
            if k == 'country':
                country_code = i[k]

    # Generating the API call URL with country code variable
    COUNTRY_URL = (f'https://api.api-ninjas.com/v1/country?name={country_code}')

    # Generating the API call URL with city name variable
    HISTORICAL_EVENT_URL = (f'https://api.api-ninjas.com/v1/historicalevents?text={location}')
    
    # Fetch historical events data from api-ninja and converts data to JSON string
    historical_events = requests.get(HISTORICAL_EVENT_URL, headers={'X-Api-Key': FACT_API_KEY}).json()

    # Fetch country statistics from api-ninja and converts data to JSON string
    country = requests.get(COUNTRY_URL, headers={'X-Api-Key': FACT_API_KEY}).json()

    try:
        return render_template('index.html', location=location, weather_data=weather_data, city=city, country=country,historical_events=historical_events)
    except Exception as e:
	    return render_template("error.html", error = str(e))

@app.template_filter('ctime')
def timectime(s):
    return ctime(s)

@app.template_filter('unix_to_datetime')
def unix_to_datetime(unix_time):
    return datetime.utcfromtimestamp(int(unix_time)).strftime('%H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)