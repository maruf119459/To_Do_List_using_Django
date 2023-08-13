from django.urls import path
from .  import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('add_do_list/', views.AddDoList.as_view(), name='add_do_list') , 
    path('edit_list/<str:pk>', views.EditList.as_view(), name='edit_list') , 
    path('delete_list/<str:title>', views.delete_list, name='delete_list') ,
    path('complete_work/<str:title>', views.complete_work, name='complete_work') ,
    path('list_details/<str:title>', views.ListDetailsView.as_view(), name='list_details') ,
]