from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

# Configurações do banco de dados
DATABASE_URL = 'sqlite:///C:/Users/estagiario.cgi/Documents/GitHub/QuizIFC/IFC.db'

app = Flask(__name__)

# Configuração do SQLAlchemy
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Curso(Base):
    __tablename__ = 'IFC'  # Certifique-se de que o nome da tabela está correto
    Curso = Column(String, primary_key=True)
    Turno = Column(String)

@app.route('/cursos_ead')
def cursos_ead():
    session = Session()
    cursos = session.query(Curso).filter(Curso.Turno == 'EAD').all()
    session.close()
    return render_template('cursos.html', cursos=cursos)

if __name__ == '__main__':
    app.run(debug=True)
