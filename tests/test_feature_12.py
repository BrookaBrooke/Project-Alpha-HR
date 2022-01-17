from django.contrib import admin
from django.test import TestCase


class FeatureTests(TestCase):
    def test_project_registered_with_admin(self):
        try:
            from tasks.models import Task

            self.assertTrue(
                admin.site.is_registered(Task),
                msg="tasks.models.Task is not registered with the admin",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models'")
        except ImportError:
            self.fail("Could not find 'tasks.models.Task'")
