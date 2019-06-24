from datetime import datetime

from static.imports import *
from tests.unit.unit_base_test import UnitBaseTest


class PsychologistTest(UnitBaseTest):
    def test_create_psychologist(self):

        date_text = "22-09-2018"
        date = datetime.strptime(date_text, '%d-%m-%Y').date()

        psychologist = PsychologistModel('0000000', 'test', date, None)

        self.assertEqual(psychologist.crp, '0000000',
                         "The crp of the psychologist after creation does not equal the constructor argument.")
        self.assertEqual(psychologist.password, 'test',
                         "The password of the psychologist after creation does not equal the constructor argument.")
        self.assertEqual(psychologist.date_of_birth, date,
                         "The date_of_birth of the psychologist after creation does not equal the constructor argument.")
        self.assertEqual(psychologist.person_psy_id, None,
                         "The person_psy_id of the psychologist after creation does not equal the constructor argument.")
