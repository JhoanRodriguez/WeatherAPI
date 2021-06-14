import unittest
import requests


class ApiTest(unittest.TestCase):
    def test_valid_params(self):
        r = requests.get(
            'http://localhost:5000/weather?city=cali&country=CO')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()['Response']), 11)

    def test_invalid_city(self):
        r = requests.get(
            'http://localhost:5000/weather?city=12&country=CO')
        self.assertEqual(r.status_code, 404)
        self.assertEqual(len(r.json()['Response']), 2)

    def test_invalid_country(self):
        r = requests.get(
            'http://localhost:5000/weather?city=barranquilla&country=52')
        self.assertEqual(r.status_code, 404)
        self.assertEqual(len(r.json()['Response']), 2)

    def test_content_type(self):
        r = requests.get(
            'http://localhost:5000/weather?city=barranquilla&country=CO')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")


if __name__ == '__main__':
    unittest.main()
