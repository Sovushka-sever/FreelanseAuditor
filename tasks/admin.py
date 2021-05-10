from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'responsable', 'date_created', 'date_completion', 'status', 'price')
    search_fields = ('author',)
    list_filter = ('responsable', 'author', 'status')
    empty_value_display = '-пусто-'
    fieldsets = (
        (None, {'fields': ('author', 'responsable')}),
        (
            'Информация о заказе',
            {
                'fields': (
                    'title',
                    'content',
                    'status',
                    'price',
                ),
            },
        ),
    )
