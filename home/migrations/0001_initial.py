# Generated by Django 3.2.4 on 2021-06-17 14:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('manufacturers', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('cart_icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('menu_icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('bannertext', models.CharField(max_length=300)),
            ],
        ),
    ]
