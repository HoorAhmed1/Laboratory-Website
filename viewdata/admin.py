from django.contrib import admin
from .models import  Laboratory, BrokenPC, Device
# , BrokenPC

# Register your models here.
admin.site.register(Laboratory)
# admin.site.register(Computer)
admin.site.register(BrokenPC)
admin.site.register(Device)