from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Schoolhtml(ListView):
    model=School
    context_object_name='schools'

class Schooldetails(DetailView):
    model=School
    context_object_name='sclobject'    

class Schoolcreate(CreateView):
    model=School
    fields='__all__'   


class Schoolupdate(UpdateView):
    model=School
    fields='__all__'   

class Schooldelete(DeleteView):
    model=School
    context_object_name='sclobject'
    success_url=reverse_lazy('Schoolhtml')
