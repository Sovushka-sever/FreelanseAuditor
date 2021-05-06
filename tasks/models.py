from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from users.model import User

STATUS_TASK_CHOICES = (
    ('open', 'Open'),
    ('close', 'Close'),
    ('progress', 'In progress'),
)


class Task(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_task',
    )
    title = models.CharField(
        max_length=50,
    )
    content = models.TextField(
        max_length=5000
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    date_completion = models.DateTimeField(
        default=timezone.now
    )
    responsable = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='freelanse_task',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_TASK_CHOICES,
        default='open')
    price = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        default=0,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-date_created',)
