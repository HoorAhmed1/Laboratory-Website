"""backendProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('homepage.urls')),
    path('',include('all_projects.urls')),
    path('addpc/',include('addpc.urls')),
    path('addlab/', include('addlab.urls')),
    path('reportpc/', include('reportpc.urls')),
    path('pcrepair/', include('pcrepair.urls')),
    path('search/', include('search.urls')),
    path('editlab/', include('editlab.urls')),
    path('viewdata/', include('viewdata.urls'))
    
    #http://127.0.0.1:8000/
    #http://127.0.0.1:8000/homepage/
]