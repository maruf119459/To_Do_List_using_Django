from django.contrib import admin
from . import models
# Register your models here.


#admin.site.register(BookStoreModel)

class ToDoModelAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    
admin.site.register(models.ToDoModel, ToDoModelAdmin)