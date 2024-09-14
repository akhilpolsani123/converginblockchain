from django.db import models

# Create your models here.

class doctorreplaysysmptoms(models.Model):
    patientid = models.CharField(max_length=10)
    sysid = models.CharField(max_length=100)
    patinetname = models.CharField(max_length=60)
    docid = models.CharField(max_length=60)
    doctorname=models.CharField(max_length=60)
    email = models.CharField(max_length=600)
    mobile = models.CharField(max_length=250)
    city = models.CharField(max_length=600)
    patinetallsymptoms = models.CharField(max_length=5000)
    diseasname = models.CharField(max_length=600)
    descriptions = models.CharField(max_length=600)
    reqdate = models.DateTimeField()
    prescription1 = models.CharField(max_length=100)
    prescription2 = models.CharField(max_length=100)
    prescription3 = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    blkchMoney = models.CharField(max_length=100)   
    respdate = models.DateTimeField()
    status = models.CharField(max_length=600)
    
    def __str__(self):
        return self.respdate


