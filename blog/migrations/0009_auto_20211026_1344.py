# Generated by Django 3.2.8 on 2021-10-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.CharField(choices=[('django', 'Django'), ('JS', 'JavaScript')], default='Django', max_length=50),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='post_images/amugus.gif', upload_to='media/post_images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='tatlikedi.jpeg', upload_to='media/profile_pics'),
        ),
    ]
