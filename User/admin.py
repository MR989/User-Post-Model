from django.contrib import admin

# Register your models here.
from .models import User1,Post
admin.site.register(User1)
admin.site.register(Post)