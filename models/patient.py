from db import db
import enum


class ManualDomainEnum(enum.Enum):
    RIGHT = "destro"
    LEFT = "canhoto"


class StatusEnum(enum.Enum):
    PROGRESS = "andamento"
    DONE = "finalizado"
    WAITING = "aguardando"


class PatientModel(db.Model):
    __tablename__ = 'PATIENT'

    id_patient = db.Column('id_patient', db.Integer, primary_key=True)
    registry_number_pat = db.Column('registry_number', db.String(11), unique=True)
    dt_birth = db.Column('dt_birth', db.DateTime, nullable=False)
    scholarity = db.Column('scholarity', db.String(100), nullable=False)
    observation = db.Column('observation', db.String)
    manual_domain = db.Column('manual_domain', db.Enum(ManualDomainEnum), nullable=False)
    status = db.Column('status', db.Enum(StatusEnum), nullable=False)

    person_pat_id = db.Column('fk_person', db.Integer, db.ForeignKey('PERSON.id_person'), unique=True, nullable=False)
    accountable_patient_id_patient = db.Column('fk_accountable', db.String(11), db.ForeignKey('ACCOUNTABLE.registry_number'), unique=True)

    pat_psycho_hosps = db.relationship('PatPsychoHospModel', backref='PATIENT', cascade='all, delete-orphan')

    def __init__(self, registry_number_pat, dt_birth, scholarity, observation, manual_domain, status, person_pat_id, accountable_patient_id_patient):
        self.scholarity = scholarity
        self.observation = observation
        self.manual_domain = manual_domain
        self.registry_number_pat = registry_number_pat
        self.dt_birth = dt_birth
        self.person_pat_id = person_pat_id
        self.accountable_patient_id_patient = accountable_patient_id_patient
        self.status = status
    
    def json(self):
        return {
                    'id_patient': self.id_patient, 'scholarity': self.scholarity, 'observation': self.observation,
                    'manual_domain': self.manual_domain, 'registry number': self.registry_number_pat, 
                    'date of birth': self.dt_birth.date().isoformat()
                }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id_patient=id).first()
    
    @classmethod
    def find_by_registry_number_pat(cls, registry_number_pat):
        return cls.query.filter_by(registry_number_pat=registry_number_pat).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
