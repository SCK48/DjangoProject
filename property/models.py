from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
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
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    #def image_tag(self):
        #return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    #image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class PropertyForm(ModelForm):
    class Meta:
        model = Properties
        fields = [#'category',
                  'title', 'keywords', 'description', 'image', 'price', 'address', 'room', 'year', 'sqm', 'detail']
