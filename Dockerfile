FROM python:2.7
LABEL maintainer "Tim Cinel <email@timcinel.com>"

WORKDIR /opt

RUN apt-get update && apt-get install -y jq  && rm -rf /var/lib/apt/lists/*

ADD requirements.txt ./
RUN pip install -r requirements.txt 

ADD auswoo.py requirements.txt process.sh  ./


ENTRYPOINT [ "/bin/bash", "/opt/process.sh" ]
