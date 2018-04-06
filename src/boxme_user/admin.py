"""Admin definition for BoxmeUser."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import BoxmeUserChangeForm, BoxmeUserCreationForm
from .models import BoxmeUser


class BoxmeUserAdmin(UserAdmin):

    """BoxmeUser Admin model."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }
    ),
    )

    # The forms to add and change user instances
    form = BoxmeUserChangeForm
    add_form = BoxmeUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


# Register the new BoxmeUserAdmin
admin.site.register(BoxmeUser, BoxmeUserAdmin)
