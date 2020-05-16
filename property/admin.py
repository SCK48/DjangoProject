from django.contrib import admin

# Register your models here.
from property.models import Properties, Galeri, PropetyComment


class PropertiesAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'status']
    list_filter = ['user', 'status']
    prepopulated_fields = {'slug': ('title',)}

class GaleriAdmin(admin.ModelAdmin):
    list_display = ['title', 'property', 'image']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'property', 'user', 'status']
    list_filter = ['status']


admin.site.register(Properties, PropertiesAdmin)
admin.site.register(Galeri, GaleriAdmin)
admin.site.register(PropetyComment, CommentAdmin)