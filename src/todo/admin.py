from django.contrib import admin
from .models import Todo

admin.site.register(Todo)


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'done')
    list_filter = ('done',)
    search_fields = ('title',)
    ordering = ('title',)
