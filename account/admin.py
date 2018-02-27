from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
from register.forms import UserCreationForm


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(UA):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'pass1', 'pass2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
