FROM alpine:3.7
MAINTAINER Emmanuelle Muckensturm "emuck@protonmail.com"

WORKDIR /api

RUN apk update \
    && apk add py3-flask py3-requests py3-pytest

CMD ["python3", "api.py"]
