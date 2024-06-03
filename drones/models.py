from django.db import models
from common.models import AuditModel
from users.models import User
# Create your models here.
class Drone(AuditModel):
    company_name = models.CharField(max_length= 120)
    drone_description = models.TextField(blank = True, null = True)
    droneid= models.CharField(max_length=250,default='none')
    expiry = models.DateTimeField(null=True,blank=True)
    manufacturer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    live = models.BooleanField(default=False)
    
    def __str__(self):
        return self.company_name


class DroneData(AuditModel):
    droneid=models.CharField(max_length=223)
    time= models.DateTimeField(max_length=128)
    FileField = models.FileField(upload_to='media',default='null')
    def __str__(self):
        return self.droneid