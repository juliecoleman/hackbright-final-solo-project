![alt text](https://github.com/juliecoleman/hackbright-final-solo-project/static/img/Garden_Knowledge green.png)

###### Garden knowledge provides personalized gardening recommendations and information to help with garden success. Garden Knowledge begins by using data from the USDA’s plant hardiness zones via an API, Frostline, to determine the local growing climate based on the user’s zip code. Then, from additional optional information given by the user for planting month, available sunlight, soil conditions, and desired difficulty, Garden Knowledge gives recommendations of vegetables to grow and how from a gardening API, Harvest Helper, based on data conditions collected and designed for this project.  The user has the option to save favorite vegetables and retrieve back a list of their favorites to reference when they are ready to start gardening.

------------------

## Tech Stack
###### Python, JavaScript, SQLAlchemy, PostgreSQL, Flask, JQuery, AJAX, Bootstrap

-------
## Features
##### **User account**
###### User creates and account and logs in on the homepage navbar.


### User query
###### User selects options to query for gardening recommendations, including zipcode (to determine USDA plant hardiness zone), planting month, shade, soil type, soil ph, and difficulty level.

### User results
###### User receives back their plant hardiness zone and suggested vegetables for their garden based on their query. Each vegetable has details on: how to plant (from HarvestHelper), when to plant for any given plant hardiness zone, what its preferences for soil and shade are, and what its difficulty is.


### User favorites
###### User saves favorite vegetables from their results. User can perform a new query or go to their favorites list.

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