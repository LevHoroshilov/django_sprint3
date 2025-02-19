from django.db import models

import datetime


class CommonModel(models.Model):
    """Абстрактная модель. Добaвляет флаг is_published и created_at."""
    is_published = models.BooleanField(
        verbose_name = 'Опубликовано', 
        default=True, 
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        #"%Y-%m-%dT%H:%M:%S%:z",
        verbose_name= 'Добавлено',
        default=str(datetime.date.today)
    )
    
    class Meta:
        abstract = True