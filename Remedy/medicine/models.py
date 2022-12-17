from django.db import models

# Create your models here.

class MedicineType(models.Model):
    type = models.CharField(max_length=100)

class MedicineTime(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

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

class SavedMedicines(models.Model):
    medicine_name=models.ForeignKey(MedicineName,on_delete=models.PROTECT,related_name='+')
    time=models.ManyToManyField(MedicineTime)
    dosage = models.IntegerField()
    timeof = models.BooleanField()

    def __str__(self):
        return self.medicine_name