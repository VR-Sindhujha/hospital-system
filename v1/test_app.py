import unittest
from app import app, patients

class HospitalSystemTests(unittest.TestCase):
    def setUp(self):
        patients.clear()
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['version'], 'v1')

    def test_add_patient(self):
        response = self.client.post('/patients', json={"name":"Anu", "age":21, "disease":"Fever"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['patient']['name'], 'Anu')

    def test_missing_fields(self):
        response = self.client.post('/patients', json={"name":"Anu"})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
