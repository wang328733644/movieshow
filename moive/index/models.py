# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Comments(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    mov = models.ForeignKey('Movie', models.DO_NOTHING)
    content = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'comments'


class Event(models.Model):
    movie = models.ForeignKey('Movie', models.DO_NOTHING)
    click_counts = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'event'


class Movie(models.Model):
    name = models.CharField(max_length=128)
    img = models.CharField(max_length=256)
    des = models.CharField(max_length=10000)
    area = models.ForeignKey('MovieAreas', models.DO_NOTHING)
    actors = models.CharField(max_length=1024)
    year = models.CharField(max_length=16)
    type = models.ForeignKey('MovieTypes', models.DO_NOTHING)
    score = models.CharField(max_length=64)
    status = models.IntegerField(blank=True, null=True)
    letter = models.CharField(max_length=4)
    url = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'movie'


class MovieAreas(models.Model):
    area_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_areas'


class MovieTypes(models.Model):
    type_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_types'


class Nav(models.Model):
    huge_pic = models.CharField(max_length=128)
    movie_name = models.CharField(max_length=10, blank=True, null=True)
    movie_desc = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nav'


class News(models.Model):
    img = models.CharField(max_length=256)
    title = models.CharField(max_length=512)
    short_content = models.CharField(max_length=10000)
    long_content = models.TextField()
    time = models.CharField(max_length=128)
    view = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class Permission(models.Model):
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'permission'


class SuperUser(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    tel = models.CharField(unique=True, max_length=16)
    email = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'super_user'


class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    tel = models.CharField(unique=True, max_length=11)
    email = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'user'


class UserStatus(models.Model):
    id = models.ForeignKey(User, models.DO_NOTHING, db_column='id', primary_key=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_status'


class UserTicket(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    ticket = models.CharField(max_length=64)
    out_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_ticket'
