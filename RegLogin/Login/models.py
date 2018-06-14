from __future__ import unicode_literals

from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=32, null=False)
    is_ban = models.BooleanField(null=False, default=False)
    role = models.CharField(max_length=1, null=False, default=1)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=11, null=True)
    register_time = models.DateTimeField(null=False, auto_now=True)
    last_login_time = models.DateTimeField(null=False, auto_now=True)
