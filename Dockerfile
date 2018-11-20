FROM ubuntu:16.04

MAINTAINER KIMU

# Installing base software
RUN apt-get update && \
    apt-get install -y git wget nano python3 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install -U spacy && \
    python3 -m spacy download en && \
    python3 -m spacy download de && \
    pip3 install Flask

# Download scripts from repo
RUN git clone https://github.com/kirilzilla/spacy-flask.git spacy-flask

EXPOSE 3000

CMD /spacy-flask/run_spacy_flask.py
