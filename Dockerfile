FROM python:3.9-slim-buster
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

CMD ["echo", "Nenhum script especificado. Use: docker run <imagem> python <nome_do_script>.py"]

# Comandos para rodar:

# Para buildar a imagem:    
# docker build -t atividade-ia-python .

# Para rodar os scripts Python:
# docker run -v $(pwd):/app atividade-ia-python python questaoX.py

# Ex:
# docker run -v $(pwd):/app atividade-ia-python python questao1.py
# docker run -v $(pwd):/app atividade-ia-python python questao2.py
# docker run -v $(pwd):/app atividade-ia-python python questao3.py
# ...