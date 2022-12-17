from django.db import models

# Create your models here.

class MedicineRecord(models.Model):
    medicine_name=models.CharField(max_length=100)

    class Meta:
        ordering = ['medicine_name']

    def __str__(self):
        return self.medicine_name

class MedicineDetails(models.Model):
    medicine_details=models.TextField()

    def __str__(self):
        return self.medicine_details
