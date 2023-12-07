from django.urls import path,include
from . import views


#URLConf
urlpatterns = [
    path('index/view_week/<YY>/<MM>/<DD>/', views.index,name='index'),
    path('index/todo_page/create/', views.create_task, name='create_task'),
    path('index/todo_page/delete/<int:task_id>/<str:source>/', views.handle_task, name='delete_todo'),
    path('index/todo_page/save/<int:task_id>/<str:source>/', views.handle_task, name='Save_Changes'),
    path('index/todo_page/restore/<int:task_id>/<str:source>/', views.handle_task, name='Restore_Task'),
    path('index/todo_page/<str:src>/checked/<int:task_id>/', views.checked_done_todo, name='checked_done_todo'),
    path('index/todo_page/<str:src>/<int:task_id>/', views.get_task_data, name="get_task_data"),
    path('index/todo_page/AddNewList/<str:ListName>/<str:HashColor>/',views.AddNewList,name='AddNewList'),

    
    
    path('index/todo_page/Upcoming', views.view_upcoming_page, name="upcoming_page"),
    path('index/todo_page/Today', views.view_today_page, name='today_page'),
   
    path('index/todo_page/Calendar', views.view_calendar_page, name="calendar_page"),
    path('index/todo_page/StickyWall', views.view_stickywall_page, name="stickywall_page"),
    path('index/todo_page/RecycleBin', views.view_RecycleBin, name="RecycleBin_page"),

    
    path('index/todo_page/login_user', views.login_user, name="login_page" ),
    path('index/todo_page/logout_user', views.logout_user, name="logout_page" ),
    path('index/todo_page/register_user', views.register_user, name="register_user_page" ),
   
    path('index/todo_page/', include('django.contrib.auth.urls')),
    

    

]