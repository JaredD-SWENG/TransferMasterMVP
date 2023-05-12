from django.db import models

# Create your models here.
from django.db import models
#Create your models here

#NEXT STEP1: add constraints to all the fields (such as NOT NULL)
#NEXT STEP2: create the actual functions that populate those fields such as file upload
#table: Users
class Users(models.Model):
    Username = models.TextField(max_length=191)
    Role = models.TextField(max_length=50)
    Password = models.TextField(max_length=191)
    db_table_name = "Users"

#table: ExternalSyllabus
class ExternalSyllabus(models.Model):
    UniversityName = models.TextField(max_length=255)
    ExtenalCourseName = models.TextField(max_length=100)
    ExternalCourseNumber = models.TextField(max_length=10)
    SourceID = models.TextField(max_length=10)
    SchoolSubject = models.TextField(max_length=100)
    ExternalUnits = models.DecimalField(max_digits=6, decimal_places=2)
    TermType = models.TextField(max_length=15)
    ExternalCourseDescription = models.TextField(max_length=255)
    AccreditionStatus = models.TextField(max_length=50)
    db_table_name = "ExternalSyllabus"

#table: PSUSyllabus
class PSUSyllabus(models.Model):
    PSUCourseName = models.TextField(max_length=100)
    PSUCourseNumber = models.TextField(max_length=10)
    PSUUnits = models.DecimalField(max_digits=6, decimal_places=2)
    PSUCourseCatalog = models.TextField(max_length=191)
    db_table_name = "PSUSyllabus"

#table: TransferRequest
class TransferRequest(models.Model):
    ExternalID = models.ForeignKey(ExternalSyllabus, db_column='external_id', on_delete=models.CASCADE, related_name='transfer_requests')
    PSUID = models.ForeignKey(PSUSyllabus, db_column='psu_id', on_delete=models.CASCADE, related_name='transfer_requests')
    UnitsTaken = models.IntegerField()
    PercentMatch = models.DecimalField(max_digits=6, decimal_places=2)
    Match = models.BooleanField()
    db_table_name = "TransferRequest"

