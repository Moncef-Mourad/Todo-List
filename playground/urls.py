from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('view_week/<YY>/<MM>/<DD>/', views.index,name='index'),
    path('todo_page/create/', views.create_todo_page, name='todo_page_create'),
    path('todo_page/delete/<task_id>/', views.delete_todo, name='delete_todo'),
    path('todo_page/checked/<task_id>/', views.checked_done_todo, name='checked_done_todo'),
    path('todo_page/Upcoming', views.view_upcoming_page, name="upcoming_page"),
    path('todo_page/Today', views.view_today_page, name='today_page'),
    path('todo_page/Calendar', views.view_calendar_page, name="calendar_page"),
    path('todo_page/StickyWall', views.view_stickywall_page, name="stickywall_page")

]