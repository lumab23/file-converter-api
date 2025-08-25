# usando a imagem oficial do Python
FROM python:3.11-slim

WORKDIR /app

# adiciona o repositório 'non-free' e instala 'unrar'
RUN echo "deb http://deb.debian.org/debian trixie non-free" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y unrar

# copia requirements e instala dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia todo o código da aplicação
COPY . .

# expõe a porta do FastAPI
EXPOSE 8000

# executa o FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]