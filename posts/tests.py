from django.test import TestCase
from .models import Posts
from django.urls import reverse
# Create your tests here.
class PostsTests(TestCase):
    def setUp(self):
        Posts.objects.create(text="hello world")
    def test_Posts(self):
        post=Posts.objects.get(id=1)
        str=post.text
        self.assertEqual(str,"hello world")
class HomepageTest(TestCase):
    def setUp(self):
        Posts.objects.create(text="sivasankar")
    def test_url_exists_proper_location(self):
        resp=self.client.get("/")
        self.assertEqual(resp.status_code,200)
    def test_url_name(self):
        resp=self.client.get(reverse("Home"))
        self.assertEqual(resp.status_code,200)
    def test_view_uses_correct_template(self):
        resp=self.client.get(reverse("Home"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,"home.html")