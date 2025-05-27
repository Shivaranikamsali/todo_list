from django.db import models

# Create your models here.
class TodoList(models.Model):
    done=models.CharField()
    date=models.DateTimeField()
    description=models.CharField()
    status=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    
    
    def __str__(self):
        return self.done
