# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import  views
from django.contrib import admin
from models import Jobs, Apply, UserEmail

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Apply)
admin.site.register(UserEmail)