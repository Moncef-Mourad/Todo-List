from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import List,Todo,DeletedTask,ModificationHistory
from datetime import datetime, timedelta
from django.http import JsonResponse   
import json 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method =="POST":
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       if user is not None:
         login(request, user)
         return redirect('today_page')
        # Redirect to a success page.
        
       else:
        # Return an 'invalid login' error message.
         messages.success(request,("There was an error logging in ,try again"))
         return redirect('login_page')
    else:
      return render(request, 'authenticate/login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out "))
    return redirect('login_page')

def register_user(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("Registration Succesful !"))
            return redirect('today_page')
    else:
        form = UserCreationForm()
        
    return render(request,'authenticate/register_user.html',{'form':form,})
                       
        
     



# Create your views here.
#request -> response 
#request handler


def load_Lists():
    #Load The Available Lists
    Curr_Lists = List.objects.all()
    list_dict  = {}
    for list_obj in Curr_Lists:
        list_dict[list_obj.ListName] = list_obj.svgColor  
    return list_dict    



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

def create_task(request):
    if '/todo_page/create/' in request.path:
        curr_date = datetime.now().date()
        if request.method == 'POST':
            data = json.loads(request.body)
            txt = data.get('title')
            Descr = data.get('description')
            due_date = data.get('due_date')
            Progress = data.get('progress')
            listname = data.get('list')
            curr_URL = data.get('curr_url')
            print(txt)
            print(curr_URL)
            new_Task = Todo(task_Text=txt,task_Descr=Descr,due_date=due_date,task_Progress=Progress, date_created=curr_date)
            new_Task.task_List = List.objects.get(ListName=listname)
            new_Task.save()
    return JsonResponse({'message': 'Data received successfully!', 'redirect_url': curr_URL})
    

def delete_List(request, listName):
    if request.method == 'POST':
        list_wanted = get_object_or_404(List,ListName = listName)
        list_wanted.delete()
    return redirect('today_page')


def handle_task(request, task_id, source):
    task = get_object_or_404(Todo, id=task_id)
    # task_in_recycle = get_object_or_404(DeletedTask, original_task_id=task_id).original_task
    # Your logic for handling the task based on the source (e.g., delete or save changes)

        # Logic for delete
    if '/todo_page/delete/' in request.path:
        if source == 'RecycleBin':
            task.delete()
        elif source == 'Upcoming' or source == 'Today':
            task.is_in_recycle_bin = True
            task.save()
            DeletedTask.objects.create(original_task=task)
            # generate_notification("Task Delete Successfully!")
    elif '/todo_page/save/' in request.path:
        old_task_Text = task.task_Text
        old_task_Descr = task.task_Descr
        old_due_date = task.due_date
        old_task_Progress = task.task_Progress
        old_task_List = task.task_List.ListName

        # Logic for save changes
        if request.method == 'POST':
            data = json.loads(request.body)
            task.task_Text = data.get('title', task.task_Text)
            task.task_Descr = data.get('description', task.task_Descr)
            task.due_date = data.get('due_date', task.due_date)
            task.task_Progress = data.get('progress', task.task_Progress)
            task.task_List.ListName = data.get('list', task.task_List.ListName)
            print(task.task_List.ListName)
            print(task)
            
            # Save modifications to the ModificationHistory model
            modified_fields = {
                'task_Text': {
                    'old_value': old_task_Text,
                    'new_value': task.task_Text
                },'task_Descr': {
                    'old_value': old_task_Descr,
                    'new_value': task.task_Descr
                },'due_date': {
                    'old_value': str(old_due_date),
                    'new_value': task.due_date
                },'task_Progress': {
                    'old_value': old_task_Progress,
                    'new_value': task.task_Progress
                },'task_List': {
                    'old_value': old_task_List,
                    'new_value': task.task_List.ListName
                },
}
            print(modified_fields)
            task.save() 
            task.save_modifications(modified_fields)
            # Assuming 'todo_instance' is an instance of the Todo model
            modification_history = ModificationHistory.objects.filter(original_task=task)
            # Accessing modification dates for each record
            for modification_record in modification_history:
                print(modification_record.modification_date)


    elif '/todo_page/restore/' in request.path:
        if request.method == 'POST':
            task.is_in_recycle_bin = False
            task.save()    
            task_deleted = get_object_or_404(DeletedTask, pk=task_id)
            task_deleted.delete()




    # Redirect the user to the appropriate page based on the source
    if source == 'Upcoming':
        return JsonResponse({'message': 'Data received successfully!', 'redirect_url': reverse('upcoming_page')})
    elif source == 'Today':
        return JsonResponse({'message': 'Data received successfully!', 'redirect_url': reverse('today_page')})
    elif source == 'Calendar':
        return redirect('calendar_page')
    elif source =='RecycleBin':
        return JsonResponse({'message': 'Data restored successfully!', 'redirect_url': reverse('RecycleBin_page')})
    else:
        # Handle other cases or provide a default redirect
        return redirect('index')



def checked_done_todo(request,src,task_id):
        # Use get_object_or_404 to get the specific Todo item
    if src  == 'RecycleBin':
        task = get_object_or_404(DeletedTask, original_task_id=task_id).original_task
    elif src == 'Upcoming' or src=='Today':
        task = get_object_or_404(Todo, id=task_id)

    # mark the checking box
    task.isDone = not task.isDone
    task.save()
    # After deletion, you can redirect to the same page or a different page as needed.
    if src == 'Today':
        return JsonResponse({'message': 'Data received successfully!', 'redirect_url': reverse('today_page')})
    elif src == 'Upcoming':
        return JsonResponse({'message': 'Data received successfully!', 'redirect_url': reverse('upcoming_page')})
    elif src == 'RecycleBin':
        return JsonResponse({'message': 'Data received successfully!', 'redirect_url': reverse('RecycleBin_page')})




def AddNewList(request,NewListName,HashColor):

    List.objects.create(ListName=NewListName, svgColor=HashColor)
    return JsonResponse({'message': 'List Created successfully!'})





#URLS for the Html's 
def view_today_page(request):
    list_dict = load_Lists()
    modifications = ModificationHistory.objects.all().order_by('-modification_date')

    tasks_NotDone_NotInRecycleBin = 0
    tasks_Done_NotInRecycleBin = 0
    current_date = datetime.now().date()
    today_tasks = Todo.objects.filter(due_date=current_date)
    for task in today_tasks:
        if not task.isDone and not task.is_in_recycle_bin:
            tasks_NotDone_NotInRecycleBin+=1
        elif task.isDone and not task.is_in_recycle_bin:
            tasks_Done_NotInRecycleBin+=1      
    
    return render(request, 'Today.html',{'list_dict':list_dict,'modifications':modifications,'today_tasks':today_tasks,'today':current_date,'counter_notDone':tasks_NotDone_NotInRecycleBin,'counter_Done':tasks_Done_NotInRecycleBin})


def view_upcoming_page(request):
    list_dict = load_Lists()
    modifications = ModificationHistory.objects.all().order_by('-modification_date')

    tasks_NotDone_NotInRecycleBin=0
    tasks_Done_NotInRecycleBin=0
    current_date = datetime.now().date()
    next_day = current_date + timedelta(days=1)
    formatted_next_day = next_day.strftime('%b %d, %y')
    upcoming_tasks = Todo.objects.filter(due_date=next_day)
    for task in upcoming_tasks:
        if not task.isDone and not task.is_in_recycle_bin:
            tasks_NotDone_NotInRecycleBin+=1
        elif task.isDone and not task.is_in_recycle_bin:
            tasks_Done_NotInRecycleBin+=1


    return render(request, 'Upcoming.html', {'list_dict':list_dict,'modifications':modifications,'upcoming_tasks':upcoming_tasks, 'next_day':formatted_next_day,'counter_notDone':tasks_NotDone_NotInRecycleBin,'counter_done':tasks_Done_NotInRecycleBin})




def get_task_data(request, src,task_id):
    if not '/todo_page/RecycleBin' in request.path:
        task = get_object_or_404(Todo, id=task_id)
    else:
        task = get_object_or_404(DeletedTask, original_task_id=task_id).original_task
    data = {
        'title': task.task_Text,
        'description': task.task_Descr,
        'list': task.task_List.ListName,
        'progress': task.task_Progress,
        'due_date': task.due_date
    }
    return JsonResponse(data)



def view_calendar_page(request):
    list_dict = load_Lists()
    modifications = ModificationHistory.objects.all().order_by('-modification_date')

    return render(request, 'Calendar.html',{'list_dict':list_dict,'modifications':modifications,})

def view_stickywall_page(request):
    list_dict = load_Lists()
    modifications = ModificationHistory.objects.all().order_by('-modification_date')

    return render(request, 'StickyWall.html',{'list_dict':list_dict,'modifications':modifications,})

def view_RecycleBin(request):
    list_dict = load_Lists()
    modifications = ModificationHistory.objects.all().order_by('-modification_date')

    Recycled_Tasks = DeletedTask.objects.all()
    return render(request, 'RecycleBin.html',{'list_dict':list_dict,'modifications':modifications,'Recycled_Tasks':Recycled_Tasks})

def view_List(request, ListName):
    list_dict = load_Lists()
    modifications = ModificationHistory.objects.all().order_by('-modification_date')
    listObj = get_object_or_404(List,ListName=ListName)
    listTasks = Todo.objects.filter(task_List=listObj.ListName)

    return render(request, 'List.html', {'list_dict':list_dict,'modifications':modifications, 'List':listObj, 'listTasks':listTasks})



# other functionalities:


