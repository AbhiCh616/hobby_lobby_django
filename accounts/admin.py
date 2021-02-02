from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import User
from accounts.forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # Fields to display the list page
    list_display = ('email', 'is_admin', 'is_staff')
    list_filter = ('is_admin',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    # Fields to display the details page
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_admin',),})
    )
    # Fields to use when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_admin', 'password1', 'password2'),
            }
        ),
    )

# Register new UserAdmin
admin.site.register(User, UserAdmin)

# Unregister Group model from admin
admin.site.unregister(Group)