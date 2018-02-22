from django.contrib import admin

from .models import User, Content


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Content)
class Content(admin.ModelAdmin):
    pass
