from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.models import Aluno, Professor, Disciplina, Matricula

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')
    aluno = Aluno.query.filter_by(aluno=login, senha=senha).first()
    professor = Professor.query.filter_by(professor=login, senha=senha).first()
    if aluno:
        login_user(aluno)
        return redirect(url_for('main.historico_aluno'))
    elif professor:
        login_user(professor)
        return redirect(url_for('main.historico_professor'))
    else:
        flash('Usuário ou senha inválidos')
        return redirect(url_for('main.index'))
    pass


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/aluno/historico')
@login_required
def historico_aluno():
    historico = Matricula.query.filter_by(aluno=current_user.aluno).all()
    return render_template('aluno/historico.html', historico=historico)
    pass


