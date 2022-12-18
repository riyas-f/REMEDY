from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
# Create your views here.

@login_required(login_url='login/')
def addmed(request):
    if request.method == 'POST':
        medicine_name = request.POST['name']
        type = request.POST['type']
        dosage = request.POST['dosage']        
        intake = request.POST['intake']
        time = request.POST['time']

        #Save data to database
        savedMedicine = SavedMedicines.objects.create(medicine_name = medicine_name, dosage=dosage,type=type, time=time )
        savedMedicine.save()           
  
        messages.success(request, 'Record Saved')
    medicines=MedicineName.objects.all()
    return render(request, 'addmed.html',{'medicines':medicines})