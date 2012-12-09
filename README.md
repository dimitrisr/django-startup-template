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
