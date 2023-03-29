# Generated by Django 3.2.13 on 2023-03-22 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0003_auto_20230322_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='request',
            name='number',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('На рассмотрении', 'Under Consideration'), ('Обработано', 'Processed'), ('Закрыта', 'Closed')], default='PROCESSED', max_length=100, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='Indicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Горячая вода', 'Indicators Hot Water'), ('Холодная вода', 'Indicators Cold Water'), ('Дневной период', 'Indicators Light Day'), ('Ночной период', 'Indicators Light Night')], max_length=100, verbose_name='Показатель')),
                ('date_send', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата отправки')),
                ('indicator', models.PositiveIntegerField(default=0, verbose_name='Показатель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
