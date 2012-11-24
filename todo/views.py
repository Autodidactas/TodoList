# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from todo.models import Todo, TodoArticulo
from todo.forms import *

def index(request):

	if request.method == 'POST':
		todo_form = TodoForm(request.POST)
		if todo_form.is_valid():
			todo_form.save()
			return HttpResponseRedirect('/')
	else:
		todo_form = TodoForm()

	todo = Todo.objects.all().order_by('id') #Select * from Todo ;
	return  render_to_response('index.html',
		                       RequestContext(request, locals()))

def ver_detalle(request, id):
	ver = get_object_or_404(Todo, id=id)
	return render_to_response('todo/ver.html',
		                      RequestContext(request, locals()))
