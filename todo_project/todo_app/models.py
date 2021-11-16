from __future__ import unicode_literals

from django.db import models

# Create your models here.

class to_do_list(models.Model):
    name=models.CharField(max_length=30)
    create_date=models.DateField()

    def __str__(self):
        return self.name

class to_do_item(models.Model):
    description=models.CharField(max_length=100)
    due_date=models.DateField()
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(to_do_list)

    def __str__(self):
        return self.description



