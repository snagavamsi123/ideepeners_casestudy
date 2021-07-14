from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.forms.widgets import SelectDateWidget, Widget
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone

class signup(models.Model):
    Mobile = PhoneNumberField(null=False,blank=False,unique=True)
    Email = models.EmailField(null=False,blank=False,unique=True)
    Age = models.IntegerField(null=True,
                              blank=True,
                              validators=[MaxValueValidator(100)])
    Password = models.CharField(max_length=15,null=False,blank=False)

    def __str__(self):
        return str(self.Mobile)

class DailyUpdate(models.Model):
    Date = models.DateField(default=timezone.now)
    Area = models.CharField(max_length=100,null=False,blank=False)
    AppointedPersons = models.IntegerField(default=0,null=False,blank=False)
    NoOfClients = models.IntegerField(default=0,null=False,blank=False)

    def __str__(self):
        return self.Area


gender_choice = (('Male','MALE'),('Female','FEMALE'))
class ClientDetails(models.Model):
    Name = models.CharField(max_length=100,null=False,blank=False)
    DateOfBirth = models.DateField()
    Age = models.IntegerField(null=True,
                              blank=True,
                              validators=[MaxValueValidator(100)])

    Gender = models.CharField(max_length=10,choices=gender_choice)
    FamilySize = models.IntegerField(null=True,blank=True,default=2)

    def __str__(self):
        return self.Name



#---------2nd question Queries Dont consider these------------------------------------

'''
class Customer(models.Model):
    
    customer_name = models.CharField(max_length=25)
    City = models.CharField(max_length=25)
    State = models.CharField(max_length=25)
    def __str__(self):
        return str(self.customer_name)

class Order(models.Model):
    #order_id = models.IntegerField(unique=True,default=0)
    order_date = models.DateField()
    order_amount = models.FloatField()
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,default=0)
    def __str__(self):
        return str(self.customer_id)

status_chioces = (('failed','FAILED'),('paid','PAID'))
class Payment(models.Model):
    payment_id =models.IntegerField(default=0)
    status = models.CharField(max_length=10,choices=status_chioces)
    Order_id= models.ForeignKey(Order,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return str(self.payment_id)


'''
