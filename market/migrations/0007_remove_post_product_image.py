# Generated by Django 4.0 on 2022-02-02 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_rename_product_name_image_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='product_image',
        ),
    ]
