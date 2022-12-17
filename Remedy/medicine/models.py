from django.db import models

# Create your models here.

class MedicineRecord(models.Model):
    medicine_name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Medicine Name"
        ordering = ['medicine_name']

    def __str__(self):
        return self.medicine_name

    medicine_details=models.TextField()

    class Meta:
        verbose_name_plural = "Medicine Details"

    def __str__(self):
        return self.medicine_details
