# didcoding/didcoding/tests.py
from django.test import TestCase, Client
from django.urls import reverse

class MainViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    # didcoding/tests.py に追加
    def test_404_page(self):
        """存在しないページへのアクセステスト"""
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)