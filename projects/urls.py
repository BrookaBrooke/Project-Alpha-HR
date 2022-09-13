from django.urls import path

from projects.views import ProjectListView

urlpatterns = [path("", ProjectListView.as_view(), name="list_projects")]
