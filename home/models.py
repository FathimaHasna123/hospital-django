from django.db import models

# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    email =  models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    
    
def __str__(self):
 return self.name

class Department(models.Model):
    name =  models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
class Doctors(models.Model):
    doctrosName =  models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE ,null=True,blank=True)
    image =  models.ImageField(upload_to='doctors/',null=True,blank=True)
    
    
    def __str__(self):
        return self.doctrosName   
    
    
class Appointment(models.Model):
    name =  models.CharField(max_length=255,null=True,blank=True)
    phone =  models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE ,null=True,blank=True)
    doctros = models.ForeignKey(Doctors,on_delete=models.CASCADE ,null=True,blank=True)
    time =  models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.name     