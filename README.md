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

