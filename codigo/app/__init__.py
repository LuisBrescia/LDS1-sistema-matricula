from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)

    # Importando os modelos aqui para evitar a importação circular
    from app.models import Aluno, Professor, Secretaria

    @login_manager.user_loader
    def load_user(user_id):
        return Aluno.query.get(int(user_id)) or Professor.query.get(int(user_id)) or Secretaria.query.get(int(user_id))
    
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

        db.create_all()
        
    return app
