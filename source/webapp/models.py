from django.db import models
from django.contrib.sessions.models import Session


STATUS_NEW = 'new'
STATUS_MODERATED = 'moderated'
STATUS_CHOICES = [
    (STATUS_MODERATED, 'Модерировано'),
    (STATUS_NEW, 'Новая'),
]

STATUS_DEFAULT = STATUS_NEW


class Quote(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Текст')
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(verbose_name='Email')
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name='Статус',
                              default=STATUS_DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
        ordering = ['-created_at', ]

    def __str__(self):
        return f'{self.author}, {self.text[:20]}...'


class Vote(models.Model):
    session_key = models.CharField(max_length=40, verbose_name='Ключ сессии')
    rating = models.IntegerField(choices=((1, 'up'), (-1, 'down')), verbose_name='Рэйтинг')
    quote = models.ForeignKey('webapp.Quote', related_name='votes', verbose_name='Цитата',
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quote}: {self.rating}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        ordering = ['quote', 'rating']



