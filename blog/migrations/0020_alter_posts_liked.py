# Generated by Django 3.2.8 on 2021-10-28 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20211028_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='liked',
            field=models.ManyToManyField(default=False, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
