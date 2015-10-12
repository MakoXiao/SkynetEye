__author__ = 'whoami'
import os,sys

basedir = "/".join(__file__.split("/")[:-2])
sys.path.append(basedir)

sys.path.append('%s/SkynetEye'%basedir)
os.environ['DJANGO_SETTINGS_MODULE'] ='SkynetEye.settings'
import django
django.setup()

