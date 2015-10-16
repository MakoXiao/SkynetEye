# SkynetEye

SkynetEye 天网监控中心
---

# pycharm download
https://download.jetbrains.com/python/pycharm-community-4.5.4.tar.gz
http://download.jetbrains.com/python/pycharm-community-4.5.4.tar.gz

# jdk 1.7
```
whoami@ubuntu:~$ apt-get install  java-1.7-open

whoami@ubuntu:~$ grep JAVA_HOME .profile
JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
PATH=.:$JAVA_HOME/bin:$PATH

```

# your git info
https://github.com/itweet/SkynetEye.git
```
whoami@ubuntu:~$ git config --global user.name "SkynetEye"
whoami@ubuntu:~$ git config --global user.email "whoami@qq.com"
whoami@ubuntu:~$ cd ~/.ssh
whoami@ubuntu:~$ rm -rf  ~/.ssh/*
whoami@ubuntu:~$ ssh-keygen -t rsa -C "whoami@qq.com"
```

# git SkynetEye
```
git clone https://github.com/itweet/SkynetEye.git
```

# python+django
```
whoami@ubuntu:~$ sudo apt-get install python-pip
whoami@ubuntu:~$ sudo pip install Django==1.8.4
whoami@ubuntu:~$ sudo pip install django-suit==0.2.15
whoami@ubuntu:~$ sudo pip install django-session-security
whoami@ubuntu:~$ sudo pip install paramiko
whoami@ubuntu:~$ sudo pip install django-debugtools

## install python-mysql model
whoami@ubuntu:~$ sudo apt-get install python-mysqldb  #for ubuntu
yum install MySQL-python  #for CentOS
```

# install mysql
```
whoami@ubuntu:~$ sudo apt-get install mysql-server mysql-client

whoami@ubuntu:~$ mysql -uroot -padmin
mysql> create database SkynetEye;
mysql> exit
```

# config settings.py
```
 eidt SkynetEye/settings.py
 # Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SkynetEye',
        'HOST': 'localhost',
        'PORT':3306,
        'USER':'root',
        'PASSWORD': 'admin'
    }
}
```

# initialization database table
```
whoami@ubuntu:~/py/SkynetEye$ python manage.py syncdb
....omit....
You have installed Django's auth system, and don't have any superusers defined.
Would you like to create one now? (yes/no): yes     
Username (leave blank to use 'whoami'): whoami
Email address: whoami@gmail.com
Password: 
Password (again): 
Superuser created successfully.

whoami@ubuntu:~/py/SkynetEye$ python manage.py makemigrations
whoami@ubuntu:~/py/SkynetEye$ python manage.py migrate
whoami@ubuntu:~/py/SkynetEye$ python manage.py createsuperuser #创建后台管理员用户(如果在执行python manage.py syncdb的时候已经创建了用户了，这一步可以不执行, RemovedInDjango19Warning: The syncdb command will be removed in Django 1.9)
```

# run web app 
## with pycharm
### 1. pycharm debug-runserver
```
whoami@ubuntu:/apps/pycharm$ sh bin/pycharm.sh

├── pycharm 
    └── Open SkynetEye Project
```

### 2. pycharm debug
```
├── Run-->Debug Configurations-->Add New Configuration-->Python
    └── Name : debug-runserver
     └──Script: /home/whoami/py/SkynetEye/manage.py
     └──Script: runserver 0.0.0.0:8000
     └──Python interpreter: Python 2.7.6(/usr/bin/python2.7) 

├──Run-->Debug-->debug-runserver
```

## command run
```
whoami@ubuntu:~/py/SkynetEye$ python manage.py runserver 0.0.0.0:8001
```

## FireFox visit
  FireFox Address : http://localhost:8000/admin 

# pip install joe
   -  A .gitignore magician in your command line. Joe generates .gitignore files from the command line for you.
   - https://github.com/karan/joe

```
# git tracking  file delete
whoami@ubuntu:~/py/SkynetEye$ git rm -r --cached .idea
whoami@ubuntu:~/py/SkynetEye$ git rm -r --cached *.pyc

# use joe 
whoami@ubuntu:~/py/SkynetEye$ sudo pip install joe
whoami@ubuntu:~/py/SkynetEye$ joe

     _
    (_)   _      __
    | | /'_`\  /'__`\
    | |( (_) )(  ___/
 _  | |`\___/'`\____)
( )_| |
`\___/'


joe generates .gitignore files from the command line for you

Usage:
  joe (ls | list)
  joe [NAME...]
  joe (-h | --help)
  joe --version

Options:
  -h --help     Show this screen.
  --version     Show version.

whoami@ubuntu:~/py/SkynetEye$ joe ls
actionscript, ada, agda, android, anjuta, appceleratortitanium, archlinuxpackages, archives, autotools, bricxcc, c, c++, cfwheels, cmake, cvs, cakephp, chefcookbook, clojure, cloud9, codeigniter, codekit, commonlisp, composer, concrete5, coq, craftcms, dm, dart, darteditor, delphi, dreamweaver, drupal, episerver, eagle, eclipse, eiffelstudio, elisp, elixir, emacs, ensime, erlang, espresso, expressionengine, extjs, fancy, finale, flexbuilder, forcedotcom, fortran, fuelphp, gwt, gcov, gitbook, go, gradle, grails, haskell, igorpro, ipythonnotebook, idris, jdeveloper, java, jboss, jekyll, jetbrains, joomla, jython, kdevelop4, kate, kohana, labview, laravel, lazarus, leiningen, lemonstand, libreoffice, lilypond, linux, lithium, lua, lyx, magento, matlab, maven, mercurial, mercury, metaprogrammingsystem, meteor, microsoftoffice, modelsim, momentics, monodevelop, nanoc, netbeans, nim, ninja, node, notepadpp, ocaml, osx, objective-c, opa, opencart, oracleforms, packer, perl, phalcon, playframework, plone, prestashop, processing, python, qooxdoo, qt, r, ros, rails, redcar, redis, rhodesrhomobile, ruby, rust, sbt, scons, svn, sass, scala, scrivener, sdcc, seamgen, sketchup, slickedit, stella, sublimetext, sugarcrm, swift, symfony, symphonycms, tags, tex, textmate, textpattern, tortoisegit, turbogears2, typo3, umbraco, unity, vvvv, vagrant, vim, virtualenv, visualstudio, waf, webmethods, windows, wordpress, xcode, xilinxise, xojo, yeoman, yii, zendframework, zephir

whoami@ubuntu:~/py/SkynetEye$ joe java python osx > .gitignore
whoami@ubuntu:~/py/SkynetEye$ cat .gitignore 
#### joe made this: http://goel.io/joe

#####=== Java ===#####

*.class

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.ear

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*

#####=== Python ===#####

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.cache
nosetests.xml
coverage.xml

# Translations
*.mo
*.pot

# Django stuff:
*.log

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Idea
.idea

#####=== OSX ===#####
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon

# Thumbnails
._*

# Files that might appear on external disk
.Spotlight-V100
.Trashes

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

whoami@ubuntu:~/py/SkynetEye$ git add .
whoami@ubuntu:~/py/SkynetEye$ git commit -m "update joe .gitignore"
whoami@ubuntu:~/py/SkynetEye$ git push origin master
```

# pip install psutil
```
whoami@ubuntu:~$ sudo pip install psutil

```