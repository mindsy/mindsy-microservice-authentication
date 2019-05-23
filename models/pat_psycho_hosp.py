from db import db


class Pat_Psycho_HospModel(db.Model):
    __tablename__ = 'pat_psycho_hosp'

    id_pat_psycho_hosp = db.Column(db.Integer, primary_key=True)

    pat_psycho_hosp_id_psycho_hosp = db.Column(db.Integer, db.ForeignKey('psychologist_hospital.id_psycho_hosp'))
    patient_hosp_psy_id_patient = db.Column(db.Integer, db.ForeignKey('patient.id_patient'))

    def __init__(self, pat_psycho_hosp_id_psycho_hosp, patient_hosp_psy_id_patient):
        self.pat_psycho_hosp_id_psycho_hosp = pat_psycho_hosp_id_psycho_hosp
        self.patient_hosp_psy_id_patient = patient_hosp_psy_id_patient

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()