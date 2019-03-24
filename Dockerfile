FROM python:3.6.8-alpine3.9

RUN mkdir /fruitmachine
COPY ./ /fruitmachine/

WORKDIR /fruitmachine

RUN chmod +x /fruitmachine/scripts/docker/install
RUN /fruitmachine/scripts/docker/install

CMD ["python", "/fruitmachine/main.py"]