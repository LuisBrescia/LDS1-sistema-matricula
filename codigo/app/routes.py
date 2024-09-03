from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.models import Aluno, Professor, Disciplina, Matricula, Secretaria, SistemaCobrancas, User
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__)

@bp.route('/test')
def test():
    return "A rota de teste está funcionando!"

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = Aluno.query.filter_by(email=email).first() or Professor.query.filter_by(email=email).first() or Secretaria.query.filter_by(email=email).first()
        if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login inválido. Verifique suas credenciais e tente novamente.', 'danger')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/aluno/historico')
@login_required
def historico_aluno():
    if isinstance(current_user, Aluno):
        matriculas = Matricula.query.filter_by(aluno_id=current_user.id).all()
        return render_template('historico.html', matriculas=matriculas)
    return redirect(url_for('main.index'))
    

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        tipo = request.form.get('tipo')  # 'aluno', 'professor'

        senha_hash = generate_password_hash(senha, method='sha256')

        if tipo == 'aluno':
            novo_usuario = Aluno(nome=nome, email=email, senha=senha_hash)
        elif tipo == 'professor':
            novo_usuario = Professor(nome=nome, email=email, senha=senha_hash)
        else:
            flash('Tipo de usuário inválido.', 'danger')
            return redirect(url_for('main.register'))

        db.session.add(novo_usuario)
        db.session.commit()
        flash('Registro realizado com sucesso! Agora você pode fazer login.', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')


@bp.route('/aluno/matricular', methods=['GET', 'POST'])
@login_required
def matricular_disciplinas():
    if isinstance(current_user, Aluno):
        if request.method == 'POST':
            disciplinas_selecionadas = request.form.getlist('disciplinas')
            for disciplina_id in disciplinas_selecionadas:
                nova_matricula = Matricula(aluno_id=current_user.id, disciplina_id=disciplina_id)
                db.session.add(nova_matricula)
            db.session.commit()
            flash('Matrículas realizadas com sucesso!', 'success')
            return redirect(url_for('main.historico_aluno'))
        disciplinas = Disciplina.query.all()
        return render_template('matricular.html', disciplinas=disciplinas)
    return redirect(url_for('main.index'))

@bp.route('/aluno/cancelar_matricula/<int:matricula_id>')
@login_required
def cancelar_matricula(matricula_id):
    if isinstance(current_user, Aluno):
        matricula = Matricula.query.get_or_404(matricula_id)
        if matricula.aluno_id == current_user.id:
            db.session.delete(matricula)
            db.session.commit()
            flash('Matrícula cancelada com sucesso!', 'success')
        return redirect(url_for('main.historico_aluno'))
    return redirect(url_for('main.index'))

@bp.route('/professor/turmas')
@login_required
def turmas_professor():
    if isinstance(current_user, Professor):
        disciplinas = Disciplina.query.filter_by(professor_id=current_user.id).all()
        return render_template('turmas.html', disciplinas=disciplinas)
    return redirect(url_for('main.index'))

@bp.route('/professor/atualizar_notas/<int:disciplina_id>', methods=['GET', 'POST'])
@login_required
def atualizar_notas(disciplina_id):
    if isinstance(current_user, Professor):
        disciplina = Disciplina.query.get_or_404(disciplina_id)
        if request.method == 'POST':
            notas = request.form.getlist('nota')
            matriculas_ids = request.form.getlist('matricula_id')
            for matricula_id, nota in zip(matriculas_ids, notas):
                matricula = Matricula.query.get_or_404(matricula_id)
                matricula.nota = float(nota)
            db.session.commit()
            flash('Notas atualizadas com sucesso!', 'success')
            return redirect(url_for('main.turmas_professor'))
        matriculas = Matricula.query.filter_by(disciplina_id=disciplina_id).all()
        return render_template('atualizar_notas.html', disciplina=disciplina, matriculas=matriculas)
    return redirect(url_for('main.index'))

@bp.route('/secretaria/curriculo')
@login_required
def gerar_curriculo():
    if isinstance(current_user, Secretaria):
        disciplinas = Disciplina.query.all()
        return render_template('curriculo.html', disciplinas=disciplinas)
    return redirect(url_for('main.index'))

@bp.route('/secretaria/gerenciar_disciplinas', methods=['GET', 'POST'])
@login_required
def gerenciar_disciplinas():
    if isinstance(current_user, Secretaria):
        if request.method == 'POST':
            nome = request.form.get('nome')
            horario = request.form.get('horario')
            professor_id = request.form.get('professor_id')
            nova_disciplina = Disciplina(nome=nome, horario=horario, professor_id=professor_id)
            db.session.add(nova_disciplina)
            db.session.commit()
            flash('Disciplina criada com sucesso!', 'success')
        disciplinas = Disciplina.query.all()
        professores = Professor.query.all()
        return render_template('gerenciar_disciplinas.html', disciplinas=disciplinas, professores=professores)
    return redirect(url_for('main.index'))

@bp.route('/secretaria/gerenciar_professores', methods=['GET', 'POST'])
@login_required
def gerenciar_professores():
    if isinstance(current_user, Secretaria):
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = generate_password_hash(request.form.get('senha'), method='sha256')
            novo_professor = Professor(nome=nome, email=email, senha=senha)
            db.session.add(novo_professor)
            db.session.commit()
            flash('Professor cadastrado com sucesso!', 'success')
        professores = Professor.query.all()
        return render_template('gerenciar_professores.html', professores=professores)
    return redirect(url_for('main.index'))

@bp.route('/secretaria/gerenciar_alunos', methods=['GET', 'POST'])
@login_required
def gerenciar_alunos():
    if isinstance(current_user, Secretaria):
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = generate_password_hash(request.form.get('senha'), method='sha256')
            novo_aluno = Aluno(nome=nome, email=email, senha=senha)
            db.session.add(novo_aluno)
            db.session.commit()
            flash('Aluno cadastrado com sucesso!', 'success')
        alunos = Aluno.query.all()
        return render_template('gerenciar_alunos.html', alunos=alunos)
    return redirect(url_for('main.index'))
