# Generated by Django 3.2.8 on 2021-10-28 09:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20211028_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=50),
        ),
        migrations.AlterField(
            model_name='posts',
            name='liked',
            field=models.ManyToManyField(blank=True, default=0, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
