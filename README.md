Installation
1. createdb cropweather
2. git clone the repo
3. within the main folder, create a secret.sh file that has export_key="insert_key" where "insert_key" is a string of an API key from Meteostat
4. within the main folder, create a virtual environment
5. activate the virtual environment
6. pip install the requirements
7. source secret.sh
8. python3 seed_database.py to create tables and seed the database
9. python3 server.py to start the server
10. open the browser at http://localhost:5000


Tech Stack
-Python
-SQLAlchemy
-Postgresql
-flask
-JavaScript
-jQuery
-AJAX
