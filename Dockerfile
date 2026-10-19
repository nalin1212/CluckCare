FROM python:3.10.20-slim-bookworm

RUN pip install awscli
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]