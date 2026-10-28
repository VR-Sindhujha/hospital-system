import unittest
from app import app, patients

class HospitalSystemTests(unittest.TestCase):
    def setUp(self):
        patients.clear()
        self.client = app.test_client()

    def test_add_view_delete(self):
        add = self.client.post('/patients', json={"name":"Anu", "age":21, "disease":"Fever"})
        self.assertEqual(add.status_code, 201)
        patient_id = add.get_json()['patient']['id']
        self.assertEqual(self.client.get('/patients').get_json()['count'], 1)
        deleted = self.client.delete(f'/patients/{patient_id}')
        self.assertEqual(deleted.status_code, 200)
        self.assertEqual(self.client.get('/patients').get_json()['count'], 0)

    def test_delete_missing_patient(self):
        self.assertEqual(self.client.delete('/patients/999').status_code, 404)

    def test_missing_fields(self):
        self.assertEqual(self.client.post('/patients', json={"name":"Anu"}).status_code, 400)

if __name__ == '__main__':
    unittest.main()
