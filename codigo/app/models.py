from app import db
from flask_login import UserMixin

class Aluno(UserMixin, db.Model):
    # Definição do modelo do Aluno
    aluno = db.Column(db.String(50), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    matricula = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(50), nullable=False)
    rg = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(50), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    data_matricula = db.Column(db.String(50), nullable=False)
    data_conclusao = db.Column(db.String(50), nullable=False)
    data_cancelamento = db.Column(db.String(50), nullable=False)


class Professor(UserMixin, db.Model):
    professor = db.Column(db.String(50), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(50), nullable=False)
    rg = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(50), nullable=False)
    titulacao = db.Column(db.String(50), nullable=False)
    data_admissao = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    data_demissao = db.Column(db.String(50), nullable=False)


class Disciplina(db.Model):
    disciplina = db.Column(db.String(50), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    carga_horaria = db.Column(db.String(50), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    professor = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)


class Matricula(db.Model):
    matricula = db.Column(db.String(50), primary_key=True)
    aluno = db.Column(db.String(50), nullable=False)
    disciplina = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    data_matricula = db.Column(db.String(50), nullable=False)
    data_cancelamento = db.Column(db.String(50), nullable=False)


class Secretaria(UserMixin, db.Model):
    secretaria = db.Column(db.String(50), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(50), nullable=False)
    rg = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.String(50), nullable=False)
    data_admissao = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    data_demissao = db.Column(db.String(50), nullable=False) 


class SistemaCobrancas(db.Model):
    sistemacobrancas = db.Column(db.String(50), primary_key=True)
    aluno = db.Column(db.String(50), nullable=False)
    disciplina = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.String(50), nullable=False)
    data_vencimento = db.Column(db.String(50), nullable=False)
    situacao = db.Column(db.String(50), nullable=False)
    data_pagamento = db.Column(db.String(50), nullable=False)
    
