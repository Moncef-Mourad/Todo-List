from django.db import models

# Create your models here.

class Todo(models.Model):
    #id
    date_created = models.DateField()
    task_Text = models.CharField(max_length=250) 
    isDone = models.BooleanField(default=False)

    def __str__(self):
        if self.isDone:
            DoneTxt = 'Task Done.'
        else:
            DoneTxt = 'Task Not Done Yet.'

        return str(self.id) + '    ||    ' + self.task_Text + '    ||    ' + DoneTxt + '    ||    ' + str(self.date_created)

