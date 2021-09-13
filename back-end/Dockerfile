FROM alpine:latest

# 파이썬 버퍼 설정
ENV PYTHONUNBUFFERED 1

RUN mkdir /django
WORKDIR /django

# Copying requirement
COPY ./Netflix_clone    .

RUN apk add --no-cache --virtual .build-deps \
        ca-certificates gcc postgresql-dev linux-headers musl-dev \
        libffi-dev  jpeg-dev  zlib-dev \
        ** pip install -r requirements.txt \
