from django.db import models


class Incident(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    timeDateDispatched = models.DateTimeField()
    incidentType = models.ForeignKey('IncidentType', on_delete=models.PROTECT)
    dispatchedUnits = models.ManyToManyField('Units')
    nearestStation = models.OneToOneField('Station', on_delete=models.PROTECT)
    alarmLevel = models.IntegerField()
    location = models.CharField(max_length=200)


class Units(models.Model):
    name = models.CharField(max_length=200)
    codeName = models.CharField(max_length=10)


class Station(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class IncidentType(models.Model):
    name = models.CharField(max_length=200)
