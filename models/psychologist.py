from db import db


class PsychologistModel(db.Model):
    __tablename__ = 'PSYCHOLOGIST'

    crp = db.Column('crp', db.String(7), primary_key=True)
    password = db.Column('password', db.String(255), nullable=False)
    date_of_birth = db.Column('dt_birth', db.DateTime, nullable=False)
    token = db.Column('token', db.String(255))

    person_psy_id = db.Column('fk_person', db.Integer, db.ForeignKey('PERSON.id_person'), unique=True, nullable=False)
    hospital_psychologists = db.relationship('PsychologistHospitalModel', backref='PSYCHOLOGIST', lazy='dynamic',
                                             cascade='all, delete-orphan')

    def __init__(self, crp, password, date_of_birth, person_psy_id):
        self.crp = crp
        self.password = password
        self.person_psy_id = person_psy_id
        self.date_of_birth = date_of_birth

    def json(self):
        return {'crp': self.crp, 'date_of_birth': self.date_of_birth.strftime("%d-%m-%Y"), 'password': self.password}

    @classmethod
    def find_by_crp(cls, crp):
        return cls.query.filter_by(crp=crp).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
