from django import forms
from . import models

class ToDoForm(forms.ModelForm):
    class Meta:
        model = models.ToDoModel
        fields = ['title', 'description']
        
class EditToDoForm(forms.ModelForm):
    class Meta:
        model = models.ToDoModel
        fields = ['title','description'] 
        widgets ={
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
        }