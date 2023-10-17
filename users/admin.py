from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        'consumer_category',
        'users_department'
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("consumer_category", "users_department")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("consumer_category", "users_department")}),)


admin.site.register(CustomUser, CustomUserAdmin)
