# Generated by Django 3.2.8 on 2021-10-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_posts_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='post_images/amugus.gif', upload_to='post_images'),
        ),
    ]
