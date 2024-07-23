# run
from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IFC.db'
db = SQLAlchemy(app)

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

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

