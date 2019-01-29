from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import Account


class AccountAdmin(UserAdmin):
    model = get_user_model()
    add_form = AccountCreationForm
    form = AccountChangeForm

    list_display = ('email', 'first_name', 'last_name', 'username')
    list_filter = ('stream', 'course', 'gender')
    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Credentials', {'fields': ('password',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ('Credentials', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
        ('Personal Info', {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'dob', 'gender', 'phn_num')}
         ),
        ('Academic Info', {
            'fields': ('reg_num', 'stream', 'course')
        }),
        ('Permissions', {
            'fields': ('is_cr', 'is_faculty', 'is_superuser', 'is_staff', 'is_active',)}),
    )

    search_fields = ('email', 'username', 'reg_num')
    ordering = ('reg_num',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
