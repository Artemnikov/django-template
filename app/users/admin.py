from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "avatar",
        "is_staff",
        "is_active",
        "is_superuser",
        "last_login",
        "date_joined",
    )

# Register your models here.
admin.site.register(User, UserAdmin)
