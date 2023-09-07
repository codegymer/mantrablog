from django.contrib import admin

# Register your models here.
# from django.contrib.auth.models import User

from .models import Post,Comment

admin.site.register(Post)
admin.site.register(Comment)
