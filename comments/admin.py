from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    """ Comment """

    list_display = ('id', 'user', 'video', 'parent', 'is_child', 'timestamp')
    list_display_links = ('id', 'user')
    search_fields = ('user__username', 'video__title')
    fields = (('user', 'video'), 'text', ('parent', 'is_child'))


admin.site.register(Comment, CommentAdmin)
