FROM testerq/python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /srv

COPY requirements.txt /srv/

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
