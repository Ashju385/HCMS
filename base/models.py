from email.policy import default
import imp
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=10,null=False,primary_key=True)
    name = models.CharField(max_length=50,null=False)
    house_num = models.CharField(max_length=10,blank=False)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50,null=True)
    created = models.DateTimeField(auto_now_add=True,null=False)

    def __str__(self):
        return self.name

class Service(models.Model):
    ##pool_id= models.CharField(max_length=10,primary_key=True)
    OPTION= (('Swimming Pool','Swimming Pool'),
    ('Picnic Spot','Picnic Spot'),
    ('Community Hall','Community Hall')
    )
    service_name = models.CharField(max_length=50,null=False,choices=OPTION,default="Select")
    member_name = models.ForeignKey(Member,null=True,on_delete=models.CASCADE)
    ##status = models.BooleanField(null=True)
    start = models.DateField(auto_now=False)
    end =  models.DateField(auto_now=False,blank=True)
    date_ordered = models.DateTimeField(auto_now=True,null=True)
    date_finished = models.DateTimeField(auto_now_add=True,null=True)
    total_d= models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(7)],default=0)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return self.service_name