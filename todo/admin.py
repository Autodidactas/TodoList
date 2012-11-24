from django.contrib import admin
from todo.models import Todo, TodoArticulo

class TodoArticuloAdmin(admin.TabularInline):
	model = TodoArticulo
	extra = 1

class TodoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)
	search_fields = ['nombre']
	inlines = [TodoArticuloAdmin]

admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoArticulo)