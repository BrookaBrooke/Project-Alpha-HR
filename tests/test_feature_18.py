from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .utils import Document
from projects.models import Project


class FeatureTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.noor_credentials = {"username": "noor", "password": "1234abcd."}
        self.noor = User.objects.create_user(**self.noor_credentials)
        self.alisha = User.objects.create_user(
            username="alisha", password="1234abcd."
        )
        self.client.post(reverse("login"), self.noor_credentials)
        self.project = Project.objects.create(
            name="ZZZZZZ", description="AAAAA\n\nBBBBB"
        )
        self.project.members.add(self.noor)

    def test_project_description_has_multiple_paragraphs(self):
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        paragraphs = html.get_all_children("p")
        has_aaaaa = False
        has_bbbbb = False
        for p in paragraphs:
            if "AAAAA" in p.inner_text():
                has_aaaaa = True
            elif "BBBBB" in p.inner_text():
                has_bbbbb = True
        self.assertTrue(
            has_aaaaa and has_bbbbb,
            msg="Did not find a markdownified section for description",
        )
