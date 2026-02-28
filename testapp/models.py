from django.db import models

# Create your models here.
class Jobs(models.Model):
    #left side value stored in db and right side value displays in forms/admin/templates
    CITY_CHOICES=(
        ('HYD','Hyderabad'),
        ('BNG','Bangalore'),
        ('PUN','Pune'),
    )
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30) 
    salary=models.IntegerField()
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
    city=models.CharField(max_length=3,choices=CITY_CHOICES) 