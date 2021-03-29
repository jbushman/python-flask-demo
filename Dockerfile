FROM python:3.8.2-buster

LABEL python-flask-recipe.version="0.0.1-beta"

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock  --requirements > requirements.txt

# Multi-stage image
FROM python:3.8.2-buster

RUN apt-get update -y \
    && groupadd -r webapp \
    && useradd --no-log-init --create-home --shell /bin/bash -r -g webapp webapp

ENV PATH=/home/webapp/.local/bin:$PATH

USER webapp
WORKDIR /home/webapp

COPY src  .
COPY --from=0 /tmp/requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "app.py" ]
