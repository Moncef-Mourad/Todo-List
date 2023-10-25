from django.shortcuts import render,redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Todo
import datetime

# Create your views here.
#request -> response 
#request handler

def index(request):
    #Connect to the database
    all_todo_lists = Todo.objects.all()
    html = ''
    for task in all_todo_lists:
        url = '/index/todo_page/'+str(task.id)+'/'
        html+= '<a href="'+ url +'">Todo-List_'+ str(task.id) +'</a><br>'
    return HttpResponse(html)

def create_todo_page(request):
    if request.method == 'POST':
        task_txt = request.POST.get('task_Txt')
        date_created = request.POST.get('date')

        if task_txt:
            new_Task = Todo(task_Text=task_txt, date_created=date_created, isDone=False)
            new_Task.save()
            # Redirect to the same page after successful submission
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

    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # else:
    #     form = TodoForm(initial={'date_created': datetime.date.today()})  # Set the initial date

    # try:
    #     form = request.POST['task_Text','date_created','done',]
    #     return ''
    # except ():
    #     return ''
    # else:


    #     something.save()
        #Connect to the database