from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Todo
from datetime import datetime, timedelta
from django.http import JsonResponse

# Create your views here.
#request -> response 
#request handler

def index(request,YY,MM,DD):
    date = YY+'-'+MM+'-'+DD
    # # Connect to the database
    tasks_ymd = Todo.objects.filter(date_created=date)
    # # Convert the date string to a datetime object
    date_object = datetime.strptime(date, '%Y-%m-%d')
    # # Get the day name
    day_name = date_object.strftime('%A')
    # # Get the month name
    month_name = date_object.strftime('%b')

    return render(request, 'view_week.html',{'day_name': day_name,'YY': YY,'MM':month_name,'DD':DD,'tasks_ymd': tasks_ymd,})    








def create_todo_page(request):
    if request.method == 'POST':
        task_txt = request.POST.get('task_Txt')
        date_created = request.POST.get('date')

        # Convert the form input to a datetime object
        date_created = datetime.strptime(date_created, '%Y-%m-%d')
        curr_date = datetime.now().date()
        # Check if the date inserted in the form page is less than the curr_date
        if task_txt and date_created.date() >= curr_date:
            new_Task = Todo(task_Text=task_txt, date_created=date_created, isDone=False)
            new_Task.save()
            # Redirect to the same page after successful submission
            return redirect(reverse('todo_page_create'))
        else:
            return redirect(reverse('todo_page_create'))
    all_tasks = Todo.objects.all() 
    return render(request, 'create_Todo-List.html',{'all_tasks': all_tasks})    


def delete_todo(request,task_id):
    if request.method == 'POST':
        # Use get_object_or_404 to get the specific Todo item
        task = get_object_or_404(Todo, id=task_id)
        # Delete the item
        task.delete()
    
    # After deletion, you can redirect to the same page or a different page as needed.
    return redirect('todo_page_create')


def checked_done_todo(request,task_id):
    if request.method == 'POST':
        # Use get_object_or_404 to get the specific Todo item
        task = get_object_or_404(Todo, id=task_id)
        # mark the checking box
        task.isDone= not task.isDone
        task.save()
    # After deletion, you can redirect to the same page or a different page as needed.
    return redirect('todo_page_create')





#URLS for the Html's 
def view_today_page(request):
     
    current_date = datetime.now().date()
    formatted_today = current_date.strftime('%b %d, %Y')
    today_tasks = Todo.objects.filter(due_date=current_date)

    
    return render(request, 'Today.html',{'today_tasks':today_tasks,'today':current_date})


def view_upcoming_page(request):

    current_date = datetime.now().date()
    next_day = current_date + timedelta(days=1)
    formatted_next_day = next_day.strftime('%b %d, %Y')
    upcoming_tasks = Todo.objects.filter(due_date=next_day)

    return render(request, 'Upcoming.html', {'upcoming_tasks':upcoming_tasks, 'next_day':formatted_next_day,})

def get_task_data(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    data = {
        'title': task.task_Text,
        'description': task.task_Descr,
        'list': task.task_List,
        'progress': task.task_Progress,
        'due_date': task.due_date,

    }
    return JsonResponse(data)



def view_calendar_page(request):
    return render(request, 'Calendar.html')

def view_stickywall_page(request):
    return render(request, 'StickyWall.html')
