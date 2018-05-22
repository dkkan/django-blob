from django.contrib import admin
from myapp.models import Post
from myapp.models import Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
