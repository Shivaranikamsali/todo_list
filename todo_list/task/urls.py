from django.urls import path
from task import views


urlpatterns = [
    path('',views.home,name='home'),
    path('edit/<int:id>/',views.task_update,name='update'),
    path('delete/<int:id>',views.task_delete,name='delete'),
    path('add_task',views.add_task,name='add_task'),
    path('all_task',views.all_task,name='all_task'),
    
]