from django.http import HttpRequest
from django.test import TestCase, LiveServerTestCase

# Create your tests here.
from django.urls import resolve
from django.utils.datetime_safe import datetime

from blogpost.models import Blogpost
from blogpost.views import index, view_post
from selenium import webdriver
from pyvirtualdisplay import Display


'''
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        print(found)
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn(b'<title>Welcome to my blog</title>', response.content)
'''

'''
class BlogpostTest(TestCase):
    def test_blogpost_url_resolve_to_blog_post_view(self):
        found = resolve('blog/this_is_a_test.html')
        self.assertEqual(found.func, view_post)

    def test_blogpost_create_with_view(self):
        Blogpost.objects.create(title='hello', author='admin', slug='this_is_a_test', body='This is a Blog',
                                posted='datetime.now')
        response = self.client.get('/blog/this_is_a_test.html')
        self.assertIn(b'This is a blog', response.content)
'''


class HomepageTestCase(LiveServerTestCase):
    def setUp(self):
        Blogpost.objects.create(
            title='hello',
            author='admin',
            slug='this_is_a_test',
            body='This is a blog',
            posted=datetime.now
        )
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()

        # self.selenium = webdriver.Firefox()
        # self.selenium.maximize_window()
        super(HomepageTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        self.display.stop()
        super(HomepageTestCase, self).tearDown()

    def test_visit_blog_post(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/")
        )

        self.selenium.find_element_by_link_text("hello").click()
        self.assertIn("hello", self.selenium.title)

