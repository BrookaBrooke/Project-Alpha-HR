from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from projects.models import Project


# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/projects.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/show_project.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ["name", "description", "members"]
    template_name = "projects/create.html"
