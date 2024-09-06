from app import create_app, db
from app.models import Aluno, Professor, Secretaria
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Criar Secretaria
    secretaria = Secretaria(
        nome='Secretaria Geral',
        email='secretaria@escola.com',
        senha=generate_password_hash('secretaria123', method='pbkdf2:sha256')
    )
    db.session.add(secretaria)
    
    # Criar Professores
    professor1 = Professor(
        nome='João Silva',
        email='joao.silva@escola.com',
        senha=generate_password_hash('professor123', method='pbkdf2:sha256')
    )
    db.session.add(professor1)
    
    # Criar Alunos
    aluno1 = Aluno(
        nome='Maria Oliveira',
        email='maria.oliveira@escola.com',
        senha=generate_password_hash('aluno123', method='pbkdf2:sha256'),
        curso='Ciência da Computação'  # Adicione um valor válido para o curso
    )
    db.session.add(aluno1)
    
    db.session.commit()
    print("Dados iniciais inseridos com sucesso!")
