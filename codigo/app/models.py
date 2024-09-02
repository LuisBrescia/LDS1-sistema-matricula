from app import db
from flask_login import UserMixin

class Aluno(UserMixin, db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)
    matriculas = db.relationship('Matricula', backref='aluno', lazy=True)

class Professor(UserMixin, db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)
    disciplinas = db.relationship('Disciplina', backref='professor', lazy=True)

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

class Secretaria(UserMixin, db.Model):
    __tablename__ = 'secretaria'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

class SistemaCobrancas(db.Model):
    __tablename__ = 'sistema_cobrancas'
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # ex: 'pendente', 'pago'
