from django.urls import path
from .views import index

urlpatterns = [
    path('', index , name="all projects")
]
# 123.0.0.1:888/