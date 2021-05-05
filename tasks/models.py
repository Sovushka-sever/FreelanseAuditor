from django.db import models
from django.utils import timezone
from users.model import User

STATUS_TASK_CHOICES = (
    ('O', 'open'),
    ('C', 'close'),
    ('P', 'in progress'),
)


class Task(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_task',
        verbose_name='Автор заказа',
    )
    title = models.CharField(
        verbose_name='Название заказа',
        max_length=50,
    )
    content = models.TextField(
        verbose_name='Описание заказа',
        max_length=5000
    )
    date_created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        db_index=True,
    )
    date_completion = models.DateTimeField(
        verbose_name='Дата выполнения',
        default=timezone.now
    )
    responsable = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='freelanse_task',
        verbose_name='Исполнитель заказа',
    )
    status = models.CharField(
        verbose_name='Статус выполнения',
        max_length=1,
        choices=STATUS_TASK_CHOICES,
        default='O')
    price = models.DecimalField(
        verbose_name='Цена',
        decimal_places=0,
        max_digits=10,
        default=0
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
