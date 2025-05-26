FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
COPY src/ ./src/

# Anahtar ortam değişkenleri
ENV HOME=/home/user
ENV STREAMLIT_HOME=/tmp/streamlit
ENV TRANSFORMERS_CACHE=/tmp/huggingface

# Gerekli dizinleri oluştur
RUN mkdir -p $HOME/.streamlit && mkdir -p $HOME/.cache/huggingface

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

