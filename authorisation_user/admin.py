from django.contrib import admin

from .models import AdvUser


class UserAdmin(admin.ModelAdmin):
    """ User """

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'activated', 'send_messages')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = ('username', 'email', ('first_name', 'last_name'), ('about', 'avatar'), ('activated', 'send_messages'),
              'groups', 'user_permissions', ('is_staff', 'is_superuser', 'is_active'), ('last_login', 'date_joined'),
              'subscription', 'subscriber', 'history')
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(AdvUser, UserAdmin)
