# Generated by Django 3.2.8 on 2021-10-26 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_comments_shared_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='shared_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.posts'),
        ),
    ]