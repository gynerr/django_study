FROM python:latest

WORKDIR usr/src/app

SHELL ["/bin/bash", "-c"]
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .






