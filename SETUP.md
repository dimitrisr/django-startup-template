Set-up {{ project_name }}
-------------------------
**Make sure you are working from the virtual environment**

You should always do this.

```
source /usr/local/bin/virtualenvwrapper.sh
workon env_{{ project_name }}
```

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
source /usr/local/bin/virtualenvwrapper.sh
workon env_{{ project_name }}
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

Create a new Django application on webfaction called  **{{ project_name }}**.

**SSH to your webfaction account**

```
ssh account@ip-address
```

Create a new folder to place your app. It is adviced to keep your code under ```app``` as that folder is referenced in other places as well.

```
mkdir ~/webapps/{{ project_name }}/app
```

The myproject folder created by webfaction will not be used so remove it.

```
rm -r ~/webapps/{{ project_name }}/myproject
```

**Make sure we work with Python 2.7**

Add some aliases on ```.bash_profile``` to reference python2.7 instead of an 
older version and reload the file.

```
echo "alias python=python2.7" >> ~/.bash_profile
echo "alias pip=pip-2.7" >> ~/.bash_profile
echo "alias easy_install=easy_install-2.7" >> ~/.bash_profile
mkdir ~/lib/python2.7
source ~/.bash_profile
```

**Install Pip**

Pip is a python package manager we will be using for installing and updating
python libraries and third-party django apps.

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
echo "PYTHONPATH=~/lib/python2.7" >> ~/.bash_profile
echo "export PYTHONPATH" >> ~/.bash_profile
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7" >> ~/.bash_profile
echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bash_profile
echo "export PROJECT_HOME=~/webapps" >> ~/.bash_profile
echo "export PIP_VIRTUALENV_BASE=$WORKON_HOME" >> ~/.bash_profile
echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.bash_profile
echo "if [ -f ~/bin/virtualenvwrapper.sh ]; then" >> ~/.bash_profile
echo "    source ~/bin/virtualenvwrapper.sh" >> ~/.bash_profile
echo "fi" >> ~/.bash_profile
```

**Set-up git**

Create a Git application on Webfaction called **```git```**.

Then create a new git repo and set up a post-receive hook so that whenever
you push to that repo the code is checked out under ```~/webapps/{{ project_name }}/app``` and is ready to start serving.

```
GIT_REPO=$HOME'/webapps/git/repos/{{ project_name }}.git' 
git init --bare $GIT_REPO
touch $GIT_REPO/hooks/post-receive
echo "#!/bin/sh" >> $GIT_REPO/hooks/post-receive
echo "echo 'Executing post-receive'" >> $GIT_REPO/hooks/post-receive
echo "APP_DIR=$HOME/webapps/{{ project_name }}" >> $GIT_REPO/hooks/post-receive
echo "GIT_WORK_TREE=\$APP_DIR/app git checkout -f" >> $GIT_REPO/hooks/post-receive
echo "GIT_WORK_TREE=\$APP_DIR/app git reset --hard" >> $GIT_REPO/hooks/post-receive
echo "rm \$APP_DIR/app/{{ project_name }}/settings/development.py" >> $GIT_REPO/hooks/post-receive
chmod +x $GIT_REPO/hooks/post-receive
rm -r $HOME/webapps/git/repos/proj.git
```

If you want to auto compress and move the static files to Amazon S3 on every
push (not advised) also do the following:

```
echo "source $HOME/bin/virtualenvwrapper.sh" >> $GIT_REPO/hooks/post-receive
echo "workon env_{{ project_name }}" >> $GIT_REPO/hooks/post-receive
echo "python $APP_DIR/app/manage.py compress" >> $GIT_REPO/hooks/post-receive
echo "python $APP_DIR/app/manage.py collectstatic  --noinput" >> $GIT_REPO/hooks/post-receive
echo "deactivate" >> $GIT_REPO/hooks/post-receive
```

**Create a new virtual env on the server**

On the server:

```
source ~/bin/virtualenvwrapper.sh
mkvirtualenv env_{{ project_name }}
workon env_{{ project_name }}
```

**Create and set-up the Database**

On Webfaction ..

On your settings/production.py file change the ```DATABASE``` entry with the
credentials given by Webfaction. You will need to specify the ```NAME```, 
```USER```, and ```PASSWORD``` entries.

**Specify AWS Credentials and S3 bucket name**

On your settings/productions.py file change the ```AMAZONS3``` entry with your
Amazon Security Credentials. You will need to specify your ```ACCESS_KEY_ID```,
your ```SECRET_ACCESS_KEY```, and the name of the ```BUCKET``` where you want 
to upload your static files.

**Note** that bucket names are global on Amazon's servers so you need to pick
a unique name for that. 

**Change your apache config file to match your project settings**

**Important*:*
* Replace the ```YOUR_WEBFACTION_USERNAME``` portion of the  following line 
with your username on webfaction (the name of your account).

* Replace the ```YOUR_WEBFACTION_APP_PORT``` portion of the following line
with the port of your application. It's the number in brackets next to your app's name on http://my.webfaction.com/applications.

On your machine:

```
sed 's/__/YOUR_WEBFACTION_USERNAME/g' webfaction/apache.conf > webfaction/apache2.conf
sed 's/00000/YOUR_WEBFACTION_APP_PORT/g' webfaction/apache2.conf > webfaction/httpd.conf
rm webfaction/apache.conf
```

**Push your local code to the server**

*On your machine from within your project's directory*

Create a new repo if you haven't done so already:

```
git init
git add {{ project_name }} requirements webfaction .gitignore manage.py README.md SETUP.md requirements.txt wsgi.py
git commit -am 'First commit'
```

Add the remote git repo we created above.

```
git remote add wf ssh://rudasn@rudasn.webfactional.com/~/webapps/git/repos/{{ project_name }}.git
```

Push the code to webfaction's server.

```
git push wf master
```

**Move the apache configuration file to the appropriate folder.**

*On the server*

```
mv ~/webapps/{{ project_name }}/app/webfaction/httpd.conf ~/webapps/{{ project_name }}/apache2/conf
```


**Install requirements**

*On the server*

```
cd ~/webapps/{{ project_name }}/app
pip install -r requirements.txt
```

**Initialize the database**

*On the server*

```
cd ~/webapps/{{ project_name }}/app
```

Create database tables.

```
python manage.py syncdb
```

You will be asked to create an admin user. Go ahead and do that.

Then set-up database migrations.

```
python manage.py migrate
```

Compress JS & CSS:

```
python manage.py compress
```

Copy files from /assets/ to /static/ and push them to Amazon S3:

```
python manage.py collectstatic --noinput
```

**(Re)Start the server**

```
~/webapps/{{ project_name }}/apache2/bin/restart
```

**Set-up a website and domain**

On Webfaction's control panel..

**YAY!**

If all went well, going to ```http://USENAME.webfactional.com``` should display ..


