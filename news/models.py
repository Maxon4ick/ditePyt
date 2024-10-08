from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase


class NewsItemTag(TagBase):
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Изображение',
        blank=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        )

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


class NewsTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        NewsItemTag,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name='Категория',
    )


class NewsItem(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название',)
    description = models.TextField(verbose_name='Описание',)
    slug = models.CharField(
        unique=True,
        max_length=50,
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления',)
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='items/',
        blank=True,
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступно',
    )
    tags = TaggableManager(through=NewsTaggedItem, related_name="tagged_items", verbose_name='Категории',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
