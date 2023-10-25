from django import forms
from .models import Todo
import datetime

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_Text', 'isCompleted', 'date_created']
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_created(self):
        date_created = self.cleaned_data['date_created']
        today = datetime.date.today()
        print(today)
        if date_created < today:
            raise forms.ValidationError("The selected date cannot be earlier than today.")
        
        return date_created
