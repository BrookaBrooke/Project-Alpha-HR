from django.test import TestCase, Client
from django.urls import reverse


class FeatureTests(TestCase):
    def test_root_path_redirects_to_projects(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(
            response.status_code,
            302,
            msg="Did not get a redirect",
        )
        self.assertTrue(
            response.has_header("Location"),
            msg="Response does not redirect to a new URL",
        )
        location = response.headers.get("Location")
        if not location.startswith("/accounts/login/"):
            self.assertEqual(
                location,
                "/projects/",
                msg="Redirection does not point to /projects/",
            )

    def test_root_resolves_from_home(self):
        path = reverse("home")
        self.assertEqual(
            path,
            "/",
            msg="'home' path does not resolve to root",
        )
