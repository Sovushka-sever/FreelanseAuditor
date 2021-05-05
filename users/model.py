from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(models.TextChoices):

    FREELANCER = 'freelancer', 'Исполнитель'
    CUSTOMER = 'сustomer', 'Заказчик'


RATE_CHOICES = (
    (5, 'excellent'),
    (4, 'very good'),
    (3, 'good'),
    (2, 'not bad'),
    (1, 'bad'),
)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='e-mail',
        unique=True
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=30,
        null=True,
        unique=True
    )
    bio = models.TextField(
        verbose_name='O себе',
        max_length=500,
        blank=True,
    )
    role = models.CharField(
        verbose_name='Роль пользователя',
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.FREELANCER,
    )
    program_language = models.TextField(
        verbose_name='Язык программирования',
        max_length=500,
        blank=True,
    )
    review = models.ManyToManyField(
        'Review',
        related_name='reviews',
        blank=True,
        verbose_name='Отзыв',
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        choices=RATE_CHOICES)

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    @property
    def is_freelancer(self):
        return self.role == UserRoles.FREELANCER

    @property
    def is_customer(self):
        return self.role == UserRoles.CUSTOMER


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text
