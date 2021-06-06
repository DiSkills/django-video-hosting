from django.contrib import admin

from .models import Category, Video, LikeOrDislike


class CategoryAdmin(admin.ModelAdmin):
    """ Category """

    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    fields = (('name', 'slug'),)


class VideoAdmin(admin.ModelAdmin):
    """ Video """

    list_display = ('category', 'title', 'slug', 'author', 'blocked', 'views', 'private', 'comments_on')
    search_fields = ('title', 'author__username', 'category__name')
    prepopulated_fields = {'slug': ('title',)}
    fields = (('category', 'author'), ('title', 'slug'), 'description', ('file', 'preview'),
              ('views', 'subscriptions_views'), ('blocked', 'private'), 'comments_on')
    list_editable = ('blocked', 'comments_on')


class LikeOrDislikeAdmin(admin.ModelAdmin):
    """ Like Or Dislike """

    list_display = ('video', 'user', 'vote')
    search_fields = ('video__title', 'user__username')
    fields = ('user', 'video', 'vote')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(LikeOrDislike, LikeOrDislikeAdmin)
