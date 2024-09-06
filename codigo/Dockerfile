# Use a imagem oficial do Python como base
FROM python:3.12-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o requirements.txt e instalar as dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código do aplicativo
COPY . .

# Expor a porta que o Flask usará
EXPOSE 5000

# Definir a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Comando para iniciar o Flask
CMD ["flask", "run", "--host=0.0.0.0"]