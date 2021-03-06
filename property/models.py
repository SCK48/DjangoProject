from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, FileInput, Select , EmailInput
from django.urls import reverse
from django.utils.safestring import mark_safe

from product.models import Category


class Properties(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Confirmed', 'Confirmed'),
        ('Declined', 'Declined'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField(blank=True,)
    address = models.CharField(max_length=255)
    room = models.IntegerField(blank=True,)
    year = models.IntegerField(blank=True, )
    sqm = models.IntegerField(blank=True,)
    detail = RichTextUploadingField()
    slug = models.SlugField(null=True, unique=True)
    status = models.CharField(max_length=10, choices=STATUS,default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    #def image_tag(self):
    #return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    #image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class Galeri(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title



class PropertyForm(ModelForm):
    class Meta:
        model = Properties
        fields = [
            'category', 'title', 'keywords', 'description', 'image', 'price', 'address', 'room', 'year', 'sqm', 'detail'
        ]
        widgets = {
            'category': Select(attrs={'class': 'form-control', 'placeholder': 'category'}, ),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
            'price': TextInput(attrs={'class': 'form-control', 'placeholder': 'price'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'room': TextInput(attrs={'class': 'form-control', 'placeholder': 'room'}),
            'year': TextInput(attrs={'class': 'form-control', 'placeholder': 'year'}),
            'sqm': TextInput(attrs={'class': 'form-control', 'placeholder': 'sqm'}),
            'detail': CKEditorWidget(),

        }

class PropetyComment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class GaleriForm(ModelForm):
    class Meta:
        model = Galeri
        fields = ['title', 'image']