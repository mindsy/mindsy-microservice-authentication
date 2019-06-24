from models.person import PersonModel
from tests.unit.unit_base_test import UnitBaseTest


class PersonTest(UnitBaseTest):
    def test_create_item(self):
        person = PersonModel('test', 'test@test.com')

        self.assertEqual(person.name, 'test',
                         "The name of the person after creation does not equal the constructor argument.")
        self.assertEqual(person.email, 'test@test.com',
                         "The email of the person after creation does not equal the constructor argument.")

    def test_person_json(self):
        person = PersonModel('test', 'test@gmail.com')
        expected = {
            'id_person': None, 'name': 'test', 'email': 'test@gmail.com', 'telephone': []
        }

        self.assertEqual(
            person.json(),
            expected,
            "The JSON export of the person is incorrect. Received {}, expected {}.".format(person.json(), expected))
