from django.db import models

class patientregistrationmodel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status  = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class docotrtregistrationmodel(models.Model):
    doctorname = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status  = models.CharField(max_length=100)

    def __str__(self):
        return self.emailid
