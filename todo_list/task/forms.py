from django import forms
from task.models import TodoList
from datetime import datetime

class TaskForm(forms.ModelForm):
    class Meta:
        model=TodoList
        fields='__all__'
        labels ={
            'done':'Task to be done?',
            'date':'Due-date' ,
            'description': 'Description about task',
            'status':'Status(Pending/completed)',
            'image': 'Image',
        }
        widgets = {
            'done':forms.TextInput(attrs={
                'type':'Text',
                'placeholder':'Enter the task name',
                }),
            'date':forms.DateTimeInput(attrs={
                'type':'datetime-local',
                'min': datetime.now().strftime("%Y-%m-%dT%H:%M"),
            }),
            
            
        }
        
        
        
        