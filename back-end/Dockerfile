FROM alpine:latest

# 파이썬 버퍼 설정
ENV PYTHONUNBUFFERED 1

RUN mkdir /django
WORKDIR /django

# Copying requirement

RUN apk update && apk add --no-cache --update ca-certificates gcc postgresql-dev \
    linux-headers musl-dev libffi-dev jpeg-dev zlib-dev bash python3-dev  postgresql-dev \
    py3-pip

# python 패키지 업데이트
RUN pip3 install update

# pip를 이용한 Django 설치
RUN pip3 install django


#ENTRYPOINT ["entrypoint.sh"]
