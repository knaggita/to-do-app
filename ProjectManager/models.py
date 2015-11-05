from django.db import models


class ActionPlan(models.Model):
    name = models.CharField(max_length=200)
    tasks = models.CharField(max_length=200)
    responsibility = models.CharField(max_length=200)
    objective = models.CharField(max_length=200)
    Date_Due = models.DateTimeField('due date')
    Date_Finished = models.DateTimeField()


class Contact(models.Model):
    ContactName = models.CharField(max_length=200)
    About = models.CharField(max_length=200)
    WayForward = models.CharField(max_length=200)
    DateSeen = models.DateTimeField('date seen')
    nextMtg = models.DateTimeField()


class Task(models.Model):
    Task = models.CharField(max_length=200)
    objective = models.CharField(max_length=200)
    Due_Date = models.DateTimeField()
    Finish_Date = models.DateTimeField()
