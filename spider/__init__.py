import sys
import os

#sys.path.append('../../../Jpider')
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'spider.settings'



import django
django.setup()
