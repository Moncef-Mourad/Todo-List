from django.db import models

# Create your models here.

class Todo(models.Model):
    #id
    date_created = models.DateField()
    due_date = models.DateField(default='0000-00-00')   
    task_Text = models.CharField(max_length=50) 
    task_Descr = models.CharField(default='Default Decr',max_length=150)
    task_List = models.CharField(default='Default List', max_length=10) 
    task_Progress = models.CharField(default='Incomplete',max_length=15)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + '    ||    ' + self.task_Text + '    ||    ' + 'Descr...' + '    ||    ' + self.task_List + '    ||    ' + self.task_Progress + '    ||    Date Created:' + str(self.date_created) + '    ||    Due Date:' + str(self.due_date)

