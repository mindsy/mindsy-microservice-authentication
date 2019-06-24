from static.imports import *
from tests.base_test import BaseTest
from datetime import datetime


class PersonTest(BaseTest):
    def test_crud_telephone(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            person.save_to_db()
            telephone = TelephoneModel('000000000', 'comercial', 1)

            self.assertIsNone(TelephoneModel.find_by_number('000000000'), "Found a telephone with number "
                                                                          "'000000000' before save_to_db")

            telephone.save_to_db()

            self.assertIsNotNone(TelephoneModel.find_by_number('000000000'),
                                 "Did not find an telephone with number '000000000' after save_to_db")

            telephone.delete_from_db()

            self.assertIsNone(TelephoneModel.find_by_number('000000000'), "Found a telephone with "
                                                                          "number '000000000' after delete_from_db")

    def test_store_relationship_telephone(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            telephone = TelephoneModel('000000000', 'comercial', 1)

            person.save_to_db()
            telephone.save_to_db()

            self.assertEqual(person.telephones[0].number, '000000000')

    def test_crud_hospital(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            person.save_to_db()
            hospital = HospitalModel('00000000000', 'TESTE LTDA', 1)

            self.assertIsNone(HospitalModel.find_by_registry_number('00000000000'), "Found a hospital with "
                                                                                    "registry number "
                                                                                    "'00000000000' before save_to_db")

            hospital.save_to_db()

            self.assertIsNotNone(HospitalModel.find_by_registry_number('00000000000'),
                                 "Did not find a hospital with registry number '000000000' after save_to_db")

            hospital.delete_from_db()

            self.assertIsNone(HospitalModel.find_by_registry_number('00000000000'),
                              'Found a telephone with ''number \'000000000\' after delete_from_db')

    def test_store_relationship_hospital(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            hospital = HospitalModel('00000000000', 'TESTE LTDA', 1)

            person.save_to_db()
            hospital.save_to_db()

            self.assertEqual(person.hospitals.registry_number, '00000000000')

    def test_crud_psychologist(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            person.save_to_db()

            date_text = "22-09-2018"
            date = datetime.strptime(date_text, '%d-%m-%Y').date()

            psychologist = PsychologistModel('0000000', 'test', date, 1)

            self.assertIsNone(PsychologistModel.find_by_crp('0000000'), "Found a psychologist with this crp")
            psychologist.save_to_db()

            self.assertIsNotNone(PsychologistModel.find_by_crp('0000000'),
                                 "Did not find a psychologist with crp '0000000' after save_to_db")

            psychologist.delete_from_db()

            self.assertIsNone(PsychologistModel.find_by_crp('0000000'), "Found a psychologist with crp ")

    def test_store_relationship_psychologist(self):
        with self.app_context():
            date_text = "22-09-2018"
            date = datetime.strptime(date_text, '%d-%m-%Y').date()

            person = PersonModel('test', 'test@test.com')
            psychologist = PsychologistModel('0000000', 'test', date, 1)

            person.save_to_db()
            psychologist.save_to_db()

            self.assertEqual(person.psychologists.crp, '0000000')

    def test_crud_accountables(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            person.save_to_db()

            accountable = AccountableModel('00000000000', 'test', 1)

            self.assertIsNone(AccountableModel.find_by_registry_number_acc('00000000000'), "Found a accountable with "
                                                                                           "this registry number")
            accountable.save_to_db()

            self.assertIsNotNone(AccountableModel.find_by_registry_number_acc('00000000000'),
                                 "Did not find a accountable with registry number '00000000000' after save_to_db")

            accountable.delete_from_db()

            self.assertIsNone(AccountableModel.find_by_registry_number_acc('00000000000'), "Found a accountable with "
                                                                                           "this registry number ")

    def test_store_relationship_accountables(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            accountable = AccountableModel('00000000000', 'test', 1)

            person.save_to_db()
            accountable.save_to_db()

            self.assertEqual(person.accountables.registry_number_acc, '00000000000')

    def test_crud_patient(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            person.save_to_db()

            accountable = AccountableModel('00000000000', 'test', 1)
            accountable.save_to_db()

            date_text = "22-09-2018"
            date = datetime.strptime(date_text, '%d-%m-%Y').date()

            patient = PatientModel('test', 'test', 'canhoto', '00000000000', date, 1, '00000000000', 'andamento')

            self.assertIsNone(PatientModel.find_by_registry_number_pat('00000000000'), "Found a patient with "
                                                                                       "this registry_number")
            patient.save_to_db()

            self.assertIsNotNone(PatientModel.find_by_registry_number_pat('00000000000'),
                                 "Did not find a accountable with registry number '00000000000' after save_to_db")

            patient.delete_from_db()

            self.assertIsNone(PatientModel.find_by_registry_number_pat('00000000000'), "Found a accountable with "
                                                                                           "this registry number ")

    def test_store_relationship_patient(self):
        with self.app_context():
            person = PersonModel('test', 'test@test.com')
            accountable = AccountableModel('00000000000', 'test', 1)
            date_text = "22-09-2018"
            date = datetime.strptime(date_text, '%d-%m-%Y').date()

            patient = PatientModel('test', 'test', 'canhoto', '00000000000', date, 1, '00000000000', 'andamento')

            person.save_to_db()
            accountable.save_to_db()
            patient.save_to_db()

            self.assertEqual(person.patients.registry_number_pat, '00000000000')
