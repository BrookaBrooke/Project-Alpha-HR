from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
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


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/show_my_tasks.html"
    task = Task.objects.all()
    context = {"task_list": task}

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)
