from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    """ブログ記事モデル"""
    title = models.CharField('タイトル', max_length=200)
    content = models.TextField('内容')
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name='著者'
    )
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'ブログ記事'
        verbose_name_plural = 'ブログ記事'
    
    def __str__(self):
        return self.title