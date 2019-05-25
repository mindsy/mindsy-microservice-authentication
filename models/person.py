from db import db


class PersonModel(db.Model):
    __tablename__ = 'PERSON'

    id = db.Column('id_person', db.Integer, primary_key=True)
    name = db.Column('name', db.String, nullable=False)
    email = db.Column('email', db.String, nullable=False)

    telephones = db.relationship('TelephoneModel', backref='PERSON', lazy='dynamic', cascade='all, delete-orphan')
    hospitals = db.relationship('HospitalModel', backref='PERSON', uselist=False)
    psychologists = db.relationship('PsychologistModel', backref='PERSON', uselist=False, cascade='all, delete-orphan')
    accountables = db.relationship('AccountableModel', backref='PERSON', uselist=False, cascade='all, delete-orphan')
    patients = db.relationship('PatientModel', backref='PERSON', uselist=False, cascade='all, delete-orphan')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def json(self):
        return {'id_person': self.id, 'name': self.name, 'email': self.email, 'telephone': [telephone.json()
                                                                                            for telephone
                                                                                            in self.telephones.all()]}

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()