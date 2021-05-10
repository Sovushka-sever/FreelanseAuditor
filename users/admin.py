from django.contrib import admin
from users.model import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'role', 'rating', )
    search_fields = ('role',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'
    fieldsets = (
        (None, {'fields': ('username', 'role',)}),
        (
            'Информация и фото',
            {
                'fields': (
                    'avatar',
                    'bio',
                    'program_language',
                ),
            },
        ),
    )
