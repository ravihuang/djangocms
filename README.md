# djangocms-postgres-docker
Build a docker environment with Django 2, Django CMS 3.7, and Postgres 4 running on python 3.7

## How to use this docker images
Once you clone this repositorie yo can see the following file structure:

djangocms-postgres-docker\
&nbsp;&nbsp;|-- Dockerfile\
&nbsp;&nbsp;|-- docker-compose.yml\
&nbsp;&nbsp;|-- requirements.txt\

Perform this command to create your Django project (you can change the project name "djangoexample")

```
sudo docker-compose run web django-admin startproject djangoexample .
```
