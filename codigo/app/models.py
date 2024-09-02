# models.py
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Aluno {self.nome}>'

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Professor {self.nome}>'

class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    creditos = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    professor = db.relationship('Professor', backref=db.backref('disciplinas', lazy=True))

    def __repr__(self):
        return f'<Disciplina {self.nome}>'

class Matricula(db.Model):
    __tablename__ = 'matriculas'
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)

    aluno = db.relationship('Aluno', backref=db.backref('matriculas', lazy=True))
    disciplina = db.relationship('Disciplina', backref=db.backref('matriculas', lazy=True))

    def __repr__(self):
        return f'<Matricula Aluno: {self.aluno.nome}, Disciplina: {self.disciplina.nome}>'
