"""Server for garden knowledge app."""

from flask import (Flask, render_template, request, jsonify, flash, session,
                   redirect)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db
import crud
import requests

from jinja2 import StrictUndefined

import os
key_1 = os.environ['API_KEY_1']

app = Flask(__name__)
app.secret_key = "gardenslollol"
app.jinja_env.undefined = StrictUndefined
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/create-gardener', methods=['POST'])
def register_gardener():
    """Create a new gardener user."""

    username = request.form.get('username')
    password = request.form.get('password')

    gardener = crud.get_gardener_by_username(username)
    if gardener:
        flash('Username already taken. Please enter a different username.')
    else:
        crud.create_gardener(username, password)
        flash('Your Garden Knowledge account is created. Now please log in.')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login_gardener():
    """Log in gardener user."""

    username = request.form.get('username')
    password_to_check = request.form.get('password')

    gardener = crud.get_gardener_by_username(username)

    if password_to_check == gardener.password:
       session['gardener_id'] = gardener.gardener_id
       flash('You are logged in and ready to save your searches and favorites!')
    else:
       flash('Error. Incorrect password or username.')

    return redirect('/')

@app.route('/logout')
def logout_gardener():
    """Log out gardener user."""

    session.pop('gardener_id', None)

    flash('You are logged out.')

    return redirect('/')

@app.route('/create-favorite', methods=['POST'])
def add_favorite():
    """Add a new favorite crop to the 'database'."""

    crop_id = request.form.get('crop_id')
    print('PRINTING CROP ID********', crop_id)
    gardener_id = session['gardener_id']

    already_favorite_crop = crud.check_crop_favorites(crop_id, gardener_id)
    print('PRINTING IF ALREADY FAVORITE*******', already_favorite_crop)
    if already_favorite_crop:
        return "This crop has already been added to favorites."

    else:
        favorite_crop = crud.create_favorite_crop(gardener_id, crop_id)
        return "Added to favorites!"

@app.route('/favorites')
def favorites():
    """View all favorite crops."""

    gardener_id = session['gardener_id']

    crop_favorite_list = crud.get_crop_favorites(gardener_id)

    return render_template('favorites.html', crop_favorite_list=crop_favorite_list)

@app.route('/results')
def results():
    """View results of search."""

    city = request.args.get('city')
    shade_ok = request.args.get('shade_ok')
    soil_type = request.args.get('soil_type')

    res = requests.get(
        f'https://api.meteostat.net/v1/stations/search?q={city}&key={key_1}')

    city_data = res.json()

    city_list = city_data['data']

    city_id = city_list[0]['id']

    to_query_next = f'station={city_id}&start=2018-01&end=2019-12&key={key_1}'

    res2 = requests.get(
        f'https://api.meteostat.net/v1/history/monthly?{to_query_next}')

    weather_data = res2.json()

    weather_dict = weather_data['data']

    precipitation_values = []
    rain_days_values = []
    temp_min_values = []
    temp_max_values = []


    for month in weather_dict:
        precipitation_values.append(month['precipitation'])
        rain_days_values.append(month['raindays'])
        temp_min_values.append(month['temperature_min'])
        temp_max_values.append(month['temperature_max'])

    total_precipition = 0
    number_rain_days = 0

    for value in precipitation_values:
        total_precipition += value
    total_precipition = total_precipition / 2
    #Note this is divided by 2 because requested 2 years data
    
    for value in rain_days_values                                          :
        number_rain_days += value
    number_rain_days = number_rain_days / 2
    # Note this is divided by 2 because requested 2 years data

    sorted_temp_min_values = sorted(temp_min_values)
    min_temp = (sorted_temp_min_values[0] * (9/5) + 32)
    # #Note converted to Fahrenheit from Celsius

    sorted_temp_max_values = sorted(temp_max_values)
    max_temp = (sorted_temp_max_values[-1] * (9/5) + 32)
    # #Note converted to Fahrenheit from Celsius

    crop_list = crud.get_crop_recommendations(min_temp, shade_ok, soil_type)

    return render_template('results.html', city=city, city_data=city_data, city_list=city_list,
        city_id=city_id, weather_dict=weather_dict, precipitation_values=precipitation_values,
        rain_days_values=rain_days_values, temp_min_values=temp_min_values,
        temp_max_values=temp_max_values, total_precipition=total_precipition,
        number_rain_days=number_rain_days, min_temp=min_temp, max_temp=max_temp,
        cropList=crop_list)

    #Note this works for Amarillo but not San Jose. Need to filter city list
    #results to only be for US and/or have file still work if no values
    #received back from user search. So far if no values received back,
    #then min_temp and max_temp variables are breaking

if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    DebugToolbarExtension(app)
    app.run(host='0.0.0.0', debug=True)