from django.db import models

# Create your models here.

class patientsymptomsanalysis(models.Model):
    patintid = models.CharField(max_length=10)
    patinetname = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    patinetallsymptoms = models.CharField(max_length=600)
    diseasname = models.CharField(max_length=250)
    descriptions = models.CharField(max_length=600)
    createdon = models.DateTimeField(max_length=50)
    status = models.CharField(max_length=600,default='waiting')
    docname = models.CharField(max_length=600,default='notassigned')
    
    def __str__(self):
        return self.createdon


class blkchainapproach(models.Model):
    id = models.AutoField(primary_key=True)
    docname = models.CharField(max_length=100)
    docid = models.IntegerField()
    patientname = models.CharField(max_length=100)
    patientid = models.IntegerField()
    disease = models.CharField(max_length=100)
    price = models.FloatField()
    sysmptid = models.IntegerField()
    ledgerbalance = models.FloatField()
    tranxid = models.IntegerField()

    def __str__(self):
        return self.tranxid

class transactionsstore(models.Model):
    id = models.AutoField(primary_key=True)
    docid = models.IntegerField()  
    patientid = models.IntegerField() 
    nameoncard = models.CharField(max_length=100)
    cvv = models.IntegerField()
    cardnumber = models.CharField(max_length=100)
    expiredate = models.CharField(max_length=100)
    tranxid = models.IntegerField()
    price = models.FloatField()
    ledgerbalance = models.FloatField()




