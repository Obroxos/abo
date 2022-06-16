#Permite crear, actualizar y editar modelos.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Permite listar modelos.
from django.views.generic.list import ListView
#Permite ver modelos en detalle.
from django.views.generic.detail import DetailView
#Permite hacer render de páginas.
from django.shortcuts import render, HttpResponse, redirect
#Importa modelos
from .models import Proceso
from django.contrib.auth import login
from django.contrib import messages


def perfil(request):
	return render(request, 'core/admin_perfil.html')

class LandingView(ListView):
	model = Proceso
	template_name = 'core/static_landing.html'

def ley(request):
	return render(request, 'core/static_ley.html')

def asambleas(request):
	return render(request, 'core/static_asambleas.html')

class ProcesoCreate(CreateView):
	model = Proceso
	fields = ['title', 'subtitle', 'content', 'video', 'image', 'author']
	template_name = 'core/admin_procesos_crear.html'
	success_url ="/admin/procesos"

class ProcesoUpdateView(UpdateView):
	model = Proceso
	fields = ['title', 'subtitle', 'content', 'video',  'image', 'author']
	template_name = 'core/admin_procesos_crear.html'
	success_url ="/admin/procesos"

class ProcesoDeleteView(DeleteView):
	model = Proceso
	template_name = 'core/admin_procesos_eliminar.html'
	success_url ="/admin/procesos"

class ProcesoListView(ListView):
	model = Proceso

class ProcesoDetailView(DetailView):
	model = Proceso

