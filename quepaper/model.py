from django.db import models


class User(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # confirm_password = models.CharField(max_length=100)
    class Meta:
        db_table = 'userdetails'


class Question(models.Model):
    objects = None
    course = models.CharField(max_length=100)
    question = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    class Meta:
        db_table = 'questions'


class Createpaper(models.Model):
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    noofsection = models.CharField(max_length=100)
    qps = models.IntegerField()
    code = models.CharField(max_length=100)
    cps = models.IntegerField()
    time = models.CharField(max_length=100)
    marka = models.IntegerField()
    markb = models.IntegerField(null=True)
    markc = models.IntegerField(null=True)
    class Meta:
        db_table = 'createpaper'