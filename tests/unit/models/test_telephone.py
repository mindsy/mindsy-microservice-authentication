from models.telephone import TelephoneModel
from tests.unit.unit_base_test import UnitBaseTest


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        telephone = TelephoneModel('000000000', 'comercial', None)

        self.assertEqual(telephone.number, '000000000',
                         "The number of the telephone after creation does not equal the constructor argument.")
        self.assertEqual(telephone.telephone_type, 'comercial',
                         "The telephone type of the telephone after creation does not equal the constructor argument.")
        self.assertEqual(telephone.tel_person_id, None,
                         "The id person of the person after creation does not equal the constructor argument.")
