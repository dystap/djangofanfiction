from django.db import models

# Create your models here.


class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=67)
    birthday = models.DateField()
    hobby = models.CharField(max_length=67)
    quote = models.TextField(blank=True, null=True)
