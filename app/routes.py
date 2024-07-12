# app/routes.py
from flask import Flask, request, jsonify
from .models import Curso, Caracteristica
from . import db

app = Flask(__name__)

@app.route('/quiz', methods=['POST'])
def quiz():
    data = request.json
    turno = data.get('turno')
    nivel = data.get('nivel')
    localidade = data.get('localidade')

    query = Curso.query
    if turno:
        query = query.filter_by(turno=turno)
    if nivel:
        query = query.filter_by(nivel=nivel)
    if localidade:
        query = query.filter_by(localidade=localidade)

    cursos = query.all()
    cursos_data = [{'id': curso.id, 'nome': curso.nome} for curso in cursos]

    return jsonify(cursos_data)
