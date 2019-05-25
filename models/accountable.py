from db import db


class AccountableModel(db.Model):
    __tablename__ = 'ACCOUNTABLE'

    registry_number_acc = db.Column('registry_number', db.String(11), primary_key=True)
    kinship_degree = db.Column('kinship_degree', db.String(15))

    accountable_person_id = db.Column('fk_person', db.Integer, db.ForeignKey('PERSON.id_person'), unique=True)
    patients = db.relationship('PatientModel', backref='ACCOUNTABLE', uselist=False,
                                   cascade='all, delete-orphan')

    def __init__(self, registry_number_acc, kinship_degree, accountable_person_id):
        self.registry_number_acc = registry_number_acc
        self.kinship_degree = kinship_degree
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