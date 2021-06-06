from django.contrib import admin

from .models import AdvUser
from .send_mail import send_mail_about_activation


def send_mails_about_activation_for_users(model_admin, request, users):
    """ Action send mails about activation for users """

    for user in users:
        if not user.activated:
            send_mail_about_activation(user)
    model_admin.message_user(request, 'Requirement letters sent')


send_mails_about_activation_for_users.short_description = 'Sending activation requests'


class NonActivatedFilter(admin.SimpleListFilter):
    """ Filter users by activate """

    title = 'You activated?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Activated'),
            ('no_activated', 'No activated')
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(activated=True)
        elif val == 'no_activated':
            return queryset.filter(activated=False)


class UserAdmin(admin.ModelAdmin):
    """ User """

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'activated', 'send_messages')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = ('username', 'email', ('first_name', 'last_name'), ('about', 'avatar'), ('activated', 'send_messages'),
              'groups', 'user_permissions', ('is_staff', 'is_superuser', 'is_active'), ('last_login', 'date_joined'),
              'subscription', 'subscriber', 'history')
    readonly_fields = ('last_login', 'date_joined')
    list_filter = (NonActivatedFilter,)
    actions = (send_mails_about_activation_for_users,)


admin.site.register(AdvUser, UserAdmin)
