import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave_secreta_para_sessao'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sistema_escolar.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.exemplo.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'usuario@exemplo.com'
    MAIL_PASSWORD = 'senha'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
