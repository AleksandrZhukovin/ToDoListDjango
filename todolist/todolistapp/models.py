from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=250)


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
