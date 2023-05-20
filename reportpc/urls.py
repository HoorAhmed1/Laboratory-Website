from django.urls import path
from .views import reportpc

urlpatterns=[
    path('',reportpc, name = 'reportpc')
]
