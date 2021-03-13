FROM python:3.7.5

RUN mkdir /fruitmachine
COPY ./ /fruitmachine/

WORKDIR /fruitmachine/

RUN chmod +x /fruitmachine/scripts/docker/install
RUN /fruitmachine/scripts/docker/install

ENV PYTHONPATH "${PYTHONPATH}:/fruitmachine/src/"

CMD ["python", "/fruitmachine/src/main.py"]