from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone
from .constants import task_status_choices, task_priority_choices

class Task(models.Model):
    '''
    Creating a model for Tasks which contains:
        - user (Foreign key relationship)
        - name
        - description
        - status
        - created_on
        - deadline
        - completed_on
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Task Name', max_length=200)
    description = models.CharField('Description', max_length=1024)
    status = models.CharField('Status', choices=task_status_choices, max_length=40)
    priority = models.CharField('Priority', choices=task_priority_choices, max_length=20)
    github_link = models.CharField('GitHub Link', max_length=200, blank=True, null=True)
    created_on = models.DateTimeField('Created On', default=timezone.now)
    deadline = models.DateTimeField('Deadline', blank=True, null=True)
    completed_on = models.DateTimeField('Completed On', blank=True, null=True)

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return f'{self.name}'