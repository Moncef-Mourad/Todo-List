from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.index,name='index'),
    path('todo_page/create/', views.create_todo_page, name='todo_page_create'),
    path('todo_page/delete/<task_id>/', views.delete_todo, name='delete_todo'),
    path('todo_page/checked/<task_id>/', views.checked_done_todo, name='checked_done_todo'),
    path('todo_page/<task_id>/', views.view_todo_page, name='todo_page_view'),

]