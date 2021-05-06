from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class UserRoles(models.TextChoices):

    FREELANCER = 'freelancer', 'Исполнитель'
    CUSTOMER = 'сustomer', 'Заказчик'


RATE_CHOICES = (
    (5, 'Excellent'),
    (4, 'Very good'),
    (3, 'Good'),
    (2, 'Not bad'),
    (1, 'Bad'),
)


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_superuser = models.BooleanField(
        default=False,
    )
    username = models.CharField(
        max_length=30,
        unique=True
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.FREELANCER,
    )
    program_language = models.TextField(
        max_length=500,
        blank=True,
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATE_CHOICES, default=1)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        ordering = ('username',)

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
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
