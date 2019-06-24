from static.imports import *
from tests.unit.unit_base_test import UnitBaseTest


class PatPsychoHospTest(UnitBaseTest):
    def test_create_pat_psycho_hosp(self):

        pat_psycho_hosp = PatPsychoHospModel(None, None)

        self.assertEqual(pat_psycho_hosp.pat_psycho_hosp_id_psycho_hosp, None,
                         "The pat_psycho_hosp_id_psycho_hosp of the table after creation does not equal the constructor argument.")
        self.assertEqual(pat_psycho_hosp.patient_hosp_psy_id_patient, None,
                         "The patient_hosp_psy_id_patient of the table after creation does not equal the constructor argument.")

