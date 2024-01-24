# tests.py in your app folder (e.g., Q2/tests.py)
from django.test import RequestFactory
from django.urls import reverse
from django.test import TestCase
from Q2.views import greet_user

class GreetUserViewTests(TestCase):

    def run_test(self, test_name, func):
        try:
            func()
            print(f"Passed {test_name}")
        except AssertionError:
            print(f"Failed {test_name}")

    def test_greet_user_default_name(self):
        self.run_test("test_greet_user_default_name", lambda: self.assertContains(greet_user(RequestFactory().get(reverse('greet_user'))), 'Guest', status_code=200))

    def test_greet_user_custom_name(self):
        self.run_test("test_greet_user_custom_name", lambda: self.assertContains(greet_user(RequestFactory().get(reverse('greet_user') + '?name=John')), 'John', status_code=200))

    def test_greet_user_template_used(self):
        self.run_test("test_greet_user_template_used", lambda: self.assertContains(greet_user(RequestFactory().get(reverse('greet_user'))), 'Hello, Guest!', status_code=200))

    def test_greet_user_empty_name(self):
        self.run_test("test_greet_user_empty_name", lambda: self.assertContains(greet_user(RequestFactory().get(reverse('greet_user') + '?name=')), '', status_code=200))

    def test_greet_user_long_name(self):
        long_name = 'X' * 100
        self.run_test("test_greet_user_long_name", lambda: self.assertContains(greet_user(RequestFactory().get(reverse('greet_user') + f'?name={long_name}')), long_name, status_code=200))
