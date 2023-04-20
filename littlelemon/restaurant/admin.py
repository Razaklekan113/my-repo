from django.contrib import admin

from .models import Booking, Menu

admin.site.register(Menu)
admin.site.register(Booking)