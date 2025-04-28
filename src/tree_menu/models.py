"""Models for tree-menu.
"""
from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    """Модель элемента меню.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Название пункта'
    )
    menu_name = models.CharField(
        max_length=100,
        verbose_name='Название меню'
    )
    url = models.CharField(
        max_length=255,
        verbose_name='URL или named URL'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Родительский пункт'
    )
    position = models.IntegerField(
        default=0, verbose_name='Позиция'
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def get_url(self):
        """Получает URL

        Returns:
            str: адрес страницы для пункта меню
        """
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return self.url

    def __str__(self):
        return self.name
