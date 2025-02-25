from django.db import models
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()


class CommonModel(models.Model):
    """Абстрактная модель. Добaвляет флаг is_published и created_at."""

    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        default=datetime.datetime.now
    )

    class Meta:
        abstract = True


class Location(CommonModel):
    name = models.CharField(verbose_name='Название места', max_length=256)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(CommonModel):
    title = models.CharField(verbose_name='Заголовок', max_length=256)
    description = models.TextField(verbose_name='Описание',)
    slug = models.SlugField(
        verbose_name='Идентификатор',
        unique=True,
        help_text='''
            Идентификатор страницы для URL;
            разрешены символы латиницы, цифры, дефис и подчёркивание.
            '''
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(CommonModel):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,default='sad'
        )
    text = models.TextField(verbose_name='Текст',default='23')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        default=datetime.datetime.now,
        help_text='''
            Если установить дату и время
            в будущем — можно делать отложенные публикации.''',
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
