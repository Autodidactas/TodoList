# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Todo(models.Model):
	nombre = models.CharField('Nombre', 
							   max_length=200,
							   help_text='Ingrese el nombre del proyecto'

							  )

	def __unicode__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',)

class TodoArticulo(models.Model):
	fktodo = models.ForeignKey(Todo)
	tarea = models.TextField('Tareas', help_text='Descripción de la tarea')
	fecha = models.DateField()

	def __unicode__(self):
		return u'%s | %s ' % (self.fktodo, self.tarea)

	class Meta:
		verbose_name=u'Todo Tarea'
		verbose_name_plural = 'Todo Tareas'
 
     