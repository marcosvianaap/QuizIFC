from . import db

class Dados_Gerais(db.Model):
    __tablename__ = 'dados_gerais'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instituicao = db.Column(db.String(255), nullable=False)
    campus = db.Column(db.String(255), nullable=False)
    cidade = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    site = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    instagram = db.Column(db.String(255), nullable=False)


class Condicoes_Servicos(db.Model):
    __tablename__ = 'condicoes_servicos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instituicao = db.Column(db.String(255), nullable=False)
    campus = db.Column(db.String(255), nullable=False)
    indice = db.Column(db.String(255), nullable=False)
    opcao = db.Column(db.String(255), nullable=False)


class Cursos_Ensino_Medio_Integrado(db.Model):
    __tablename__ = 'cursos_ensino_medio_integrado'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instituicao = db.Column(db.String(255), nullable=False)
    campus = db.Column(db.String(255), nullable=False)
    curso = db.Column(db.String(255), nullable=False)
    pagina_do_curso = db.Column(db.String(255), nullable=False)
    turno = db.Column(db.String(255), nullable=False)
    duracao = db.Column(db.String(255), nullable=False)
    areas_de_atuacao = db.Column(db.String(255), nullable=False)
    forma_de_selecao = db.Column(db.String(255), nullable=False)
    grade_curricular = db.Column(db.String(255), nullable=False)


class Cursos_Subsequentes(db.Model):
    __tablename__ = 'cursos_subsequentes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instituicao = db.Column(db.String(255), nullable=False)
    campus = db.Column(db.String(255), nullable=False)
    curso = db.Column(db.String(255), nullable=False)
    pagina_do_curso = db.Column(db.String(255), nullable=False)
    turno = db.Column(db.String(255), nullable=False)
    duracao = db.Column(db.String(255), nullable=False)
    areas_de_atuacao = db.Column(db.String(255), nullable=False)
    forma_de_selecao = db.Column(db.String(255), nullable=False)
    grade_curricular = db.Column(db.String(255), nullable=False)


class Cursos_Graduacao(db.Model):
    __tablename__ = 'cursos_graduacao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instituicao = db.Column(db.String(255), nullable=False)
    campus = db.Column(db.String(255), nullable=False)
    curso = db.Column(db.String(255), nullable=False)
    pagina_do_curso = db.Column(db.String(255), nullable=False)
    turno = db.Column(db.String(255), nullable=False)
    duracao = db.Column(db.String(255), nullable=False)
    areas_de_atuacao = db.Column(db.String(255), nullable=False)
    forma_de_selecao = db.Column(db.String(255), nullable=False)
    grade_curricular = db.Column(db.String(255), nullable=False)
