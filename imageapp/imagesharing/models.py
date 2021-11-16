from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.
#MVC  MODEL VIEW CONTROLLER



class User_details(models.Model):
    username=models.CharField(max_length=120)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    register=models.ForeignKey(User)

    def __str__(self):
        return self.username


class Post(models.Model):
    username=models.CharField(max_length=120)
    title = models.CharField(max_length = 120)
    image=models.FileField(null=True, blank=True)
    content = models.TextField()
    updated= models.DateTimeField(auto_now = True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)
    user=models.ForeignKey(User_details)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
        #return "/posts/%s/" %(self.id)


