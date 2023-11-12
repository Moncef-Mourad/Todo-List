from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Todo
from datetime import datetime, timedelta
from django.http import JsonResponse   
import json 

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


def handle_task(request, task_id, source):
    task = get_object_or_404(Todo, id=task_id)
    
    # Your logic for handling the task based on the source (e.g., delete or save changes)
    if '/todo_page/delete/' in request.path:
        # Logic for delete
        task.delete()
        # generate_notification("Task Delete Successfully!")
    elif '/todo_page/save/' in request.path:
        # Logic for save changes
        if request.method == 'POST':
            data = json.loads(request.body)
            task.task_Text = data.get('title', task.task_Text)
            task.task_Descr = data.get('description', task.task_Descr)
            task.due_date = data.get('due_date', task.due_date)
            task.task_Progress = data.get('progress', task.task_Progress)
            task.task_List = data.get('list', task.task_List)
            task.save()

    # Redirect the user to the appropriate page based on the source
    if source == 'upcoming':
        return JsonResponse({'message': 'Data received successfully!', 'redirect_url': reverse('upcoming_page')})
        # return redirect(reverse('upcoming_page'))
    elif source == 'today':
        return redirect('today_tasks_url_name')
    elif source == 'calendar':
        return redirect('today_page')
    else:
        # Handle other cases or provide a default redirect
        return redirect('index')



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

def view_today_page(request):
    return render(request, 'Today.html')

def view_calendar_page(request):
    return render(request, 'Calendar.html')

def view_stickywall_page(request):
    return render(request, 'StickyWall.html')






# other functionalities:


