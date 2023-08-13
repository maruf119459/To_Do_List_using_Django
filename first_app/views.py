from django.shortcuts import redirect
from . import models
from . import forms
from django.views.generic import  ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    model = models.ToDoModel
    template_name = 'list_view.html'
    context_object_name = 'data'
    def get_queryset(self):
        queryset = super().get_queryset()
        for item in queryset:
            item.description = item.description[:50] + '...' 
        return queryset
    
class AddDoList(CreateView):
    model = models.ToDoModel
    template_name = 'add_do_list.html'
    form_class = forms.ToDoForm
    success_url = reverse_lazy('homepage')

class EditList(UpdateView):
    model = models.ToDoModel
    template_name = 'edit_do_list.html'
    form_class = forms.EditToDoForm
    success_url = reverse_lazy('homepage')
    
def delete_list(request, title):
     book = models.ToDoModel.objects.get(pk = title).delete()
     return redirect('homepage')
 
def complete_work(request, title):
     book = models.ToDoModel.objects.get(pk = title).delete()
     return redirect('homepage')
 
 
class ListDetailsView(DetailView):
    model = models.ToDoModel
    template_name = 'view_list_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'title'