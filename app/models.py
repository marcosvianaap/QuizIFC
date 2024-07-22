#app/models.py

from . import db

class IFC(db.Model):
    __tablename__ = 'IFC'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Curso = db.Column(db.String, nullable=False)
    Turno = db.Column(db.String, nullable=False)
    Campus = db.Column(db.String, nullable=False)
    Modalidade = db.Column(db.String, nullable=False)
    Região = db.Column(db.String, nullable=False)
    Área_Temática = db.Column(db.String, nullable=False)
    Ação_Afirmativa = db.Column(db.String, nullable=False)
    Site = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<IFC {self.Curso}>'
