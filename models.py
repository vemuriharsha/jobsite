# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class EmailForm(forms.Form):
      firstname = forms.CharField(max_length=255)
      lastname = forms.CharField(max_length=255)
      email = forms.EmailField()
      subject = forms.CharField(max_length=255)
      botcheck = forms.CharField(max_length=5)
      message = forms.CharField()

class Jobs(models.Model):
      jobtype =  models.CharField(max_length=50)
      desc = models.CharField(max_length=250)
      description = models.CharField(max_length=500, default='Enter Description')
      requirements=models.CharField(max_length=1000,default='Enter Requirements')
      location = models.CharField(max_length=20, default='Enter Location')

      def __str__(self):
          return self.jobtype
          return self.desc
          return self.description
          return self.requirements
          return self.location


class Apply(models.Model):
      signoff=models.CharField(max_length=50,default=' ')
      firstname = models.CharField(max_length=25)
      lastname = models.CharField(max_length=20)
      headline = models.CharField(max_length=25)
      industry = models.CharField(max_length=30)
      mobile = models.IntegerField()
      city = models.CharField(max_length=20)
      zipcode = models.IntegerField()
      email = models.EmailField()
      country= models.CharField(max_length=30)
      stateprovince = models.CharField(max_length=30)
      resume =models.FileField(upload_to='documents/%y/%m/%d')
      #gresume=models.FileField(upload_to='documents/%y/%m/%d',default='SOME STRING')

      def __str__(self):
          return self.firstname
          return self.lastname
          return self.mobile
          return self.email
          return self.resume

      class Meta:
          db_table = "Apply"

class Email(models.Model):
    email = models.CharField(max_length=200)


class UserEmail(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Register(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    date_birth = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=1,
                           choices=(
                                    ('M', 'Male'),
                                    ('F', 'Female')
                           )
                           )
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    totexp = models.IntegerField()
    relexp = models.IntegerField()
    employer1 = models.CharField(max_length=30)
    doj1 = models.DateField()
    employer2 = models.CharField(max_length=30)
    doj2 = models.DateField()
    skills = models.CharField(max_length=50)
    current_role=models.CharField(max_length=30)

    def __str__(self):
        return self.firstname



class Board(models.Model):
    name=models.CharField(max_length=30, unique=True)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject=models.CharField(max_length=255)
    last_updated=models.DateTimeField(auto_now_add=True)
    board=models.ForeignKey(Board,related_name='topics')
    starter = models.ForeignKey(User,related_name='topics')

class Post(models.Model):
    message=models.TextField(max_length=4000)
    topic=models.ForeignKey(Topic, related_name='posts')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(null=True)
    created_by=models.ForeignKey(User,related_name='posts')
    updated_by=models.ForeignKey(User,null=True,related_name='+')




