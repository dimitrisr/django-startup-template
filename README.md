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
**Create a new folder on your system and switch to that folder**

```
mkdir MY_AWESOME_PROJECT; cd MY_AWESOME_PROJECT
```

**Create and initialize a new virtual environment**

```
mkvirtualenv ENV_AWESOME_PROJECT
source /usr/local/bin/virtualenvwrapper.sh
workon ENV_AWESOME_PROJECT
```

*Note* this will create a system-wide virtual environment under the name
```ENV_AWESOME_PROJECT```. You will be able to switch to that virtual 
environment from any folder, not just ```MY_AWESOME_PROJECT```. As such, you
may or may not want to change the virtual environment's name to something else.
If all this sounds confusing spend 30 minutes to read on virtual environments.

**Download and install the latest stable version of Django (1.4)**

```
pip install django
```

This may take a few minutes.

**Create a new Django project** using this repo as a project template and 
switch to the new application folder

```
django-admin.py startproject --template=https://github.com/rudasn/django-startup-template/zipball/master app; cd app
```

This command will create a new folder named *app* in which your Django 
project will live.

**Install dependencies**

```
pip install -r requirements/development.txt
```
This will install Django 1.4 and all other packages that you will be using.
It may take some time.


**Test drive**

Create a default sqlite database, perform initial migrations and start the
local development server.

```
python manage.py syncdb
python manage.py migrate
python manage.py runserver
```

If all goes well you should go to http://127.0.0.1:8000/ and see "Hello!".

You can now start playing with your new awesome app or you can continue reading
to see how you can deploy your app on a real server for people to enjoy.

---

Development
===========

'Development' describes the state of things when you are working on your 
application locally on your machine.

Setup
-----

Set-up version control using git.
   This will make deployments much easier.
   * local git repo
   * remote git repo (code hosting)

Workflow
--------

From now on, whenever you wish to work on your awesome project you need to
**initialize the virtual environment** you previously created. Switch to your project folder, if not already there, and:

```
source /usr/local/bin/virtualenvwrapper.sh; workon ENV_NAME
```

Whenever you make changes to your database Models, add new apps or remove 
existing apps, you need to **syncronize the database and perform any necessary
migrations**.

```
python manage.py syncdb
python manage.py migrate
```

When you update the files under the requirements folder or the requirements.txt
file itself you need to **install or update dependencies**.

```pip install -r requirements/development.txt``` to *install*.

```pip install -U -r requirements/development.txt``` to *update*.

---

Production
==========


Setup
-----

Update settings files to suit your needs.
   Make sure you update the following:
   * AWS credentials (under settings/production.py)
   * Database connections (under settings/production.py)

Workflow
--------

---

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
to re-generate your static files and upload them to Amazon S3.

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
python manage.py syncdb
python manage.py migrate
```


Deploy your Django app on Webfaction 
=====================================


