from db import db


class PatPsychoHospModel(db.Model):
    __tablename__ = 'PAT_PSYCHO_HOSP'

    id_pat_psycho_hosp = db.Column('id_pat_psycho_hosp', db.Integer, primary_key=True)

    pat_psycho_hosp_id_psycho_hosp = db.Column('fk_psycho_hosp', db.Integer, db.ForeignKey('PSYCHOLOGIST_HOSPITAL.id_psycho_hosp'), nullable=False)
    patient_hosp_psy_id_patient = db.Column('fk_patient', db.Integer, db.ForeignKey('PATIENT.id_patient'), nullable=False)

    def __init__(self, pat_psycho_hosp_id_psycho_hosp, patient_hosp_psy_id_patient):
        self.pat_psycho_hosp_id_psycho_hosp = pat_psycho_hosp_id_psycho_hosp
        self.patient_hosp_psy_id_patient = patient_hosp_psy_id_patient

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


