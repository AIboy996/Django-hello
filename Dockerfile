FROM python:3.10-alpine3.17
ENV PYTHONUNBUFFERED 1
WORKDIR /helloworld
RUN python3 -m pip install django pymysql
COPY . .