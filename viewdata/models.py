from django.db import models
#Create your models here.

    
class Laboratory(models.Model):
    labName = models.CharField(max_length=45, null=True)
    labID = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    buildingNum = models.DecimalField(max_digits=3, decimal_places=0, null=True) 
    floorNum = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    numOfPC = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    numberOfChair = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    labCapacity =  models.DecimalField(max_digits=4, decimal_places=0, null=True)
    Status = models.CharField(max_length = 20, null=True)

# class Computer(models.Model):
#     pc_labID = models.DecimalField(max_digits=10, decimal_places=0, null=True)
#     repaired = models.BooleanField(default=False, null=True)    
#     new = models.BooleanField(default=True, null=True)
#     pcID = models.DecimalField(max_digits=10, decimal_places=0, null=True) 
    
class Device(models.Model):
    pc_labID = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    repaired = models.BooleanField(default=False, null=True)    
    new = models.BooleanField(default=True, null=True)
    pcID = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True) 

class BrokenPC(models.Model):

    prob = [('Software', 'Software'), ('Hardware', 'Hardware')]

    LabId = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    # status = models.BooleanField(default=False, null=True)
    ProblemType = models.CharField(max_length=50, choices=prob)
    description = models.TextField(max_length=150, null=True)
    date = models.DateField(null=True)
    BrokenID = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)

# class Pc(models.Model):

#     pcID = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    
#     pc_labID = models.DecimalField(max_digits=10, decimal_places=0, null=True)
#     repaired = models.BooleanField(default=False, null=True)    
#     new = models.BooleanField(default=True, null=True)


# class Lab(models.Model):
#     labName = models.CharField(max_length=45, null=True)
#     labID = models.DecimalField(max_digits=10, decimal_places=0, null=True)
#     buildingNum = models.DecimalField(max_digits=3, decimal_places=0, null=True) 
#     floorNum = models.DecimalField(max_digits=3, decimal_places=0, null=True)
#     numOfPC = models.DecimalField(max_digits=3, decimal_places=0, null=True)
#     numberOfChair = models.DecimalField(max_digits=3, decimal_places=0, null=True)
#     labCapacity =  models.DecimalField(max_digits=4, decimal_places=0, null=True)
#     Status = models.CharField(max_length = 20, null=True)