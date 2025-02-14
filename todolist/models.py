from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField()
    time = models.DateTimeField()
    due_date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.title