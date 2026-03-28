from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'subscription']
    list_filter = ['id', 'username', 'email', 'subscription']
    search_fields = ['username', 'subscription']
