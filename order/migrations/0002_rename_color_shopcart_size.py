# Generated by Django 3.2.4 on 2021-06-23 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopcart',
            old_name='color',
            new_name='size',
        ),
    ]
