from models.hospital import HospitalModel
from tests.unit.unit_base_test import UnitBaseTest


class HospitalTest(UnitBaseTest):
    def test_create_hospital(self):
        hospital = HospitalModel('00000000000000', 'test', None)

        self.assertEqual(hospital.registry_number, '00000000000000',
                         "The name of the person after creation does not equal the constructor argument.")
        self.assertEqual(hospital.social_reason, 'test',
                         "The email of the person after creation does not equal the constructor argument.")
        self.assertEqual(hospital.hospital_person_id, None,
                         "The email of the person after creation does not equal the constructor argument.")

    def test_hospital_json(self):
        hospital = HospitalModel('00000000000000', 'test', None)
        expected = {
            'registry_number': '00000000000000', 'social_reason': 'test'
        }

        self.assertEqual(
            hospital.json(),
            expected,
            "The JSON export of the person is incorrect. Received {}, expected {}.".format(hospital.json(), expected))
