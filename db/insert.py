# Modelo para inserção de novos dados no banco

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco de dados
DATABASE_URL =  'sqlite:///QuizIFC/db/IFC.db' # Caminho do banco

# Criação da engine e sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Definindo a base e o modelo
Base = declarative_base()

class IFC(Base):
    __tablename__ = 'IFC'
    
    Curso = Column(String, primary_key=True)  
    Turno = Column(String)
    Modalidade = Column(String)
    Campus = Column(String)
    Região = Column(String)
    Área_Temática = Column(String)
    Ação_Afirmativa = Column(String)
    Site = Column(String)
    

# Dados a serem inseridos
dados = [
    ('EJA com qualificação em Nutrição e Segurança Alimentar', 'Noturno', 'EJA', 'Abelardo Luz', 'Oeste', 'Multidisciplinar', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'https://abelardoluz.ifc.edu.br/'),
    ('EJA com qualificação em Eletricista Industrial', 'Noturno', 'EJA', 'Blumenau', 'Vale do Itajaí', 'Engenharia e Tecnologias', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'http://blumenau.antigo.ifc.edu.br/ejaept-eletricista-industrial/'),
    ('EJA com qualificação em Agroindústria', 'Noturno', 'EJA', 'Camboriú', 'Vale do Itajaí', 'Ciências Agrárias', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'http://www.camboriu.ifc.edu.br/eja/'),
    ('EJA com qualificação em Agente de Higiene e Segurança do Trabalho', 'Noturno', 'EJA', 'Camboriú', 'Vale do Itajaí', 'Multidisciplinar', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'http://www.camboriu.ifc.edu.br/eja/'),
    ('EJA com qualificação em Operador de Computador', 'Noturno', 'EJA', 'Fraiburgo', 'Oeste', 'Engenharia e Tecnologias', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'http://proeja.fraiburgo.ifc.edu.br/'),
    ('EJA com qualificação em Auxiliar Administrativo', 'Noturno', 'EJA', 'Ibirama', 'Vale do Itajaí', 'Ciências Sociais Aplicadas', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'https://ibirama.ifc.edu.br/'),
    ('EJA com qualificação em Auxiliar Administrativo', 'Noturno', 'EJA', 'São Francisco do Sul', 'Norte', 'Ciências Sociais Aplicadas', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'https://proeja.saofrancisco.ifc.edu.br/'),
    ('EJA com qualificação em Assistente Administrativo', 'Noturno', 'EJA', 'Sombrio', 'Sul', 'Ciências Sociais Aplicadas', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'https://ejaept.sombrio.ifc.edu.br/'),
    ('EJA com qualificação em Assistente Administrativo', 'Noturno', 'EJA', 'Videira', 'Oeste', 'Ciências Sociais Aplicadas', 'Escola pública, Negros (pretos e pardos), Quilombola, Indígena, Baixa Renda', 'https://videira.ifc.edu.br/proeja/'),
]

# Inserindo os dados
for curso in dados:
    novo_curso = IFC(
        Curso=curso[0],
        Turno=curso[1],
        Modalidade=curso[2],
        Campus=curso[3],
        Região=curso[4],
        Área_Temática=curso[5],
        Ação_Afirmativa=curso[6],
        Site=curso[7]
    )
    session.add(novo_curso)

# Comitar as alterações no banco de dados
session.commit()
session.close()

