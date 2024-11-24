from django.db import models

class Project(models.Model):
    """ポートフォリオのプロジェクトモデル"""
    title = models.CharField('タイトル', max_length=200)
    description = models.TextField('説明')
    image = models.ImageField('画像', upload_to='portfolio/')
    url = models.URLField('URL', blank=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'プロジェクト'
        verbose_name_plural = 'プロジェクト'

    def __str__(self):
        return self.title
