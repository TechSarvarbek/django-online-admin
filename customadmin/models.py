# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendances(models.Model):
    arrivaltime = models.DateTimeField(db_column='arrivalTime')  # Field name made lowercase.
    departuretime = models.DateTimeField(db_column='departureTime', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    studentid = models.ForeignKey('Students', models.DO_NOTHING, db_column='StudentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attendances'


class Employees(models.Model):
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Students(models.Model):
    telegramid = models.BigIntegerField(db_column='telegramId', unique=True)  # Field name made lowercase.
    fullname = models.CharField(max_length=255)
    school = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    phone = models.BigIntegerField()
    direction = models.TextField()  # This field type is a guess.
    step = models.IntegerField(blank=True, null=True)
    graph = models.DateTimeField(blank=True, null=True)
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Students'

