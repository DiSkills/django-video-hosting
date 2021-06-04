from django.contrib import admin

from .models import Category, Video, LikeOrDislike


admin.site.register(Category)
admin.site.register(Video)
admin.site.register(LikeOrDislike)
