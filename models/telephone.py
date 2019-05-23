from db import db


class TelephoneModel(db.Model):
    __tablename__ = 'telephone'

    number = db.Column(db.String(11), primary_key=True, autoincrement=False)
    telephone_type = db.Column(db.String(15))

    tel_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, number, telephone_type, tel_person_id):
        self.number = number
        self.telephone_type = telephone_type
        self.tel_person_id = tel_person_id

    def json(self):
        return {'number': self.number, 'telephone_type': self.telephone_type}

    @classmethod
    def find_by_number(cls, number):
        return cls.query.filter_by(number=number).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()