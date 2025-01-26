import unittest
from app import app
from unittest.mock import patch


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_add_product(self):
        """
        Test response when a product is added using the provided API.
        """

        response = self.client.get('/api/v1/delivery-order-price?'
                                   'venue_slug=home-assignment-venue-helsinki&'
                                   'cart_value=1000&user_lat=60.16094&user_lon=24.93087')

        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["delivery"]["fee"], 390)


if __name__ == '__main__':
    unittest.main()
