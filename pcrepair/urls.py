from django.urls import path
from .views import pcrepair

urlpatterns=[
    path('',pcrepair, name = 'pcrepair')
]
