"""Server for garden knowledge app."""

from flask import (Flask, render_template, request, jsonify, flash, session,
                   redirect)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db
import crud
import requests

from jinja2 import StrictUndefined

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

    if gardener != None:

        if password_to_check == gardener.password:
           session['gardener_id'] = gardener.gardener_id
           flash('You are logged in and ready to save your searches and favorites!')
        else:
           flash('Error. Incorrect password.')

    else:
        flash('Error. Username does not exist.')

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

# @app.route('/favorites')
# def favorites():
#     """View all favorite crops."""

#     gardener_id = session['gardener_id']

#     crop_favorite_list = crud.get_crop_favorites(gardener_id)

#     shade_difficulty_dictionary = crud.get_crop_conditions_shade_difficulty()

#     zone_month_dictionary = crud.get_crop_conditions_zone_month()

#     soil_dictionary = crud.get_crop_conditions_soil()

#     return render_template('favorites.html', 
#         crop_favorite_list=crop_favorite_list, 
#         shade_difficulty_dictionary=shade_difficulty_dictionary, 
#         zone_month_dictionary=zone_month_dictionary, 
#         soil_dictionary=soil_dictionary)

@app.route('/results')
def results():
    """View results of search."""

    zipcode = request.args.get('zipcode')
    shade_ok = request.args.get('shade_ok')
    planting_month = request.args.get('planting_month')
    soil_type = request.args.get('soil_type')
    soil_ph = request.args.get('soil_ph')
    difficulty = request.args.get('difficulty')

    if zipcode != "":

        res = requests.get(
            f'https://phzmapi.org/{zipcode}.json')

        zipcode_data = res.json()

        plant_hardiness_zone = zipcode_data['zone'][0]

    else:
        plant_hardiness_zone = 'unknown'

    crop_list = crud.get_crop_recommendations(plant_hardiness_zone,  
                                              planting_month, shade_ok, 
                                              soil_type, soil_ph, difficulty)

    shade_difficulty_dictionary = crud.get_crop_conditions_shade_difficulty()

    zone_month_dictionary = crud.get_crop_conditions_zone_month()

    soil_dictionary = crud.get_crop_conditions_soil()

    return render_template('results.html', 
        plant_hardiness_zone=plant_hardiness_zone, crop_list=crop_list,
        shade_difficulty_dictionary=shade_difficulty_dictionary, 
        zone_month_dictionary=zone_month_dictionary, 
        soil_dictionary=soil_dictionary)


if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    DebugToolbarExtension(app)
    app.run(host='0.0.0.0', debug=True)