FROM python:3.12-slim AS python-base

RUN apt-get update && apt-get install -y socat

WORKDIR /app

CMD ["socat", "TCP-LISTEN:8080,fork,reuseaddr", "EXEC:python task.py,stderr"]
EXPOSE 8080

FROM python-base AS task-01-01
COPY ./01/01/task.py .

FROM python-base AS task-01-02
COPY ./01/02/task.py .

FROM python-base AS task-01-03
COPY ./01/03/task.py .

FROM python-base AS task-01-04
COPY ./01/04/task.py .

FROM python-base AS task-01-05
COPY ./01/05/task.py .

FROM python-base AS task-01-06
COPY ./01/06/task.py .

FROM python-base AS task-01-07
COPY ./01/07/task.py .

FROM python-base AS task-02-01
COPY ./02/01/task.py .

FROM python-base AS task-02-02
COPY ./02/02/task.py .

FROM python-base AS task-02-03

RUN pip install flask pycryptodome
COPY ./02/03/task.py app.py

CMD ["python", "app.py"]
