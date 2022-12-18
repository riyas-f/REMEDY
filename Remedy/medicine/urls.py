from django.urls import path
from . import views

urlpatterns = [
    path('addmed/',views.addmed, name='addmed')
]
