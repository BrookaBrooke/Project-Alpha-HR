from django.urls import path, reverse_lazy
from tasks.views import TaskCreateView, TaskListView, TaskUpdateView
from django.views.generic.base import RedirectView

urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
    path("<int:pk>/complete", TaskCreateView.as_view(), name="complete_task"),
]
