from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from medicine.models import SavedMedicines, MedicineRecord
# Create your views here.

@login_required(login_url='/login')
def home(request):

    medicines = SavedMedicines.objects.all().order_by('medicine_name')
    descs= MedicineRecord.objects.all().order_by('medicine_name')
    return render(request, 'home.html', {'medicines' : medicines, 'descs' : descs})