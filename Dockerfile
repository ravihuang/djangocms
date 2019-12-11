FROM python:3

ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Shanghai

WORKDIR /srv

COPY requirements.txt /srv/

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
