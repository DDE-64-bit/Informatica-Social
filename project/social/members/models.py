from django.db import models

class Member(models.Model):
  voorNaam = models.CharField(max_length=255)
  achterNaam = models.CharField(max_length=255)