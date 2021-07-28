from django.db import models
from django.forms import Textarea, TextInput
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Profile(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=100)
    keywords= models.CharField(max_length=225)
    description = models.CharField(max_length=225, null=True)
    company = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    icon = models.ImageField(blank=True, null=True, upload_to='images/')
    logo = models.ImageField(blank=True, null=True, upload_to='images/')
    cart_icon = models.ImageField(blank=True, null=True, upload_to='images/')
    menu_icon = models.ImageField(blank=True, null=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    about = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    bannertext= models.CharField(max_length=300)

    def __str__ (self):
        return self.title


class Manufacturers(models.Model):
    title = models.CharField(max_length=10, blank=True, null=True)
    manufacturers = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.title
     
