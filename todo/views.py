# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from todo.models import Todo
from todo.forms import TodoForm, TodoArticuloForm
from django.forms.formsets import formset_factory, BaseFormSet

def index(request):

	# See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
	class RequiredFormSet(BaseFormSet):
		def __init__(self, *args, **kwargs):
			super(RequiredFormSet, self).__init__(*args, **kwargs)
			for form in self.forms:
				form.empty_permitted = False

	#si se fija aca le puse extra 3 para que me pinte 3 formularios de tareas al mismo tiempo
	#si se lo quito pues pone solo uno prueben 
	TodoArticuloFormSet = formset_factory(TodoArticuloForm, extra=3, max_num=10, formset=RequiredFormSet)
	

	if request.method == 'POST':

		todo_form = TodoForm(request.POST)
		todo_articulo_formset = TodoArticuloFormSet(request.POST, request.FILES)

		if todo_form.is_valid() and todo_articulo_formset.is_valid():
			todo_lista = todo_form.save()
			for form in todo_articulo_formset.forms:
				todo_item = form.save(commit=False)
				todo_item.fktodo = todo_lista
				todo_item.save()

			return HttpResponseRedirect('/')
	else:
		todo_form = TodoForm()
		todo_articulo_formset = TodoArticuloFormSet()

	todo = Todo.objects.all().order_by('id') #Select * from Todo ;
	return  render_to_response('index.html', locals(),
								RequestContext(request))

def ver_detalle(request, id):
	ver = get_object_or_404(Todo, id=id)
	return render_to_response('todo/ver.html', {'ver': ver},
								RequestContext(request))
