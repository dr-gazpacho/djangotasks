from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="tasks_list"),
    path("delete/<int:task_id>/", views.delete, name="delete_task"),
    path("complete/<int:task_id>/", views.complete, name="complete_task"),
    path("api/", views.api, name="api")
]