from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Todo
from datetime import datetime

# Create your views here.
#request -> response 
#request handler

def index(request,YY,MM,DD):
    # #Connect to the database
    # all_todo_lists = Todo.objects.all()
    # html = ''
    # for task in all_todo_lists:
    #     url = '/index/todo_page/'+str(task.id)+'/'
    #     html+= '<a href="'+ url +'">Todo-List_'+ str(task.id) +'</a><br>'
    # return HttpResponse(html)

    # Connect to the database
    html =''
    date = YY+'-'+MM+'-'+DD
    tasks_ymd = Todo.objects.filter(date_created=date)
    # Convert the date string to a datetime object
    date_object = datetime.strptime(date, '%Y-%m-%d')
    # Get the day name
    day_name = date_object.strftime('%A')
    html+='<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>'
    html +='<p><b>'+day_name+'</b> ,'+date+'</p><br>'
    html += '<div class="date-picker"><button id="calendar-button">Select Date</button><input type="date" id="date-input" style="display: none;"></div>'
        
    for tasks_ymd_txt in tasks_ymd:
        html += '<p>'+ tasks_ymd_txt.task_Text +'</p><br>'
    html+='<script>$(function() {$("#calendar-button").click(function() {$("#date-input").datepicker("show");});});</script>'    
    return HttpResponse(html)







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





def view_todo_page(request,task_id):
    #Connect to the database
    task_id_text = Todo.objects.get(id=task_id).task_Text
    return render(request, 'view_Todo-List.html', {'task_id': str(task_id), 'task_Text': task_id_text})
