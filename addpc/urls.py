from django.urls import path
from .views import addpc
urlpatterns = [
    path('', addpc , name='add pc')
]