{% include stylesheets/styles.css %}

### Requirements
* An account on [Webfaction](http://www.webfaction.com?aid=30409) <small>*Affiliate link*</small>
* [Git](http://git-scm.com/) - version control and easy deployments
* [Pip](https://pypi.python.org/pypi/pip/) - a python package manager
* [virtualenv](https://pypi.python.org/pypi/virtualenv/) - python virtual environments
* [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) - python virtual environments made easier

### Project Settings
Generate personalised instructions by providing some basic details. **No data is being collected nor stored.**

<form>
    <p><input type="text" placeholder="Project Name" title="Project Name" data-bind="project-name"> <small>eg. my_cool_project</small></p>
    <p><input type="text" placeholder="Webfaction Username" title="Webfaction Username" data-bind="webfaction-username"> <small>eg. awesome_dev</small></p>
    <p><input type="text" placeholder="Webfaction Machine IP Address" title="Webfaction Machine IP Address" data-bind="webfaction-ip"> <small>eg. web121.webfaction.com or 75.126.24.79</small></p>
</form>

### Install
<div class="step">
    <p>Create a new folder on your system and switch to that folder.</p>
    <pre class="local">
        <code>mkdir <em class="project-name"></em> &amp;&amp; cd <em class="project-name"></em>\
        </code>
    </pre>
</div>

<div class="step">
    <p>Create and initialize a new virtual environment.</p>
    <pre class="local">
        <code>source /usr/local/bin/virtualenvwrapper.sh</code>
        <code>mkvirtualenv env_<em class="project-name"></em></code>
        <code>workon env_<em class="project-name"></em></code>
    </pre>
</div>

<div class="step">
    <p>Download and install the latest stable version of Django.</p>
    <pre class="local">
        <code>pip install django</code>
    </pre>
</div>

<div class="step">
    <p>Create a new Django project based on this repo in a new <em class="project-name"></em> folder.</p>
    <pre class="local">
        <code>django-admin.py startproject --template=https://github.com/dimitrisr/django-startup-template/zipball/master --extension=py,md,conf,.gitignore <em class="project-name"></em>
        </code>
        <code>cd <em class="project-name"></em></code>
    </pre>
</div>

<div class="step">
    <p>Install dependencies.</p>
    <pre class="local">
        <code>pip install -r requirements/development.txt</code>
    </pre>
</div>

###Services
<h3>Application</h3>
<div class="step">
<p>Create a new Django application on webfaction called <em class="project-name"></em>.</p>
<pre class="remote">
    <p>Go to the <a href="https://my.webfaction.com/new-application" target="webfaction">New Application</a> page.</p>
    <p><strong>Name</strong> should be <em class="project-name"></em>.</p>
    <p><strong>App Category</strong> should be <em>Django</em>.</p>
    <p><strong>App Type</strong> should be <em>Django 1.X.X</em>.</p>
    <p>Click <strong>Save</strong></p>
    <p>Once the application is created look for its <strong>Port</strong> and type it here <input type="text" placeholder="Port" title="Port" data-bind="webfaction-port">.</p>
</pre>
</div>
<h3>Database</h3>
<div class="step">
<p>Create and set-up a PostgreSQL database.</p>
<pre class="remote">
    <p>Go to the <a href="https://my.webfaction.com/new-database" target="webfaction">New Database</a> page.</p>
    <p><strong>Name</strong> can be <input type="text" placeholder="Database Name" class="project-name" data-prefix="db_" title="Database Name" data-bind="db-name">.</p>
    <p><strong>Database type</strong> should be <em>PostgreSQL</em>.</p>
    <p>Create a new <strong>Database Owner</strong>.</p>
    <p><strong>Username</strong> can be <input type="text" placeholder="Database User" class="project-name" data-prefix="db_" title="Database User" data-bind="db-user">.</p>
    <p><strong>Password</strong> can be <input type="text" placeholder="Password" title="Database Password" data-bind="db-password">
        <br><small>(This was randomly generated. <a id="generate-password" href="">Generate another one</a>.)</small></p>
    <p>Click <strong>Save</strong></p>
</pre>
</div>
<h3>Website &amp; Domain</h3>
<div class="step">
<p>Create a website and a domain. It's best to do this now as it takes some time for the domains to kick in. Hopefuly by the time you have finished with the rest of the steps everything should be working.</p>
<pre class="remote">
    <p>Go to the <a href="https://my.webfaction.com/new-website" target="webfaction">New Website</a> page.</p>
    <p><strong>Name</strong> can be <em class="project-name"></em>.</p>
    <p>Create two new <strong>Domains</strong>.<p>
    <p><em class="project-name"></em>.<em class="webfaction-username"></em><em>.webfactional.com</em> and www.<em class="project-name"></em>.<em class="webfaction-username"></em><em>.webfactional.com</em>.</p>
    <p>For <strong>Contents</strong> choose <em>Reuse an existing application</em> and select <em class="project-name"></em> from the list.</p>
    <p>Click <strong>Save</strong>.</p>
</pre>
</div>
<h3>Git</h3>
<p class="note"><strong>Skip</strong> this section if you already have a git application running on your server named <strong><code>git</code></strong>.</p>
<div class="step">
<p>Create a Git application to host and deploy our host.</p>
<pre class="remote">
    <p>Go to the <a href="https://my.webfaction.com/new-application" target="webfaction">New Application</a> page.</p>
    <p><strong>Name</strong> should be <em>git</em>.</p>
    <p><strong>App Category</strong> should be <em>Git</em>.</p>
    <p><strong>App Type</strong> should be <em>Git 1.7.4.1</em>.</p>
    <p>Click <strong>Save</strong></p>
</pre>
</div>
<h3>Amazon Web Services S3</h3>
<div class="step">
<p>Create a new bucket.</p>
<pre class="remote">
    <p>Go to your <a href="https://console.aws.amazon.com/s3/home" target="aws">AWS S3 console</a>.</p>
    <p>Click on <strong>Create Bucket</strong>.</p>
    <p><strong>Bucket Name</strong> can be <input type="text" class="project-name" placeholder="AWS S3 Bucket Name" title="AWS S3 Bucket Name" data-suffix="_aws_static" data-bind="aws-bucket">.</p>
    <p>Once the bucket is created select it from the list and click on <strong>Properties</strong>.</p>
    <p>Create a new <strong>Permissions</strong> entry allowing <em>Everyone</em> to just have <em>View Permissions</em>.</p>
</pre>
<p>Create a new user for this project.</p>
<pre class="remote">
    <p>Go to <a href="https://console.aws.amazon.com/iam/home?#users" target="aws">AWS Identity and Access Management</a> page.</p>
    <p><strong>Create</strong> a new user named <em class="project-name"></em>. Make sure the option to "<em>Generate an access key for each User</em>" is checked.</p>
    <p>Once the user is created click on "<em>Show User Security Credentials</em>" and copy &amp; paste them here.</p>
    <p><input type="text" placeholder="AWS S3 User Key" title="AWS S3 User Key" data-bind="aws-key"></p>
<p><input type="text" placeholder="AWS S3 User Secret" title="AWS S3 User Secret" data-bind="aws-secret"></p>
</pre>
<p>Assign permissions to the user you just created to manage the project's bucket.</p>

<pre class="remote">
    <p>Go back to the <a href="https://console.aws.amazon.com/iam/home?#users" target="aws">AWS Identity and Access Management</a> page.</p>
    <p>Select the <em class="project-name"></em> user.</p>
    <p>Click on <em>Permissions</em> (on the tabs at the bottom of the page).</p>
    <p>Click on <em>Attach User Policy</em> and select <em>Custom Policy</em>.</p>
    <p><strong>Policy Name</strong> can be something like <em>S3FullBucketPermissions<em class="aws-bucket"></em></em></p>
    <p><strong>Policy Document</strong> should be:</p>
<pre><code>{
    "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:*"],
            "Resource": ["arn:aws:s3:::<em class="aws-bucket"></em>", "arn:aws:s3:::<em class="aws-bucket"></em>/*"]
        }]
}</code></pre>
                <p>This grants full access to the <em class="project-name"></em> user <strong>just</strong> on the <em class="aws-bucket"></em> bucket.</p>
            </pre>
        </div>

    <h2>Local Set-up</h2>
        <div class="step">
            <p>Change your apache config file to match your project settings.</p>
<pre class="local">
    <code>sed 's/__/<em class="webfaction-username"></em>/g' webfaction/apache.conf > webfaction/apache2.conf
    sed 's/00000/<em class="webfaction-port"></em>/g' webfaction/apache2.conf > webfaction/httpd.conf
    rm webfaction/apache.conf
    rm webfaction/apache2.conf</code></pre>
        </div>

        <div class="step">
            <p>Move the local settings file to the right place, so that we know when django is running locally or on the server.</p>
<pre class="local">
    <code>mv <em class="project-name"></em>/is_local.py <em class="project-name"></em>/settings/local.py</code></pre>
        </div>
        <h3>Database</h3>
        <div class="step">
            <p>Enter our database credentials in our production settings file. Open the <code>settings/production.py</code> file and change the <code>DATABASE</code> entry with your database credentials to look like this:</p>
<pre class="local" data-file="settings/production.py">
    <code>DATABASE = {
        'NAME': '<em class="db-name"></em>',
        'USER': '<em class="db-user"></em>',
        'PASSWORD': '<em class="db-password"></em>'
    }</code></pre>
        </div>
        <h3>Amazon S3</h3>
        <div class="step">
            <p>Enter our Amazon S3 credentials in our production settings file.
             Open the <code>settings/production.py</code> file and change the <code>AMAZONS3</code> entry to look like this:</p>
<pre class="local" data-file="settings/production.py">
    <code>AMAZONS3 = {
        'ACCESS_KEY_ID': '<em class="aws-key"></em>',
        'SECRET_ACCESS_KEY': '<em class="aws-secret"></em>',
        'BUCKET': '<em class="aws-bucket"></em>'
    }</code></pre>
        </div>
        <h3>Django</h3>
        <div class="step">
            <p>The <code>ALLOWED_HOSTS</code> setting defines on which hosts your application can run. Read more about it on <a href="https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts" target="django">Django docs</a>.</p>
<pre class="local" data-file="settings/production.py">
    <code>ALLOWED_HOSTS = [
        # .<em class="project-name"></em>.com,
        '.<em class="project-name"></em>.<em class="webfaction-username"></em><em>.webfactional.com</em>'
    ]</code></pre>
        </div>
        <div class="step">
            <p>The <code>EMAIL</code> settings define how Django will handle e-mail sending.</p>
<pre class="local" file="settings/production.py">
    <code>EMAIL_HOST = 'smtp.gmail.com' # Leave this as is if using gmail
    EMAIL_HOST_PASSWORD = ''
    EMAIL_HOST_USER = '' # eg. system@<em class="project-name"></em>.com</code></pre>
        </div>
        <h3>Git Repo</h3>
        <div class="step">
            <p>Create a new local git repo for our project.</p>
<pre class="local">
    <code>git init
    git add <em class="project-name"></em> requirements webfaction .gitignore manage.py README.md requirements.txt wsgi.py
    git commit -am 'Initial commit'</code></pre>
            <p>Add the remote git repo we created earlier on Webfaction. We'll call it <strong>production</strong>.</p>
<pre class="local">
    <code>git remote add <strong>production</strong> ssh://<em class="webfaction-username"></em>@<em class="webfaction-username"></em>.webfactional.com/~/webapps/git/repos/<em class="project-name"></em>.git</code></pre>
    </div>
        <h3>Test Drive</h3>
        <div class="step">
            <p>Initialize the local database. You will be asked to create an admin user, go ahead and to that.</p>
<pre class="local">
    <code>python manage.py syncdb</code></pre>
            <p>Start the development server.</p>
<pre class="local">
    <code>python manage.py runserver</code></pre>
            <p>If all goes well you should be able to go to <a href="http://127.0.0.1:8000/" target="local">http://127.0.0.1:8000/</a> and see "Hello World!".</p>
        </div>
    <h2>Server Set-up</h2>
    <div class="step">
            <p>SSH to your webfaction account.</p>
<pre class="remote">
    <code>ssh <em class="webfaction-username"></em>@<em class="webfaction-ip"></em></code></pre>
        </div>
        <h3>Install dependencies</h3>
        <p class="note"><strong>Skip</strong> this section if you already have these installed (eg. if you have created another project on the server previously).</p>

        <div class="step">
            <p>Make sure we work with Python 2.7. Add some aliases on .bash_profile to reference python2.7 instead of an older version and reload the file.</p>
<pre class="remote">
    <code>echo "alias python=python2.7" >> ~/.bash_profile
    echo "alias pip=pip-2.7" >> ~/.bash_profile
    echo "alias easy_install=easy_install-2.7" >> ~/.bash_profile
    mkdir ~/lib/python2.7
    source ~/.bash_profile</code></pre>
        </div>
        <div class="step">
            <p>Install Pip.</p>
<pre class="remote">
    <code>easy_install pip</code></pre>
        </div>
        <div class="step">
            <p>Install virtualenv &amp; virtualenvwrapper.</p>
<pre class="remote">
    <code>pip install virtualenv
    pip install --install-option="--user" virtualenvwrapper</code></pre>
        </div>
        <div class="step">
            <p>Set Environment Variables.</p>
<pre class="remote">
    <code>echo "PYTHONPATH=~/lib/python2.7" >> ~/.bash_profile
    echo "export PYTHONPATH" >> ~/.bash_profile
    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7" >> ~/.bash_profile
    echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bash_profile
    echo "export PROJECT_HOME=~/webapps" >> ~/.bash_profile
    echo "export PIP_VIRTUALENV_BASE=$WORKON_HOME" >> ~/.bash_profile
    echo "export PIP_RESPECT_VIRTUALENV=true" >> ~/.bash_profile
    echo "export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'"  >> ~/.bash_profile
    echo "if [ -f ~/bin/virtualenvwrapper.sh ]; then" >> ~/.bash_profile
    echo "    source ~/bin/virtualenvwrapper.sh" >> ~/.bash_profile
    echo "fi" >> ~/.bash_profile
    source ~/.bash_profile</code></pre>
        </div>
        <h3>Virtual Environment</h3>
        <div class="step">
            <p>Create a new virtual environment on the server.</p>
<pre class="remote">
    <code>source ~/bin/virtualenvwrapper.sh
    mkvirtualenv env_<em class="project-name"></em>
    workon env_<em class="project-name"></em></code></pre>
        </div>
        <h3>Setup</h3>
        <div class="step">
            <p>Create a new folder to place your project. It is adviced to keep your code under <strong><code>app</code></strong> as that folder is referenced in other places as well.</p>
<pre class="remote">
    <code>mkdir ~/webapps/<em class="project-name"></em>/app</code></pre>
        </div>
        <div class="step">
            <p>Switch to your project's directory.</p>
<pre class="remote">
    <code>cd ~/webapps/<em class="project-name"></em>/app/</code></pre>
        </div>
        <div class="step">
            <p>The <code>myproject</code> folder created by Webfaction will not be used so remove it.</p>
<pre class="remote">
    <code>rm -r ~/webapps/<em class="project-name"></em>/myproject</code></pre>
        </div>

        <div class="step">
            <p>Then create a new git repo and set up a post-receive hook so that whenever you push to that repo the code is checked out under <code>~/webapps/<em class="project-name"></em>/app</code>.</p>
<pre class="remote">
    <code>GIT_REPO=$HOME'/webapps/git/repos/<em class="project-name"></em>.git'
    git init --bare $GIT_REPO
    touch $GIT_REPO/hooks/post-receive
    echo "#!/bin/sh" >> $GIT_REPO/hooks/post-receive
    echo "echo 'Executing post-receive'" >> $GIT_REPO/hooks/post-receive
    echo "APP_DIR=$HOME/webapps/<em class="project-name"></em>" >> $GIT_REPO/hooks/post-receive
    echo "GIT_WORK_TREE=\$APP_DIR/app git checkout -f" >> $GIT_REPO/hooks/post-receive
    echo "GIT_WORK_TREE=\$APP_DIR/app git reset --hard" >> $GIT_REPO/hooks/post-receive
    echo "rm \$APP_DIR/app/<em class="project-name"></em>/settings/development.py" >> $GIT_REPO/hooks/post-receive
    chmod +x $GIT_REPO/hooks/post-receive</code></pre>
        </div>
        <div class="step">
            <p>If this is the first git repo you are setting up then go ahead and delete the default one created by Webfaction.</p>
<pre class="remote">
    <code>rm -r $HOME/webapps/git/repos/proj.git</code></pre>
        </div>
        <div class="step">
            <p>Push our code to our remote git repo. The post-commit hook will trigger and all our files will end up where they should.</p>
    <pre class="local">
    <code>git push <strong>production</strong> master</code></pre>
        </div>
        <div class="step">
            <p>Move the apache configuration file to the appropriate place.</p>
<pre class="remote">
    <code>mv ~/webapps/<em class="project-name"></em>/app/webfaction/httpd.conf ~/webapps/<em class="project-name"></em>/apache2/conf</code></pre>
        </div>
        <div class="step">
            <p>Install requirements.</p>
<pre class="remote">
    <code>pip install -r requirements.txt</code></pre>
        </div>
        <div class="step">
            <p>Initialize the database.</p>
<pre class="remote">
    <code>python manage.py syncdb</code></pre>
            <p>You will be asked to create an admin user. Go ahead and do that.</p>
        </div>
        <div class="step">
            <p>Compress our JS &amp; CSS.</p>
<pre class="remote">
    <code>python manage.py compress</code></pre>
        </div>
        <div class="step">
            <p>Push our local static files on AWS.</p>
<pre class="remote">
    <code>python manage.py collectstatic --noinput</code></pre>
        </div>
        <div class="step">
            <p>Restart the web server.</p>
<pre class="remote">
    <code>~/webapps/<em class="project-name"></em>/apache2/bin/restart</code></pre>
            <p>If it says that the web server is not running then start it.</p>
<pre class="remote">
    <code>~/webapps/<em class="project-name"></em>/apache2/bin/start</code></pre>
        </div>
        <div class="step">
            <p class="note">If all went well <strong><em class="project-name"></em>.<em class="webfaction-username"></em><em>.webfactional.com</em></strong> should work.</p>
        </div>
        <h2>Maintenance</h2>
        <h3>Daily Usage</h3>
        <h4>virtualenv</h4>
        <p><strong>ALWAYS</strong> work from within a virtual environment.</p>
        <div class="step">
<pre class="local">
    <code>source /usr/local/bin/virtualenvwrapper.sh</code>
    <code>workon env_<em class="project-name"></em></code></pre>
        </div>
        <div class="step">
<pre class="remote">
    <code>source ~/bin/virtualenvwrapper.sh
    workon env_<em class="project-name"></em>
    cd ~/webapps/<em class="project-name"></em>/app</code></pre>
        </div>
        <h4>Static files</h4>
        <div class="step">
            <p>Compress our JS &amp; CSS.</p>
<pre class="remote">
    <code>python manage.py compress</code></pre>
        </div>
        <div class="step">
            <p>Push our local static files on AWS.</p>
<pre class="remote">
    <code>python manage.py collectstatic --noinput</code></pre>
        </div>
        <h4>Apache</h4>
        <div class="step">
<pre class="remote">
    <code>~/webapps/<em class="project-name"></em>/apache2/bin/start
    ~/webapps/<em class="project-name"></em>/apache2/bin/restart
    ~/webapps/<em class="project-name"></em>/apache2/bin/stop</code></pre>
        </div>
        <h3>Dependencies</h3>
        <p>To update dependencies you need to first change the appropriate file under the <code>requrements</code> folder.</p>
        <p>Then you use <code>pip</code> to implement those changes.</p>
        <div class="step">
<pre class="local">
    <code>pip install -U -r requirements/development.txt</code></pre>
<pre class="remote">
    <code>pip install -U -r requirements.txt</code></pre>
        </div>
        <h3>Staging Server</h3>
        <p>Repeat steps ..</p>
    </section>

    <script type="text/javascript" src="http://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script type="text/javascript">
        var inputs = $('input[data-bind]').on('change', function(e) {
            var $this = $(this),
                val = $this.val(),
                group = $this.attr('data-bind'),
                siblings = inputs.filter('[data-bind="' + group + '"]'),
                fields = $this.data('inputs') ||
                    $this.data('inputs', $('.' + $this.attr('data-bind'))) &&
                    $this.data('inputs');
            fields.each(function(i, field) {
                var $this = $(this),
                    suffix = $this.attr('data-suffix') || '',
                    prefix = $this.attr('data-prefix') || '',
                    value = prefix + val + suffix,
                    method = this.tagName === 'INPUT' ? 'val' : 'text';
                $this[method](value).trigger('change');
            });
            siblings.add(this).val(val);
        });
        var toc = $('#toc'),
            headings = $('.instructions').find('h2, h3, h4');
        headings.each(function(i, el) {
            var level = parseInt(this.tagName.replace(/^H/, ''), 10),
                $this = $(this).attr('id', 'heading-' + i )
                    .attr('data-index', i)
                    .attr('data-level', level),
                title = $this.text(),
                parent = getParent($this),
                entry = $('<li id="at-heading-' + i +'"></li>')
                    .append('<a href="#heading-' + i + '">' + title + '</a>'),
                parent_entry = parent ?
                    $('#at-heading-' + parent.attr('data-index')) :
                    null,
                list = $('> ol', parent_entry),
                appendTo = parent_entry ?
                    list.length ?
                        list :
                        $('<ol></ol>').appendTo(parent_entry)
                     :
                    toc;
            entry.appendTo(appendTo);
        });
        function getParent(heading) {
            var index = parseInt(heading.attr('data-index'), 10) - 1,
                level = parseInt(heading.attr('data-level'), 10),
                parent, parent_level;
            if (index < 0) { return null; }
            do {
                parent = headings.eq(index--);
                parent_level = parseInt(parent.attr('data-level'), 10);
                if (isNaN(parent_level) ||
                        index < 0 ||
                        !parent.length ||
                        parent[0] === heading[0]) {
                    parent = null;
                    break;
                }
            } while (parent_level >= level);
            return parent;
        }
        $('#generate-password').click(function(e) {
            e.preventDefault();
            e.stopPropagation();
            inputs
                .filter('[data-bind="db-password"]')
                    .val(generatePassword())
                    .trigger('change');
        }).click();
        function generatePassword() {
            // http://stackoverflow.com/a/1497512/67903
            var length = 12,
                charset = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_",
                retVal = "";
            for (var i = 0, n = charset.length; i < length; ++i) {
                retVal += charset.charAt(Math.floor(Math.random() * n));
            }
            return retVal;
        }
    </script>