# Generated by Django 3.2.19 on 2023-05-13 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizzeria_app', '0002_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
