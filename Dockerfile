FROM python:3.7.2-alpine3.9

RUN mkdir /fruitmachine
COPY ./ /fruitmachine/

WORKDIR /fruitmachine

RUN /fruitmachine/scripts/docker/install

CMD ["python", "/fruitmachine/main.py"]