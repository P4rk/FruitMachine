FROM python:3.7.2-alpine3.9

RUN mkdir /fruitemachine
COPY . /fruitemachine/

CMD ['python', '/fruitmachine/main.py']