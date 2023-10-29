# Generated by Django 4.2.6 on 2023-10-29 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(default='País', max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default='Ciudad', max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(default='Calle', max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]