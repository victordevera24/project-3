# Generated by Django 4.0.4 on 2022-05-26 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_remove_store_user_store_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='user',
        ),
        migrations.AddField(
            model_name='store',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
