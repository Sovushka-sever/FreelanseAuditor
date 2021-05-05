# Generated by Django 3.2.1 on 2021-05-05 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название заказа')),
                ('content', models.TextField(max_length=5000, verbose_name='Описание заказа')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('date_completion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выполнения')),
                ('status', models.CharField(choices=[('O', 'open'), ('C', 'close'), ('P', 'in progress')], default='O', max_length=1, verbose_name='Статус выполнения')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-date_created',),
            },
        ),
    ]