"""Models for garden knowledge app."""

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


# class User(db.Model):
#     """A user."""

#     __tablename__ = 'users'

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     username = db.Column(db.String, unique=True)
#     password = db.Column(db.String)

#     # ratings = a list of Rating objects

#     def __repr__(self):
#         return f'<User user_id={self.user_id} username={self.username}>'


# class User_query(db.Model):

# class Climate_info(db.Model):

# class Crop(db.Model):

# class Favorite_crops(db.Model):

# class Past_query(db.Model):

def connect_to_db(flask_app, db_uri='postgresql:///cropweather', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)