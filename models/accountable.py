from db import db


class AccountableModel(db.Model):
    __tablename__ = 'accountable'

    registry_number_acc = db.Column(db.String(11), primary_key=True, autoincrement=False)
    kinship_degree = db.Column(db.String(20))

    accountable_patient_id_patient = db.Column(db.Integer, db.ForeignKey('patient.id_patient'), unique=True)
    accountable_person_id = db.Column(db.Integer, db.ForeignKey('person.id'), unique=True)

    def __init__(self, registry_number_acc, kinship_degree, accountable_patient_id_patient, accountable_person_id):
        self.registry_number_acc = registry_number_acc 
        self.kinship_degree = kinship_degree
        self.accountable_patient_id_patient = accountable_patient_id_patient
        self.accountable_person_id = accountable_person_id

    def json(self):
        return {
                    'registry_number': self.registry_number_acc, 'kinship_degree': self.kinship_degree
                }
    
    @classmethod
    def find_by_registry_number_acc(cls, registry_number_acc):
        return cls.query.filter_by(registry_number_acc=registry_number_acc).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()