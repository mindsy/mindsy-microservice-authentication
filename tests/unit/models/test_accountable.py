from static.imports import *
from tests.unit.unit_base_test import UnitBaseTest


class AccountableTest(UnitBaseTest):
    def test_create_accountable(self):
        accountable = AccountableModel('00000000000', 'test', None)

        self.assertEqual(accountable.registry_number_acc, '00000000000',
                         "The registry_number_acc of the accountable after creation does not equal the constructor argument.")
        self.assertEqual(accountable.kinship_degree, 'test',
                         "The kinship_degree of the accountable after creation does not equal the constructor argument.")
        self.assertEqual(accountable.accountable_person_id, None,
                         "The accountable_person_id of the accountable after creation does not equal the constructor argument.")
