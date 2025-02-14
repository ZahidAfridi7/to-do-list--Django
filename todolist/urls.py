from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mark_completed/<int:id>', views.mark_completed, name='mark_completed'),
    path('delete_task/<int:id>',views.delete_task,name='delete_task'),
    path('add_task',views.add_task,name="add_task"),
    path('edit_task/<int:id>',views.edit_task,name='edit_task'),
] 