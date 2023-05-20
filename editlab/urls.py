from django.urls import path
from .views import editlab

urlpatterns=[
    path('',editlab, name = 'editlab')
]