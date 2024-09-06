from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __abstract__ = True  # Essa classe não será uma tabela própria no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

class Aluno(User):
    __tablename__ = 'alunos'
    cursos_opcoes = [
        'Ciência da Computação',
        'Engenharia de Software',
        'Engenharia da Computação',
        'Matemática Computacional',
        'Sistemas de Informação'
    ]
    curso = db.Column(db.String(100), nullable=False)
    matricula_trancada = db.Column(db.Boolean, default=False)  # Trancamento de matrícula
    matriculas = db.relationship('Matricula', backref='aluno', lazy=True)


class Professor(User):
    __tablename__ = 'professores'
    disciplinas = db.relationship('Disciplina', backref='professor', lazy=True)

class Secretaria(User):
    __tablename__ = 'secretaria'

class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    matriculas = db.relationship('Matricula', backref='disciplina', lazy=True)

class Matricula(db.Model):
    __tablename__ = 'matriculas'
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)
    nota = db.Column(db.Float, nullable=True)

class SistemaCobrancas(db.Model):
    __tablename__ = 'sistema_cobrancas'
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # ex: 'pendente', 'pago'
