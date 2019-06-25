from db import db
import enum


class TelephoneTypeEnum(enum.Enum):
    comercial = "comercial"
    residencial = "residencial"
    pessoal = "pessoal"


class TelephoneModel(db.Model):
    __tablename__ = 'TELEPHONE'

    number = db.Column('number', db.String(15), primary_key=True)
    telephone_type = db.Column('type', db.Enum(TelephoneTypeEnum), nullable=False)

    tel_person_id = db.Column('id_person', db.Integer, db.ForeignKey('PERSON.id_person'))

    def __init__(self, number, telephone_type, tel_person_id):
        self.number = number
        self.telephone_type = telephone_type
        self.tel_person_id = tel_person_id

    def json(self):
        return {'number': self.number, 'telephone_type': self.telephone_type.value}

    @classmethod
    def find_by_number(cls, number):
        return cls.query.filter_by(number=number).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
