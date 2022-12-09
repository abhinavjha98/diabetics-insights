from django.db import models

# Create your models here.
class Diabetes_table(models.Model):
    name=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=255,null=True)
    age=models.IntegerField(default=0)
    blood_pressure=models.FloatField(default=0.0)
    glucose=models.FloatField(default=0.0)
    insulin=models.IntegerField(default=0)
    bmi = models.FloatField(default=0.0)
    skin_thickness=models.FloatField(default=0.0)
    result = models.CharField(max_length=255,null=True)