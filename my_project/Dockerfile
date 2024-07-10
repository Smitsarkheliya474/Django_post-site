FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /my_project/

COPY ./requirments.txt  /requirments.txt/
COPY ./my_project /my_project

RUN pip3 install -r requirments.txt

EXPOSE 8000

RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]