from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from tasks.models import Task

# Create your views here.


class TaskCreateView(CreateView):
    model = Task
    fields = [
        "name",
        "start_date",
        "due_date",
        "project",
        "assignee",
    ]
    template_name = "tasks/create.html"
    success_url = reverse_lazy("projects/show_project.html")

    def get_queryset(self):
        return Task.objects.filter(members=self.request.user)
