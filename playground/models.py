from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ListName = models.CharField(default='Personal',max_length=10)
    svgColor = models.CharField(default='black',max_length=10)
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    due_date = models.DateField(default='0000-00-00')   
    task_Text = models.CharField(max_length=50) 
    task_Descr = models.CharField(default='Default Decription',max_length=150)
    task_List = models.ForeignKey(List,to_field='id',on_delete=models.CASCADE)
    task_Progress = models.CharField(default='Incomplete',max_length=15)
    isDone = models.BooleanField(default=False)

    #Pour la corbeille et la modification des Taches:
    is_in_recycle_bin = models.BooleanField(default=False)
    def save_modifications(self, modified_fields,user_):
        ModificationHistory.objects.create(user =user_,
            original_task=self,
            modified_fields=modified_fields
        )  
    def save(self, *args, **kwargs):
        # Your custom logic goes here
        if self.isDone:
            self.task_Progress = 'Done'
        else:
            self.task_Progress='Incomplete'  

        list_instance, created = List.objects.get_or_create(user=self.user, ListName=self.task_List.ListName)
        self.task_List = list_instance      
        # Call the original save method to save the object
        super(Todo, self).save(*args, **kwargs)   

    def __str__(self):
        return str(self.id) + '    ||    ' + self.task_Text + '    ||    ' + 'Descr...' + '    ||    ' + self.task_List.ListName + '    ||    ' + self.task_Progress + '    ||    Date Created:' + str(self.date_created) + '    ||    Due Date:' + str(self.due_date)



# Recycle Bin:

class DeletedTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_task = models.OneToOneField(Todo, on_delete=models.CASCADE, primary_key=True, related_name='deleted_task')

    deletion_date = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Before deleting, set is_in_recycle_bin to False in the corresponding Todo model
        self.original_task.is_in_recycle_bin = False
        self.original_task.save()
        super().delete(*args, **kwargs)


class ModificationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_task = models.ForeignKey(Todo, on_delete=models.CASCADE)
    modified_fields = models.JSONField()
    modification_date = models.DateTimeField(auto_now_add=True)
