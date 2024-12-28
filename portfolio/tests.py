# portfolio/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Project

class PortfolioTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title="テストプロジェクト",
            description="テスト説明",
            image="portfolio/test.jpg"
        )

    def test_portfolio_list_view(self):
        response = self.client.get(reverse('portfolio:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/portfolio_list.html')

    def test_portfolio_detail_view(self):
        response = self.client.get(
            reverse('portfolio:detail', args=[self.project.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/portfolio_detail.html')
    
    # portfolio/tests.py に追加
    def test_invalid_project_detail(self):
        """存在しないプロジェクトへのアクセステスト"""
        response = self.client.get(
            reverse('portfolio:detail', args=[99999])  # 存在しないID
        )
        self.assertEqual(response.status_code, 404)