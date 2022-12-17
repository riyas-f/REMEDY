from django.shortcuts import render,redirect


# Create your views here.
def tips(request):
    return render(request, 'tips.html')