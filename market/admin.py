from django.contrib import admin

# Register your models here.
from . models import User, UserProfile, Post, Image


class ImageInline(admin.TabularInline):
    model = Image


admin.site.register(User)
admin.site.register(UserProfile)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
