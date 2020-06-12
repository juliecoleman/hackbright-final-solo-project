from unittest import TestCase
from server import app
from model import db, Gardener, Crop, CropCondition, FavoriteCrop, connect_to_db
import crud
# from flask import session

class FlaskTestsRoute(TestCase):
    """Testing routes in Flase."""

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'gardenslollol'

        #Note both a session and database setup are needed for functions 
        #test_results and test_favorites to work. Therefore, the code below.
        with self.client as c:
            with c.session_transaction() as sess:
                sess['gardener_id'] = 1

        connect_to_db(app, "postgresql:///cropweather")
        db.create_all()

    def test_index(self):
        """Testing route to homepage."""

        result = self.client.get("/")
        self.assertIn(b"Welcome to Garden", result.data)

    def test_favorites(self):
        """Testing route to favorites."""

        result = self.client.get("/favorites")
        self.assertIn(b"Here are your favorites", result.data)

    def test_results(self):
        """Testing route to results."""

        result = self.client.get("/favorites")
        self.assertIn(b"Here are your favorites", result.data)



class FlaskTestsCreatingFavorite(TestCase):
    """Testing adding a favorite to the favorite_crops table."""

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///cropweather")
        db.create_all()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['gardener_id'] = 1

    def test_favorite_crops_table(self):
        """Testing adding a favorite to the favorite_crops tablete."""
        with self.client as c:
            result = c.post("/create-favorite",
                            data={'crop_id': 4}
                            )
        self.assertIn(b"to favorites", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()