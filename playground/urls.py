from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('view_week/<YY>/<MM>/<DD>/', views.index,name='index'),
    path('todo_page/create/', views.create_todo_page, name='todo_page_create'),
    path('todo_page/delete/<int:task_id>/<str:source>/', views.handle_task, name='delete_todo'),
    path('todo_page/save/<int:task_id>/<str:source>/', views.handle_task, name='Save_Changes'),
    path('todo_page/checked/<task_id>/', views.checked_done_todo, name='checked_done_todo'),
    path('todo_page/Upcoming', views.view_upcoming_page, name="upcoming_page"),
    path('todo_page/Upcoming/<task_id>/', views.get_task_data, name="get_task_data"),
    path('todo_page/Today', views.view_today_page, name='today_page'),
    path('todo_page/Calendar', views.view_calendar_page, name="calendar_page"),
    path('todo_page/StickyWall', views.view_stickywall_page, name="stickywall_page")

]