from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250)


class Task(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)
    deadline = models.DateField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
