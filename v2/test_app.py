import unittest
from app import app, patients

class HospitalSystemTests(unittest.TestCase):
    def setUp(self):
        patients.clear()
        self.client = app.test_client()

    def test_home(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_add_then_view(self):
        add = self.client.post('/patients', json={"name":"Anu", "age":21, "disease":"Fever"})
        self.assertEqual(add.status_code, 201)
        view = self.client.get('/patients')
        self.assertEqual(view.status_code, 200)
        self.assertEqual(view.get_json()['count'], 1)
        self.assertEqual(view.get_json()['patients'][0]['name'], 'Anu')

    def test_missing_fields(self):
        self.assertEqual(self.client.post('/patients', json={"name":"Anu"}).status_code, 400)

if __name__ == '__main__':
    unittest.main()
