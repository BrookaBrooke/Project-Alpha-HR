from django.urls import path

from projects.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("", ProjectDetailView.as_view(), name="show_project"),
]
