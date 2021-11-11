from django.contrib import admin

from .models import StartUp, Category, StartUpImage

admin.site.register(StartUp)
admin.site.register(Category)
admin.site.register(StartUpImage)
