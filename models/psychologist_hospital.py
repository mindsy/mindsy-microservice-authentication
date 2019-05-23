from db import db


class PsychologistHospitalModel(db.Model):
    __tablename__ = 'psychologist_hospital'

    id_psycho_hosp = db.Column(db.Integer, primary_key=True)
    crp_psychologist_crp = db.Column(db.String, db.ForeignKey('psychologist.crp'))
    hospital_registry_number = db.Column(db.String, db.ForeignKey('hospital.registry_number'))

    pat_pyscho_hosps = db.relationship('Pat_Psycho_HospModel', backref= 'pat_psycho_hosp', lazy='dynamic',
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