from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SENHA") 
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "instance", "IFC.db")}'
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

@app.route('/situacao', methods=['GET', 'POST'])
def tela_dois():
    if request.method == 'POST':
        situacao = request.form.get('situacao')
        opcoes_selecionadas = situacao.split(', ')  # Armazena a lista de opções
        session['situacao'] = opcoes_selecionadas  # Armazena a lista na sessão
        return redirect(url_for('tela_tres'))
    return render_template('tela2.html')


@app.route('/regiao', methods=['GET', 'POST'])
def tela_tres():
    if request.method == 'POST':
        regiao = request.form.get('regiao')   
        session['regiao'] = regiao
        return redirect(url_for('tela_quatro'))
    return render_template('tela3.html')

@app.route('/area', methods=['GET', 'POST'])
def tela_quatro():
    if request.method == 'POST':
        area = request.form.get('area')
        opcoes_selecionadas = area.split(', ')
        session['area'] = opcoes_selecionadas
        return redirect(url_for('tela_cinco'))
    return render_template('tela4.html')

@app.route('/ac', methods=['GET', 'POST'])
def tela_cinco():
    if request.method == 'POST':
        acao_afirmativa = request.form.get('acao_afirmativa')
        session['acao_afirmativa'] = acao_afirmativa
        return redirect(url_for('result'))
    return render_template('tela5.html')

@app.route('/resultado', methods=['GET'])
def result():
    # Recupera todas as respostas armazenadas na sessão
    situacao = session.get('situacao')
    regiao = session.get('regiao')
    area = session.get('area')
    acao_afirmativa = session.get('acao_afirmativa')
    print(situacao,"\n" , regiao,"\n" , area, acao_afirmativa, "\n")

    # Inicia a consulta para cursos recomendados
    cursos_recomendados_query = IFC.query
    
     # Aplica filtro por situação, se especificado
    if situacao:
        cursos_recomendados_query = cursos_recomendados_query.filter(IFC.Modalidade.in_(situacao))

    # Aplica filtro por região, se especificado e não for "Em qualquer região"
    if regiao and regiao != "Em qualquer região":
        cursos_recomendados_query = cursos_recomendados_query.filter_by(Região=regiao)

    # Aplica filtro por área temática, exceto se for "Todas as áreas"
    if area and area != "Todas as áreas":
        cursos_recomendados_query = cursos_recomendados_query.filter(IFC.Área_Temática.in_(area))

      # Aplica filtro por ação afirmativa, se especificado e não for "Não, não pretendo"
    if acao_afirmativa and acao_afirmativa != "Não, não pretendo":
        cursos_recomendados_query = cursos_recomendados_query.filter_by(Ação_Afirmativa=acao_afirmativa)

    # Executa a consulta e obtém os resultados
    cursos_recomendados = cursos_recomendados_query.all()

    return render_template('tela6.html', cursos=cursos_recomendados)


@app.route('/reiniciar')
def reiniciar_quiz():
    session.clear()  # Limpa todos os dados da sessão
    return redirect(url_for('home'))  # Redireciona para a página inicial do quiz

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    
  