![alt text](https://github.com/juliecoleman/hackbright-final-solo-project/blob/master/static/img/Garden_Knowledge-green.png?raw=true)

###### Garden knowledge provides personalized gardening recommendations and information to help with garden success. Garden Knowledge begins by using data from the USDA’s plant hardiness zones via an API, Frostline, to determine the local growing climate based on the user’s zip code. Then, from additional optional information given by the user for planting month, available sunlight, soil conditions, and desired difficulty, Garden Knowledge gives recommendations of vegetables to grow and how from a gardening API, Harvest Helper, based on data conditions collected and designed for this project.  The user has the option to save favorite vegetables and retrieve back a list of their favorites to reference when they are ready to start gardening.

------------------

## Tech Stack
###### Python, JavaScript, JQuery, AJAX, SQLAlchemy, PostgreSQL, Flask, Bootstrap

-------
## Features

### User account login and query
###### User creates an account and logs in on the homepage navbar. User selects options to query for gardening recommendations. Options include zipcode (to determine USDA plant hardiness zone), planting month, shade, soil type, soil ph, and difficulty level.
![alt text](https://github.com/juliecoleman/hackbright-final-solo-project/blob/master/static/img/homepage.PNG?raw=true)

### User results
###### User receives back their plant hardiness zone based on their zipcode. User also receives suggested vegetables for their garden based on the plant hardiness zone and the other query options selected. Each vegetable has selectable details on: how to plant (from the API Harvest Helper), when to plant for any given plant hardiness zone, preferences for soil and shade, and difficulty level.
![alt text](https://github.com/juliecoleman/hackbright-final-solo-project/blob/master/static/img/results.PNG?raw=true)

### User favorites
###### User saves favorite vegetables from their results. User can perform a new query or go to their favorites list that has a compilation of all their favorites vegetables and their selectable details.
![alt text](https://github.com/juliecoleman/hackbright-final-solo-project/blob/master/static/img/favorites.PNG?raw=true)

-------------------

## Installation
###### 1. createdb cropweather
###### 2. git clone the repo
###### 3. within the main folder, create a secrets.sh file that has export_key="insert_key" where "insert_key" is a string of an API key from [Harvest Helper](https://harvesthelper.herokuapp.com/developers)
###### 4. within the main folder, create a virtual environment
###### 5. activate the virtual environment
###### 6. pip install the requirements
###### 7. source secrets.sh
###### 8. python3 seed_database.py to create tables and seed the database
###### 9. python3 server.py to start the server
###### 10. open the browser at http://localhost:5000