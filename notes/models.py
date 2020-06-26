from django.db import models
from django import forms
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Note(models.Model):
    title = models.CharField(max_length=100, blank=True)
    text = HTMLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title