from django.urls import path
from .views import  index, ajax, search 

# from .views import search2
# search,
urlpatterns=[
    path('',search, name = 'search'),
    path('active/',ajax),
]