from django.contrib import admin

# Register your models here.
from property.models import Properties
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'status']
    list_filter = ['user', 'status']

admin.site.register(Properties,PropertiesAdmin)