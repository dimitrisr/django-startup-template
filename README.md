django-startup-template
=======================

A Django 1.4 template to kickstart a new web app.

Features
========
Out of the box this project template provides the following packages and 
functionality:

1. Local and Production settings files.
2. django-storage: Static file storage on Amazon S3.
3. django-compress: Pre-process and Compress CSS & JavaScript.
4. django-debug-toolbar: Awesome tool to debug your django site locally.
5. south: Painless database schema migrations.


Install
=======
Create a new folder on your system and switch to that folder:

```
mkdir awesome_project; cd awesome_project
```

---

Create and initialize a new virtual environment:

```
mkvirtualenv awesome_project
source /usr/local/bin/virtualenvwrapper.sh
workon awesome_project
```

---

Download and install the latest stable version of Django (1.4):

```
pip install django
```

This may take a few minutes.

---

Create a new Django project using this repo as a project template:

```
django-admin.py startproject --template=https://github.com/rudasn/django-startup-template/zipball/master app
```

This command will create a new folder named *app* in which your Django 
project will live.

---

Switch to your project's folder to begin setup:

```
cd app
```

---

Install dependencies:

```
pip install -r requirements/development.txt
```
This will install Django 1.4 and all other packages that you will be using.
It may take some time.


Set-up
======
1. Update settings files to suit your needs.
   Make sure you update the following:
   * AWS credentials (under settings/production.py)
   * Database connections (under settings/production.py)

2. Set-up version control using git.
   This will make deployments much easier.
   * local git repo
   * remote git repo (code hosting)
   * remote git repo (server)


Workflow
========
0. Initialize the virtual environment
```
source /usr/local/bin/virtualenvwrapper.sh; workon default
```

1. Making changes to the database (Models)
```
python manage.py migrate
```

2. Making changes to static files (under /assets)
   ...

3. Installing dependencies
**On your machine**
```
pip install -r requirements/development.txt
```

**On the remote server**
```
pip install -r requirements.txt
```
    
4. Updating dependencies
**On your machine**
```
pip install -U -r requirements/development.txt
```

**On the remote server**
```
pip install -U -r requirements.txt
```

Deployment
==========
When you are done writing code on your machine it's time to push the code on
a server for the world to enjoy:

**On your local machine:**
1. Commit your changes

2. Push your changes to your production server git repo.

3. Push your changes to your git hosting repo.


**On the server:**
Once you have pushed your code to the server (using ```git push```) you need
to re-generate your static files.

1. Compress JS & CSS (django-compress):
```
python manage.py compress
```

2. Copy files from /assets/ to /static/ and push them to Amazon S3 (django-storage):
```
python manage.py collectstatic --noinput
```

3. If you have made changes to your database you need to run migrations (south)
```
python manage.py migrate
```


Deploy your Django app on Webfaction 
=====================================


