# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CaiPiaoInfo(models.Model):
    cp_date = models.CharField(max_length=255)
    cp_num = models.CharField(max_length=255)
    cp_red_1 = models.IntegerField()
    cp_red_2 = models.IntegerField()
    cp_red_3 = models.IntegerField()
    cp_red_4 = models.IntegerField()
    cp_red_5 = models.IntegerField()
    cp_red_6 = models.IntegerField()
    cp_blue_7 = models.IntegerField()

