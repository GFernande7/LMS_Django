from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
     STATUS_CHOICES = [
          ('New', 'Новая'),
          ('In_progress', 'В работе'),
          ('Completed', 'Завершена'),
     ]
     project = models.ForeignKey(
          Project,
          related_name = 'tasks',
          on_delete = models.CASCADE,
     )
     name = models.CharField(max_length=100)
     description = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     assignee = models.ForeignKey(
          User,
          related_name = 'tasks',
          on_delete = models.SET_NULL,
          null = True,
          blank = True,
     )
     status = models.CharField(
          max_length = 50,
          choices = STATUS_CHOICES,
          default = 'New',
     )

     def __str__(self):
        return self.name