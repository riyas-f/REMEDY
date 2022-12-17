from django.db import models

# Create your models here.

class MedicineName(models.Model):
    medicine_name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Medicine Name"

    def __str__(self):
        return self.medicine_name

class MedicineRecord(models.Model):
    medicine_name=models.ForeignKey(MedicineName,on_delete=models.PROTECT,related_name='+')
    medicine_details=models.TextField()

    class Meta:
        verbose_name_plural = "Medicine Details"

    def __str__(self):
        return self.medicine_details


