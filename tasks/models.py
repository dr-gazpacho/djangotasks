from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks_completed = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    
    def completed_tasks_count(self):
        return self.task_set.filter(is_complete=True).count()

# adding lots of methods in here to let User access Task
# from tasks: task = Task.objects.get(id=1)
# user = task.completed_by
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    date_deadline = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    completed_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,  # If a user is deleted, we don't delete the task
        related_name='completed_tasks',
        null=True,
        blank=True
    )

    def is_task_complete(self, user):
        """Mark task as complete by specified user"""
        self.is_complete = True
        self.completed_by = user
        self.date_completed = timezone.now()
        self.save()

    def __str__(self):
        return self.task_name

