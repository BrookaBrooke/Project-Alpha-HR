from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from tasks.models import Task


# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        "name",
        "start_date",
        "due_date",
        "project",
        "assignee",
    ]
    template_name = "tasks/create.html"

    def form_valid(self, form):
        task = form.save(commit=False)
        task.owner = self.request.user
        task.save()
        form.save_m2m()
        return redirect("show_my_tasks", pk=task.id)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/show_my_tasks.html"
    task = Task.objects.all()
    context = {"task_list": task}

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]

    def get_success_url(self) -> str:
        return reverse_lazy("tasks/show_my_tasks")
