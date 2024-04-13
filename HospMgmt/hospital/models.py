from django.db import models

# Create your models here.

#When no primary key is given to sql it creates an 
#id field by default which will be used later

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)
    type_of_doctor = models.CharField(max_length=20) 

    #String representation of object for ease
    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=100)

    #String representation of object for ease
    def __str__(self):
        return self.name


class Appointment(models.Model):
    ''' Note on models.ForeignKey:
        Used to reference objects from different models
        many-to-one relationship
    
        Note on models.CASCADE:
        This is the behaviour to adopt when a referenced object is deleted.
        When the referenced object is deleted, also delete the objects that have 
        references to it        
    '''
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    #String representation of object for ease
    def __str__(self):
        return self.doctor.name + self.patient.name

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
