from static.imports import *
from tests.unit.unit_base_test import UnitBaseTest


class PsychologistHospitalTest(UnitBaseTest):
    def test_create_psychologist_hospital(self):
        psychologist_hospital = PsychologistHospitalModel(None, '0000000')

        self.assertEqual(psychologist_hospital.hospital_registry_number, None,
                         "The hospital_registry_number of the psychologist_hospital after creation does not equal the constructor argument.")
        self.assertEqual(psychologist_hospital.crp_psychologist_crp, '0000000',
                         "The crp_psychologist_crp of the psychologist_hospital after creation does not equal the constructor argument.")
