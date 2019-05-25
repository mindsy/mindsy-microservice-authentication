from db import db


class PsychologistHospitalModel(db.Model):
    __tablename__ = 'PSYCHOLOGIST_HOSPITAL'

    id_psycho_hosp = db.Column('id_psycho_hosp', db.Integer, primary_key=True)

    crp_psychologist_crp = db.Column('crp_psychologist', db.String(7), db.ForeignKey('PSYCHOLOGIST.crp'), nullable=False)
    hospital_registry_number = db.Column('id_hospital', db.String(14), db.ForeignKey('HOSPITAL.registry_number'),
                                         nullable=False)

    pat_pyscho_hosps = db.relationship('PatPsychoHospModel', backref='PSYCHOLOGIST_HOSPITAL', lazy='dynamic',
                                       cascade='all, delete-orphan')

    def __init__(self, hospital_registry_number, crp_psychologist_crp):
        self.hospital_registry_number = hospital_registry_number
        self.crp_psychologist_crp = crp_psychologist_crp

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id= cls.id_psycho_hosp).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()