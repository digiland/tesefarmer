from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


def upload_gallery_image(instance, filename):
    return 'images/{}/{}'.format(instance.post, filename)


class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images')
