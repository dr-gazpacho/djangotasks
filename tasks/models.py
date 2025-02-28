from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=200)
    tasks_completed = models.IntegerField(default=0)

class Tasks(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField()
    date_completed = models.DateTimeField()
    date_deadline = models.DateTimeField()
    is_complete = models.BooleanField()
    completed_by = models.ForeignKey(Users)

