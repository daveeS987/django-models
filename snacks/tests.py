from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Snack


class SnacksModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", email="tester@gmail.com", password="pass")
        self.new_snack = Snack.objects.create(name="Cheetos", description="cheesy", purchaser=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.new_snack), "Cheetos")

    def test_snack_name(self):
        self.assertEqual(self.new_snack.name, "Cheetos")


class SnackListViewTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")
