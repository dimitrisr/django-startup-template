Set-up {{ project_name }}
-------------------------
**Move the local settings file**

```
mv {{ project_name }}/is_local.py {{ project_name }}/settings/local.py
```

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
source /usr/local/bin/virtualenvwrapper.sh; workon {{ project_name }}
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

**Make sure we work with python-2.7**

```
echo "alias python=python2.7" >> ~/.bash_profile
echo "alias pip=pip-2.7" >> ~/.bash_profile
echo "alias easy_install=easy_install-2.7" >> ~/.bash_profile
mkdir ~/lib/python2.7
```

**Reload bash_profile**

```
source ~/.bash_profile
```

**Install Pip**

```
easy_install pip
```

**Install virtualenv & virtualenvwrapper**

```
pip install virtualenv
pip install --install-option="--user" virtualenvwrapper
```

**Set Environment Variables**

```
echo "PYTHONPATH=$HOME/lib/python2.7" >> ~/.bash_profile
echo "export PYTHONPATH" >> ~/.bash_profile
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7" >> ~/.bash_profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bash_profile
echo "export PROJECT_HOME=$HOME/webapps" >> ~/.bash_profile
echo "export PIP_VIRTUALENV_BASE=$WORKON_HOME" >> ~/.bash_profile
echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.bash_profile
echo "if [ -f $HOME/bin/virtualenvwrapper.sh ]; then" >> ~/.bash_profile
echo "    source $HOME/bin/virtualenvwrapper.sh" >> ~/.bash_profile
echo "fi"
```

**Set-up git**

Create a Git application on Webfaction...

Then

```
git init --bare ~/webapps/git/repos/{{ project_name }}.git
touch ~/webapps/git/{{ project_name }}.git/hooks/post-receive
echo "#!/bin/sh" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "echo 'Executing post-receive'" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "APP_DIR=$HOME/webapps/{{ project_name }}" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "GIT_WORK_TREE=$APP_DIR/app git checkout -f" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "GIT_WORK_TREE=$APP_DIR/app git reset --hard" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "rm $APP_DIR/app/app/settings/development.py" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "source $HOME/bin/virtualenvwrapper.sh" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "workon {{ project_name }}" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "python $APP_DIR/app/manage.py compress" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "python $APP_DIR/app/manage.py collectstatic  --noinput" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
echo "deactivate" >> ~/webapps/git/{{ project_name }}/hooks/post-receive
chmod +x ~/webapps/git/{{ project_name }}/hooks/post-receive
mkdir ~/webapps/{{ project_name }}/app
```

**Create a new virtual env on the server**

On the server:

```
mkvirtualenv {{ project_name }}
workon {{ project_name }}
```

**Install requirements**

```
cd $HOME/webapps/{{ project_name }}/app
pip install -r requirements.txt
```

**Create and set-up the Database**

On Webfaction ..

On your settings/productions.py file ...

**Specify AWS Credentials and S3 bucket name**

On your settings/productions.py file ...

**Edit the server config**

Update the ```apache2/conf/httpd.ini``` file..


**Push your local code to the server**

On your machine in your project's dictory add the remote repo:

```
git remote add production ssh://rudasn@rudasn.webfactional.com/~/webapps/git/repos/{{ project_name }}
```

And the push your code

```
git push production master
```

**Initialize the database**

Back on the server

```
python manage.py syncdb
python manage.py migrate
```


**Finally, restart the server**

```
$HOME/webapps/{{ project_name }}/apache2/bin/restart
```

**YAY!**

If all went well, going to ```http://USENAME.webfactional.com``` should display ..


