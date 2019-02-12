from django.contrib import admin

from .models import order, supply

# Register your models here.

admin.site.register(order)
admin.site.register(supply)
