from pyexpat import model
from django.db import models

# Create your models here.
class VisitorsExpoce(models.Model):
    id = models.BigIntegerField(primary_key=True,serialize=False)
    attend = models.CharField(max_length=100)
    firstName = models.CharField(db_column='firstName', max_length=250)  # Field name made lowercase.
    lastName = models.CharField(db_column='lastName', max_length=250)  # Field name made lowercase.
    email = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    cState = models.CharField(db_column='cState', max_length=100)  # Field name made lowercase.
    phone = models.CharField(max_length=50)
    languageLevel = models.CharField(db_column='languageLevel', max_length=50)  # Field name made lowercase.
    program = models.CharField(max_length=250)
    studyArea = models.CharField(db_column='studyArea', max_length=100)  # Field name made lowercase.
    dateStart = models.CharField(db_column='dateStart', max_length=100)  # Field name made lowercase.
    pay = models.CharField(max_length=100)
    sourceLead = models.CharField(db_column='sourceLead', max_length=100)  # Field name made lowercase.
    fuente = models.CharField(max_length=100)
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitors_ExpoCE'