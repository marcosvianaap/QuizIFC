# app/models.py
from . import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    turno = db.Column(db.String(50), nullable=False)
    nivel = db.Column(db.String(50), nullable=False)
    localidade = db.Column(db.String(100), nullable=False)

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
