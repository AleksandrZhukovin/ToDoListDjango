from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('edit_project', kwargs={'pk': self.pk})


class Task(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=(('Undone', 'Undone'), ('Done', 'Done')))
    priority = models.IntegerField(default=0)
    deadline = models.DateField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
