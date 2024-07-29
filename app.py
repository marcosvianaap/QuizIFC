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

@app.route('/situacao')
def tela_dois():
    # Consulta ao banco de dados para buscar os dados que deseja exibir na tela dois
    cursos = IFC.query.all()
    
    # Renderiza o template da tela dois com os dados dos cursos
    return render_template('tela2.html', cursos=cursos)

@app.route('/regiao', methods=['GET', 'POST'])
def tela_tres():
    return render_template('tela3.html')

@app.route('/area', methods=['GET', 'POST'])
def tela_quatro():
    return render_template('tela4.html')

@app.route('/ac', methods=['GET', 'POST'])
def resultado():
    return render_template('tela5.html')

@app.route('/resultado', methods=['GET', 'POST'])
def tela_cinco():
    return render_template('tela6.html')

if __name__ == '__main__':
    app.run(debug=True)

