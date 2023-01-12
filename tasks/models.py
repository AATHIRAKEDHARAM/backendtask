from django.db import models
import datetime
from django.db import models
from api.models import *



class UserReg(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table="userreg"    

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(default=1)
    assigned_to = models.ForeignKey(UserReg, on_delete=models.CASCADE)
    time_stamp= models.DateTimeField(auto_now_add=True)  
    
    class Meta:
        db_table="task"    
    
    
 
