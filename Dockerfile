FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
WORKDIR /code/AgroConnect
