from django.db import models
from django.contrib.auth.models import User

class Greeting(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Page(models.Model):
    url = models.TextField()
    users = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class UserPageAssociation(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    page = models.ForeignKey(Page, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

class Snapshot(models.Model):
    page = models.ForeignKey(Page, null=False, blank=False)
    image = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Resource(models.Model):
    name= models.TextField()
    page= models.ForeignKey(Snapshot, null=False,blank=False)
    data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Revision(models.Model):
    resource = models.ForeignKey(Resource,null=False, blank=False)
    snapshot = models.ForeignKey(Snapshot,null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
