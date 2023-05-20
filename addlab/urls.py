from django.urls import path
from .views import addlab
urlpatterns = [
    path('', addlab , name='add lab')
]
