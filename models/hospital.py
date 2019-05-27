from db import db


class HospitalModel(db.Model):
    __tablename__ = 'HOSPITAL'

    registry_number = db.Column('registry_number', db.String(14), primary_key=True)
    social_reason = db.Column('social_reason', db.String(100), nullable=False)

    hospital_person_id = db.Column('fk_person', db.Integer, db.ForeignKey('PERSON.id_person'), unique=True,
                                   nullable=False)
    hospital_psychologists = db.relationship('PsychologistHospitalModel', backref='HOSPITAL', lazy='dynamic',
                                             cascade='all, delete-orphan')

    def __init__(self, registry_number, social_reason, hospital_person_id):
        self.registry_number = registry_number
        self.social_reason = social_reason
        self.hospital_person_id = hospital_person_id

    def json(self):
        return {'registry_number': self.registry_number, 'social_reason': self.social_reason}

    @classmethod
    def find_by_registry_number(cls, registry_number):
        return cls.query.filter_by(registry_number=registry_number).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
