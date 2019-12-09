# djangocms-postgres-docker
Build a docker environment with Django 2, Django CMS 3.7, and Postgres 4 running on python 3.7

## How to use this docker images
Once you clone this repositorie yo can see the following file structure:\
&nbsp;\
djangocms-postgres-docker\
&nbsp;&nbsp;|-- Dockerfile\
&nbsp;&nbsp;|-- docker-compose.yml\
&nbsp;&nbsp;|-- requirements.txt\
&nbsp;\
Perform this command to create your Django project (you can change the project name "djangoexample") inlude the "point" at the end of the command line:
```
sudo docker-compose run web django-admin startproject djangoexample .
```
If you are in Linux, need to change the owner user of the project name folder and manage.py file:
```
sudo chown -R $USER:$USER djangoexample manage.py
```
In your new project root directory ("djangoexample" in our example) create 1 folder named "templates" and a file named "cms_menu.py", then into the templates directory creat other file named home.html, the final file structure must look like this:\
&nbsp;\
djangocms-postgres-docker\
&nbsp;&nbsp;|-- Dockerfile\
&nbsp;&nbsp;|-- docker-compose.yml\
&nbsp;&nbsp;|-- requirements.txt\
&nbsp;\

