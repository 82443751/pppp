from django.db import models

# Create your models here.
class One(models.Model):
    test=models.ForeignKey('backend.Option')

