from django.forms import ModelForm
from todo.models import *

class TodoForm(ModelForm):
	class Meta:
		model = Todo

