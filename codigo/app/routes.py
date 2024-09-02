# routes.py
from flask import Flask, request, jsonify
from models import db, Aluno, Professor, Disciplina, Matricula
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    data = request.json
    hashed_password = generate_password_hash(data['senha'], method='sha256')
    novo_aluno = Aluno(nome=data['nome'], matricula=data['matricula'], senha=hashed_password)
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno criado com sucesso'}), 201

@app.route('/professores', methods=['POST'])
def criar_professor():
    data = request.json
    hashed_password = generate_password_hash(data['senha'], method='sha256')
    novo_professor = Professor(nome=data['nome'], senha=hashed_password)
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({'message': 'Professor criado com sucesso'}), 201

@app.route('/disciplinas', methods=['POST'])
def criar_disciplina():
    data = request.json
    professor = Professor.query.get(data['professor_id'])
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404

    nova_disciplina = Disciplina(nome=data['nome'], codigo=data['codigo'], creditos=data['creditos'], professor=professor)
    db.session.add(nova_disciplina)
    db.session.commit()
    return jsonify({'message': 'Disciplina criada com sucesso'}), 201

@app.route('/matriculas', methods=['POST'])
def realizar_matricula():
    data = request.json
    aluno = Aluno.query.get(data['aluno_id'])
    disciplina = Disciplina.query.get(data['disciplina_id'])
    
    if not aluno or not disciplina:
        return jsonify({'message': 'Aluno ou Disciplina não encontrados'}), 404
    
    if len(disciplina.matriculas) >= 60:
        return jsonify({'message': 'Disciplina cheia'}), 400

    nova_matricula = Matricula(aluno=aluno, disciplina=disciplina)
    db.session.add(nova_matricula)
    db.session.commit()
    return jsonify({'message': 'Matrícula realizada com sucesso'}), 201

@app.route('/disciplinas_ativas', methods=['GET'])
def verificar_disciplinas_ativas():
    disciplinas_ativas = []
    for disciplina in Disciplina.query.all():
        if len(disciplina.matriculas) >= 3:
            disciplinas_ativas.append({'nome': disciplina.nome, 'codigo': disciplina.codigo, 'numero_alunos': len(disciplina.matriculas)})

    return jsonify({'disciplinas_ativas': disciplinas_ativas})

@app.route('/login_aluno', methods=['POST'])
def login_aluno():
    data = request.json
    aluno = Aluno.query.filter_by(matricula=data['matricula']).first()
    if aluno and check_password_hash(aluno.senha, data['senha']):
        return jsonify({'message': f'Bem-vindo, {aluno.nome}!'})
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401

@app.route('/login_professor', methods=['POST'])
def login_professor():
    data = request.json
    professor = Professor.query.filter_by(nome=data['nome']).first()
    if professor and check_password_hash(professor.senha, data['senha']):
        return jsonify({'message': f'Bem-vindo, {professor.nome}!'})
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
