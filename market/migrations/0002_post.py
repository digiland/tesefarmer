# Generated by Django 4.0 on 2022-02-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
    ]
