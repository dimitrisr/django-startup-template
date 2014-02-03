django-startup-template
=======================

A Django 1.6 template to kickstart a new web app. 

Features
========
Out of the box this project template provides the following packages and 
functionality:

1. Local and Production settings files.
2. django-storage: Static file storage on Amazon S3.
3. django-compress: Pre-process and Compress CSS & JavaScript.
4. django-debug-toolbar: Awesome tool to debug your django site locally.
5. south: Painless database schema migrations.

Requirements
=============

1. Git
2. Pip
3. virtualenv

Install
=======
**Create a new folder on your system and switch to that folder**

```
mkdir my_django_project
```


```
cd my_django_project
```

**Create and initialize a new virtual environment**

```
source /usr/local/bin/virtualenvwrapper.sh
```

You should probably change ```env_my_django_project``` to something more 
meaningful.

```
mkvirtualenv env_my_django_project
```

**Download and install the latest stable version of Django (1.6)**

```
pip install django
```

This may take a few minutes.

**Create a new Django project** using this repo as a project template and 
switch to the new application folder

```
django-admin.py startproject --template=https://github.com/dimitrisr/django-startup-template/zipball/master --extension=py,md,conf,.gitignore app; cd app
```

This command will create a new folder named **```app```** in which your Django 
project will live.

Now browse to the new project's directory and follow the instructions in **SETUP.md**.

django-admin.py startproject --template=../django-startup-template/ --extension=py,md,conf,.gitignore eheterocycles; cd eheterocycles
