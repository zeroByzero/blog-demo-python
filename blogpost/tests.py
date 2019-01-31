from django.test import TestCase

# Create your tests here.
from django.urls import resolve

from blogpost.views import index


class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        print(found)
        self.assertEqual(found.func, index)

