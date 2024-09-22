from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=80, default = "")
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=200, default = "")
    insurance_name = models,models.CharField(max_length=80, default = "")
    insurance_num = models.CharField(max_length=100, default = "")