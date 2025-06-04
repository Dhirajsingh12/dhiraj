from django.db import models
class service (models.Model):
    service_ID=models.CharField(max_length=50)
    service_Title=models.CharField(max_length=50)
    service_Desc=models.TextField()
# Create your models here.
