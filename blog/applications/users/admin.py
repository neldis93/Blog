from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display=(
        'full_name',
        'id',
    )

    search_fields=('full_name',)

admin.site.register(User, UserAdmin)