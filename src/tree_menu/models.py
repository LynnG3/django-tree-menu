"""Models for the Tree Menu application."""
from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    """
    Model for storing menu items in a hierarchical structure.

    This model represents menu items that can be organized in a tree structure,
    with support for named URLs and explicit URL paths.

    Attributes:
        name (str): The display name of the menu item
        menu_name (str): Identifier for grouping menu items
        url (str): URL path or named URL for the menu item
        parent (MenuItem): Parent menu item (nullable for root items)
        position (int): Order position within the same level
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Item name'
    )
    menu_name = models.CharField(
        max_length=100,
        verbose_name='Menu name'
    )
    url = models.CharField(
        max_length=255,
        verbose_name='URL or named URL'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Parent item'
    )
    position = models.IntegerField(
        default=1,
        verbose_name='Position',
        help_text='Order number within menu level'
    )

    class Meta:
        """Meta options for MenuItem model."""
        ordering = ['position']
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def get_url(self):
        """
        Resolve URL for the menu item.

        Returns:
            str: Resolved URL path, either from named URL or direct URL
        """
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return self.url

    def __str__(self):
        """Return string representation of the menu item."""
        return self.name
