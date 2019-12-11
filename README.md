# djangocms demo
Build a docker environment with Django 2, Django CMS 3.7, and Postgres 4 running on python 3
import from https://github.com/lexp2001/djangocms-postgres-docker

## Usage
* file tree:
```
djangocms
  |-- docker-compose.yml
  |-- Dockerfile
  |-- requirements.txt
```
* create project:
```
# cd djangocms
# docker-compose run web django-admin startproject mysite .
```
* migrate:
```
docker-compose run web python manage.py migrate
```
## Demo
* djangoexample is a demo project
```
docker-compose up -d
```
login: http://<your-ip>:8194
