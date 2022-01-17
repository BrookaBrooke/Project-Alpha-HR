from django.contrib import admin
from django.test import TestCase


class FeatureTests(TestCase):
    def test_project_registered_with_admin(self):
        try:
            from projects.models import Project

            self.assertTrue(
                admin.site.is_registered(Project),
                msg="projects.models.Project is not registered with the admin",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'projects.models'")
        except ImportError:
            self.fail("Could not find 'projects.models.Project'")
