"""Models for garden knowledge app."""

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


class Gardener(db.Model):
     """A user who is gardener."""

     __tablename__ = 'gardeners'

     gardener_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
     username = db.Column(db.String, unique=True)
     password = db.Column(db.String)

     favorite_crop = db.relationship('FavoriteCrop')

     def __repr__(self):
         return f'<User user_id={self.user_id} username={self.username}>'


class Crop(db.Model):
    """A crop."""

    __tablename__ = 'crops'

    crop_id = db.Column(db.Integer, primary_key=True)

    crop_name = db.Column(db.String)
    crop_description = db.Column(db.String)
    crop_sun = db.Column(db.String)
    crop_soil = db.Column(db.String)
    crop_planting_considerations = db.Column(db.String)
    crop_when_to_plant = db.Column(db.String)
    crop_growing_from_seed = db.Column(db.String)
    crop_spacing = db.Column(db.String)
    crop_watering = db.Column(db.String)
    crop_feeding = db.Column(db.String)
    crop_other_care = db.Column(db.String)
    crop_diseases = db.Column(db.String)
    crop_pests = db.Column(db.String)
    crop_harvesting = db.Column(db.String)
    crop_storage_use = db.Column(db.String)
    crop_image_url = db.Column(db.String)

    condition = db.relationship('CropCondition')
    favorite_crop = db.relationship('FavoriteCrop')
    

    def __repr__(self):
        return f'<Crop crop_id={self.crop_id} crop_name={self.crop_name}>'

class CropCondition(db.Model):
    """Conditions for each crop."""

    __tablename__ = 'crop_conditions'

    condition_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    crop_id = db.Column(db.Integer, db.ForeignKey('crops.crop_id'))
    crop_name = db.Column(db.String)
    lowest_min_temp = db.Column(db.Integer)
    highest_min_temp = db.Column(db.Integer)
    shade_ok = db.Column(db.String, nullable=False, default="False")
    soil_type = db.Column(db.String)

    crop = db.relationship('Crop')
    

    def __repr__(self):
        return f'<CropCondition condition_id={self.condition_id} crop_name={self.crop_name}>'

class FavoriteCrop(db.Model):
    """A gardener user's saved favorite crops."""

    __tablename__ = 'favorite_crops'

    favorite_id = db.Column(db.Integer, primary_key=True)
    gardener_id = db.Column(db.Integer, db.ForeignKey('gardeners.gardener_id'), nullable=False)
    crop_id = db.Column(db.Integer, db.ForeignKey('crops.crop_id'), nullable=False)

    gardener = db.relationship('Gardener')
    crop = db.relationship('Crop')

    def __repr__(self):
        return f'<FavoriteCrop gardener_id={self.gardener_id} crop_id={self.crop_id}>'


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