from django.forms import ModelForm
from todo.models import Todo, TodoArticulo

class TodoForm(ModelForm):
	class Meta:
		model = Todo

class TodoArticuloForm(ModelForm):
	class Meta:
		model = TodoArticulo
		exclude = ('fktodo',)
